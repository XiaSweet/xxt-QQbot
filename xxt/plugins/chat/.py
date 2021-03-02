async def text(msg):
    import xxt.lib.txai_chat.chat as txchat
    # 通过封装的函数获取机器人的回复
    reply = await txchat.anso(msg,TXAI_ID,TXAI_KEY)
    if reply:
        await chat.finish(escape(reply))
    # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取回复时的「表达」
    # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
    await chat.finish(expr(e.TXCHAT_NOANSWER))