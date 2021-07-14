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
    if xtset.Debug ==True:
        await recall.finish('Debug模式：这个提示代表了机器人准备发送群聊撤回的消息了')
    elif xtset.block_delmsg==False or xtset.FixMode==True:
        await recall.finish()
    mid = event.message_id
    meg = await bot.get_msg(message_id=mid)
    if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re), at_sender=True)


# 私聊
@recall.handle()
async def _(bot: Bot, event: FriendRecallNoticeEvent):
    if xtset.Debug ==True:
        await recall.finish('Debug模式：这个提示代表了机器人准备发送私聊撤回的消息了')
    elif xtset.block_delmsg==False or xtset.FixMode==True:
        await recall.finish()
    mid = event.message_id
    meg = await bot.get_msg(message_id=mid)
    if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        re = '刚刚说了:' + str(meg['message']) + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re))

#反对戳一下
@poke.handle()
async def _poke(bot: Bot, event: PokeNotifyEvent, state: dict) -> None:
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