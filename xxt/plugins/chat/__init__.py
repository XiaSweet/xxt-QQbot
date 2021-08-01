from nonebot import on_message
from lib.nblib.helpers import render_expression as expr
from nonebot.adapters.cqhttp import MessageSegment,utils
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from .msxblib import xblib
#智库初始化
import lib.nblib.smartlib as e
import xxt.setting as cf
chat = on_message(rule=to_me(), priority=10, block=True)
@chat.handle()
async def _(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if cf.FixMode == True: #维护模式停服指令
        await chat.finish(expr(e.Maintenance_CHAT))
    if 'CQ:record' in args:
        await chat.finish(expr(e.txchat_voice))
    elif ('&#91;'and'&#93;') in args:
        import re
        try:
            re_msg = re.search('[^&#91;]*[\u4e00-\u9fa5]',args).group()
        except AttributeError:
            await chat.finish(MessageSegment.reply(event.message_id)+'这个表情包我似乎不太认识，不好意思啦')
        state['info'] = 'qqface'
        state['msg'] = re_msg
    elif 'CQ:image' in args:
        #await chat.finish(f'[CQ:image,file=https://s3.ax1x.com/2021/02/22/yHzupn.png'+',type=show,id=40000]')
        await chat.finish('无法分析的图片文件')
    elif args:
        state['info'] = 'texts'
        state['msg'] = args
@chat.got('msg')
async def _(bot: Bot, event: Event, state: dict):
    msg = state['msg']
    if state['info'] == 'texts':
        # 通过封装的函数获取机器人的回复并回复用户的消息
        reply = await xblib.chat(msg)
        if reply != False:
            await chat.finish(MessageSegment.reply(event.message_id)+reply)
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取回复时的「表达」
        # 这里的 expr() 函数会将一个「表达」渲染成一个字符串消息
        await chat.finish(expr(e.TXCHAT_NOANSWER))
    elif state['info'] == 'qqface':
        import chatsys
        q_dt,dt_st=await chatsys.req_dtb(state['msg'])
        if dt_st == True:
            await chat.finish(f'[CQ:image,file=https://image.dbbqb.com/'+ q_dt +',type=show,id=40000]')
        else:
            print(q_dt)
            await chat.finish('小管家的智商对你的表情居然无言以对。。。。')