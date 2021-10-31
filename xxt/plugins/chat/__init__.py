from nonebot import on_message
from lib.nblib.helpers import render_expression as expr
from nonebot.adapters.cqhttp import MessageSegment,utils
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
#智库初始化
import lib.nblib.smartlib as e
import xxt.setting as cf
from .cloud_chat import txNLP
chat = on_message(rule=to_me(), priority=100, block=True)
@chat.handle()
async def _(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if cf.FixMode == True: #维护模式停服指令
        await chat.finish(expr(e.Maintenance_CHAT))
    if 'CQ:record' in args: #语音侦测
        await chat.finish(expr(e.txchat_voice))
    elif ('&#91;'and'&#93;') in args: #斗图表情包
        import re
        try:
            re_msg = re.search('[^&#91;]*[\u4e00-\u9fa5]',args).group()
        except AttributeError:
            await chat.finish(MessageSegment.reply(event.message_id)+'这个表情包我似乎不太认识，不好意思啦')
        state['info'] = 'qqface'
        state['msg'] = re_msg
    elif 'CQ:image' in args:
        #图片分析模块
        state['info'] = 'image'
        args=args.replace(']','')
        import re
        try:
            re_msg = re.search('[a-zA-z]+://[^\s]*',args).group()
        except AttributeError:
            await chat.finish(MessageSegment.reply(event.message_id)+'这个图片你觉得我能看懂吗？')
        #await chat.finish(f'[CQ:image,file=https://s3.ax1x.com/2021/02/22/yHzupn.png'+',type=show,id=40000]')
        finally:
            if cf.Debug == True:
                print('[智能闲聊]提取图片链接成功，用户给小管家发了张图片')
        gime=False #xblib.get_image(re_msg)
        if gime ==True:
            state['msg']= '/home/tmp/tmp.jpg'
        else:
            await chat.finish(f"这个图片你觉得我能看懂吗")
    elif args:
        state['info'] = 'texts'
        state['msg'] = args
@chat.got('msg')
async def _(bot: Bot, event: Event, state: dict):
    msg = state['msg']
    if state['info'] == 'texts':
        # 通过封装的函数获取机器人的回复并回复用户的消息
        reply = await txNLP.chat(msg,cf.TXCloud_id,cf.TXCloud_key)
        if reply['stat'] == True:
            print(f'[智能闲聊]成功从云端获取解答，自信度：{reply["Confidence"]}')
            await chat.finish(MessageSegment.reply(event.message_id)+reply['reply'])
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取回复时的「表达」
        # 这里的 expr() 函数会将一个「表达」渲染成一个字符串消息
        elif reply['stat'] == False:
            print(f'[智能闲聊]已知原因导致链接失败，已返回解答，C端无感知\nDebug信息:{reply["code"]}\n出现错误了：{reply["msg"]}')
            await chat.finish(expr(e.TXCHAT_NOANSWER))
        else:
            await chat.finish(expr(e.TXCHAT_NOANSWER))
    elif state['info'] == 'image':
        # 通过封装的函数获取机器人的回复并回复用户的消息
        reply = False # await xblib.imgchat(msg)
        if reply != False:
            await chat.finish(MessageSegment.reply(event.message_id)+reply)
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取回复时的「表达」
        # 这里的 expr() 函数会将一个「表达」渲染成一个字符串消息
        if cf.Debug == True:
            await chat.finish('Debug: 成功获取到了图片，但是微博方面没有回应故回复失败QAQ')
        else:
            await chat.finish('这个图片你觉得我能看懂吗？')
    elif state['info'] == 'qqface':
        import chatsys
        q_dt,dt_st=await chatsys.req_dtb(state['msg'])
        if dt_st == True:
            await chat.finish(f'[CQ:image,file=https://image.dbbqb.com/'+ q_dt +',type=show,id=40000]')
        else:
            print(q_dt)
            await chat.finish('小管家的智商对你的表情居然无言以对。。。。')