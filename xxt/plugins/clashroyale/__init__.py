from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event,MessageSegment
from nonebot.typing import T_State
#import xxt.plugins.clashroyale.get_deta as gets
from lib.nblib.helpers import render_expression as expr
import lib.nblib.smartlib as e
#查宝箱
cr_cbx = on_keyword("查宝箱", rule=to_me(), priority=4,block=True)
@cr_cbx.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).replace(' ','')
    args = str(event.get_message()).replace('\n','')    # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args !='查宝箱':
        #await cr_cbx.send(args,at_sender=True)
        import re
        try:
            bdzh=re.search('@[1-9]+',args).group()
        except AttributeError:
            try:
                re_msg=re.search('[A-Za-z0-9]+',args).group()
            except AttributeError:
                await cr_cbx.reject(MessageSegment.reply(event.message_id)+'您的TAG似乎不对，再试试吧',at_sender=True)
            except:
                await cr_cbx.finish(MessageSegment.reply(event.message_id)+'出现了一些未知的错误，请稍后再试试吧',at_sender=True)
            else:
                if re_msg!='':
                    state["msg"] = re_msg # 如果用户发送了参数则直接赋值
        except:
            await cr_cbx.finish(MessageSegment.reply(event.message_id)+'出现了一些未知的错误，请稍后再试试吧',at_sender=True)
        else: 
            if bdzh!='':
                bdzh=bdzh.replace('@','')
                from .get_deta import bdk
                import xxt.setting as xs
                bdzh=await bdk(event.user_id,bdzh,xs.yyk)
                if bdzh == None:
                    await cr_cbx.finish(expr(e.mbid),at_sender=True)
                else:
                    state["msg"]=bdzh
    else:
        import lib.sqlcx as sql
        jg,stat=sql.cx(event.user_id)
        if stat==True:
            state["msg"] = jg
        elif stat=='Wait':
            await cr_cbx.reject(jg,at_sender=True)
        if stat==False:
            await cr_cbx.finish(MessageSegment.reply(event.message_id)+'对不起，我确实不记得你有绑定过CR的账号，无法提供服务，请检查后再试QaQ。\n绑定账户方式：账户绑定+空格+你的Tag号（不区分游戏）')

@cr_cbx.got("msg", prompt="请告诉我你要查询的用户TAG号？")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    msg = state["msg"]
    await cr_cbx.send(f'>  '+MessageSegment.at(event.user_id)+expr(e.SYSTEM_WAITING)) # expr(e.SYSTEM_WAITING)
    from .get_deta import cbx as gdata
    msg_cr_cbx = await gdata(msg,'cr_cbx')
    await cr_cbx.finish(MessageSegment.reply(event.message_id)+msg_cr_cbx)

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
#找队友
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
    await cr_cwgl.send(expr(e.SYSTEM_WAITING),at_sender=True)
    from .get_deta import cr_blzgl
    req_m =await cr_blzgl('dbl')
    await cr_cwgl.finish(req_m)



#以下代码用于注册Nonebot自动化的CR部落运营统计服务
from nonebot import require,get_driver,get_bot
scheduler = require("nonebot_plugin_apscheduler").scheduler
# 每日0点自动@主人
@scheduler.scheduled_job(
    'cron',
    hour=0,
    minute=26,
)
async def _():
    from .get_deta import auto_upnoice
    bot=get_bot()
    re=await auto_upnoice()
    try:
        a=await bot.call_api("_send_group_notice",**{'group_id':1062326148,'content':str(re)})
        a=await bot.call_api("_send_group_notice",**{'group_id':240253684,'content':str(re)})
    except:
        print('出现了错误，错误信息如下：')
        print(a)