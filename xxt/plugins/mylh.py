from nonebot import on_command, require,on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import GROUP, Bot, Event
from nonebot.typing import T_State
from lib.nblib.helpers import render_expression as expr
import lib.nblib.smartlib as e
import random
russ_ban = on_keyword("命运轮回", rule=to_me(), priority=4,block=True)
@russ_ban.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    import random
    state["sjz"] = random.random()
@russ_ban.got("sjz")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    sjz=state["sjz"] #随机禁言自律模块
    if hasattr(event,"group_id") ==False:
        await russ_ban.finish(f'你都私信给我了我也只能跟你乐一乐了，不信你去茶话会里玩命运轮回试试？')
    async def zxjy(gid,qid,sc,ts,bg,s='秒'):
        try:
            await bot.call_api("set_group_ban",**{'group_id':int(gid),'user_id':int(qid),'duration':int(sc)})
        except AttributeError:
            if hasattr(event,"group_id") ==False:
                await russ_ban.finish(f'你都私信给我了我也只能跟你乐一乐了，不信你去茶话会里玩命运轮回试试？')
            else:
                await russ_ban.finish(f'你今天堪称欧皇，小管家并不敢对你下手QAQ',at_sender=True)
        except:
            await russ_ban.finish(f'你今天的气势堪称欧皇，小管家并不敢对你下手QAQ',at_sender=True)
        if s=='分':
            sc=sc//60
            await russ_ban.finish(f'您的运气值{ts}，恭喜你获得禁言{sc}{s}套餐{bg}',at_sender=True)
        else:
            await russ_ban.finish(f'您的运气值{ts}，恭喜你获得禁言{sc}{s}套餐{bg}',at_sender=True)
    if sjz < 0.35:
        await russ_ban.finish('恭喜你，你的运气差到跟小管家难兄难弟了，吃亏是福啊（*＾-＾*）',at_sender=True)
    elif 0.35<sjz and sjz<0.7:
        jy=random.randint(0,60)
        await zxjy(event.group_id,event.user_id,jy,'还算可以','(⊙﹏⊙)祝你好运')
    elif 0.7<sjz and sjz<0.95:
        jy=random.randint(0,20)
        jy=60*jy
        await zxjy(event.group_id,event.user_id,jy,'相当不错','(oﾟvﾟ)ノ',s='分')
    else:
        try:
            await bot.call_api("set_group_ban",**{'group_id':int(event.group_id),'user_id':int(event.user_id),'duration': 88888})
        except AttributeError:
            if hasattr(event,group_id) ==False:
                await russ_ban.finish(f'你都私信给我了我也只能跟你乐一乐了，不信你去茶话会里玩命运轮回试试？')
            else:
                await russ_ban.finish(f'你今天堪称欧皇，小管家并不敢对你下手QAQ',at_sender=True)
        except:
            await russ_ban.finish(f'你今天堪称欧皇，小管家并不敢对你下手QAQ',at_sender=True)
        await russ_ban.finish('错误提示：\n恭喜你，由于小管家相当讨厌欧皇，所以恭喜万众瞩目的阁下获得禁言套餐Plus：88888(约1天)\
的奖励，请等待管理员主动解除或@Ver.冬瓜萌萌，再来不便敬请谅解！\nPs:本套餐中奖概率极低，阁下今天具有大展身手的潜力，加油✧(≖ ◡ ≖✿)',at_sender=True)