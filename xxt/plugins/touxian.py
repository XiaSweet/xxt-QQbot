from nonebot import on_command, require,on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import GROUP, Bot, Event
from nonebot.typing import T_State
from lib.nblib.helpers import render_expression as expr
import lib.nblib.smartlib as e
txxg = on_keyword("改称呼", rule=to_me(), priority=4,block=True)
@txxg.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    if event.user_id==1172608638:
        state["cjyh"]=True
    else:
        state["cjyh"]=False
@txxg.got("cjyh")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    x=state["cjyh"] #头衔自定义功能
    async def gtx(cg):
        args = str(event.get_message()).replace(' ','')
        qid=0
        if cg==True:
            import re
            try:
                qid=re.search('@[0-9]*',args).group()
            except:
                qid=event.user_id
            else:
                qid=qid.replace('@','')
            qid=int(qid)
        if qid==0:
            qid=event.user_id
        try:
            tx=re.search('#.*',args).group()
        except AttributeError:
            await txxg.reject('亲爱的Master，我暂时无法定位到需要修改的昵称,请重新试一下QaQ\n小提示：请使用"#你想要的称呼"用以授予头衔',at_sender=True)
        except:
            await txxg.reject('尝试查找修改昵称时出现问题了，请重新试一下',at_sender=True)
        tx=tx.replace('#','')
        try:
            await bot.call_api("set_group_special_title",**{f'group_id':1062326148,'user_id':int(qid),'special_title':tx})
        except:
            await txxg.finish(f'小管家在修改时遇到BUG了，非常抱歉',at_sender=True)
        await txxg.finish(f'我收到了您的请求并已授予部落茶话会的专属头衔:{tx},尽请留意',at_sender=True)
    if x==True:
        await gtx(True)
    elif x==False:
        await gtx(False)
    else:
        await txxg.finish(f'出现错误了：\n无法判定超级管理，请稍后再试',at_sender=True)