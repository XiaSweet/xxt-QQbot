from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.typing import T_State
#import xxt.plugins.clashroyale.get_deta as gets
from xxt.lib.helpers import render_expression as expr
import xxt.lib.systemre as e
#示例代码段
cr_cbx = on_keyword("查宝箱", rule=to_me(), priority=5,block=True)
@cr_cbx.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["msg"] = args  # 如果用户发送了参数则直接赋值
@cr_cbx.got("msg", prompt="请告诉我你要查询的用户TAG号？")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    msg = state["msg"]
    import re
    try:
        re_msg=re.search('[A-Za-z0-9]+',msg).group()
    except AttributeError:
        await cr_cbx.reject('您的TAG似乎不对，再试试吧',at_sender=True)
    else: 
    #if msg not in ["上海", "北京"]:
       # await cr_cbx.reject("你想查询的城市暂不支持，请重新输入！")
        await cr_cbx.send(expr(e.SYSTEM_WAITING),at_sender=T_State)
        msg_cr_cbx = subprocess.getoutput("python xxt/plugins/clashroyale/lib/chests.py -u '%s'"%(re_msg))
        await cr_cbx.finish(msg_cr_cbx)

cr_xyh = on_keyword({'查用户','Tag查CR','用户查询'}, rule=to_me(), priority=4,block=True)
@cr_xyh.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.message).strip()
    if args:
        state["msg"] = args
@cr_xyh.got("msg", prompt="请告诉我你要查询的用户TAG号？")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    msg = state["msg"]
    import re
    try:
        re_msg=re.search('[A-Za-z0-9]+',msg).group()
    except AttributeError:
        await cr_xyh.reject('您的TAG似乎不对，再试试吧',at_sender=True)
    else: 
        await cr_xyh.send(expr(e.SYSTEM_WAITING)+'\rPs:小管家目前的能力暂时无法解析COC与荒野的TAG号，日后更新敬请谅解',at_sender=True)
        msg_cr_xyh = await subprocess.getoutput("python xxt/plugins/clashroyale/lib/user.py -u '%s'"%(re_msg))
        await cr_xyh.finish(msg_cr_xyh)

cr_zdy = on_keyword('找队友', rule=to_me(), priority=3,block=True)
@cr_zdy.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    state["msg"] = '233'
@cr_zdy.got("msg")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    await cr_zdy.send('Ps:小管家目前的能力只能在皇室部落范围内，望稍等一下',at_sender=True)
    req_m = subprocess.getoutput("python xxt/plugins/clashroyale/lib/findfrind.py")
    await cr_zdy.finish(req_m)

cr_cwgl = on_keyword('部落战概览', rule=to_me(), priority=2,block=True)
@cr_cwgl.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    state["msg"] = '233'
@cr_cwgl.got("msg")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    await cr_cwgl.send('Ps:小管家目前的能力只能在皇室大部落范围内，望稍等一下',at_sender=True)
    req_m = subprocess.getoutput("python xxt/plugins/clashroyale/lib/viewclan.py")
    await cr_cwgl.finish(req_m)

