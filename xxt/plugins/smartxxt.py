#机器人智能回复模块
from lib.nblib.helpers import render_expression as expr
import lib.nblib.smartlib as e
import xxt.setting as xtset

from nonebot import on_notice, on_message
from nonebot.adapters.cqhttp import GroupRecallNoticeEvent, Bot, Message, FriendRecallNoticeEvent, PokeNotifyEvent, \
    MessageEvent, MessageSegment
from nonebot.rule import to_me
last_message = ''
poke = on_notice(rule=to_me(), block=False)
recall = on_notice(block=False)
flash_img = on_message(block=False)


# 群聊
@recall.handle()
async def _(bot: Bot, event: GroupRecallNoticeEvent):
    mid = event.message_id
    meg = await bot.get_msg(message_id=mid)
    if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        if xtset.Debug ==True:
            await recall.finish('Debug模式：这个提示代表了机器人准备发送群聊撤回的消息了')
        elif xtset.block_delmsg==False or xtset.FixMode==True:
            await recall.finish()
        re = '刚刚说了:' + meg['message'] + '\n不要以为管家没看见！'
        await recall.finish(message=Message(re), at_sender=True)


# 私聊
@recall.handle()
async def _(bot: Bot, event: FriendRecallNoticeEvent):
    mid = event.message_id
    meg = await bot.get_msg(message_id=mid)
    if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        if xtset.Debug ==True:
            await recall.finish('Debug模式：这个提示代表了机器人准备发送私聊撤回的消息了')
        elif xtset.block_delmsg==False or xtset.FixMode==True:
            await recall.finish()
        re = '刚刚说了:' + str(meg['message']) + '\n不要以为管家没看见！'
        await recall.finish(message=Message(re))

#反对戳一下 
@poke.handle()
async def _poke(bot: Bot, event: PokeNotifyEvent, state: dict) -> None:
    if xtset.Debug ==True:
        await poke.finish('Debug模式：本提示假定机器人接收到了戳一戳消息并回复成功owo')
    #随机数模块
    import random
    sj=random.randint(0,3)
    if sj==2:
        from nonebot.log import logger
        from nonebot.message import _run_matcher as nbrun
        from xxt.plugins import mylh
        logger.info(f"[戳一戳]触发了随机模块，转接至命运轮回插件")
        await nbrun(mylh.russ_ban,bot,event,state)
        logger.info(f"[戳一戳]命运轮回执行完毕并返回反对戳一下")
        await poke.finish()
    elif sj==3:
        sj=random.randint(0,180)
        try:
            await bot.call_api("set_group_ban",**{'group_id':int(event.group_id),'user_id':int(event.user_id),'duration':int(sj)})
        except AttributeError:
            if hasattr(event,"group_id") ==False:
                await poke.finish(f'你都私信给我了我也只能跟你乐一乐了，不信你去茶话会里戳戳试试？')
            else:
                await poke.finish(f'>  '+MessageSegment.at(event.user_id)+'\n你今天堪称欧皇，小管家并不敢对你下手QAQ')
        except:
            await poke.finish(f'>  '+MessageSegment.at(event.user_id)+'\n'+f'你今天的气势堪称欧皇，小管家并不敢对你下手QAQ')
        await poke.finish(f'既然这么辛苦小管家就勉为其难放你{sj}秒假期吧(*^▽^*)')
    else:
        msg = expr(e.bye_poke)
        await poke.finish(msg, at_sender=True)
#防闪照模块
#@flash_img.handle()
#async def _(bot: Bot, event: MessageEvent):
#    msg = str(event.get_message())
#    if 'type=flash,' in msg:
#        msg = msg.replace('type=flash,', '')
#        await flash_img.finish(message=Message("不要发闪照，好东西就要分享。" + msg), at_sender=True)

#撤回闪照模块
@flash_img.handle()
async def _(bot: Bot, event: MessageEvent):
    if xtset.Debug ==True:
        await flash_img.finish('Debug模式：这个提示假定用户发送了闪照并被机器人撤回执行成功的场景')
    elif xtset.del_flushmsg==False or xtset.FixMode==True:
        await flash_img.finish()
    msg = str(event.get_message())
    if 'type=flash,' in msg:
        import random
        sj=random.randint(0,100)
        if sj<10:
            msg = msg.replace('type=flash,', '')
            #await bot.call_api("delete_msg",**{'message_id':int(event.message_id)})
            await flash_img.finish(MessageSegment.reply(event.message_id)+expr(e.fuck_flashzhao)+msg)
        else:
            await flash_img.finish()