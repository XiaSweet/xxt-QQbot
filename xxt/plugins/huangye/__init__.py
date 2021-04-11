from nonebot import on_keyword
from nonebot.rule import to_me,keyword
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.typing import T_State
from xxt.lib.helpers import render_expression as expr
import xxt.lib.systemre as e
#示例代码段
hy_czj = on_keyword("荒野查询", rule=to_me(), priority=5,block=True)
@hy_czj.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["msg"] = args  # 如果用户发送了参数则直接赋值
@hy_czj.got("msg", prompt="请告诉我你要查询的用户TAG号,仅限荒野国服(⊙o⊙)哦")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    msg = state["msg"]
    import re
    try:
        re_msg=re.search('[A-Za-z0-9]+',msg).group()
    except AttributeError:
        await hy_czj.reject('您的TAG似乎不对，再试试吧',at_sender=True)
    else: 
    #if msg not in ["上海", "北京"]:
       # await hy_czj.reject("你想查询的城市暂不支持，请重新输入！")
        async def hy_cx(tag:str):
            import subprocess
            req = subprocess.getoutput("python xxt/plugins/huangye/lib/chaxun.py -u '%s'"%(tag))
            return req
        await hy_czj.send(expr(e.SYSTEM_WAITING),at_sender=T_State)
        msg_hy_czj = await hy_cx(re_msg)
        await hy_czj.finish(msg_hy_czj)
