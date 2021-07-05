#Nonebot2基础模块
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event,MessageSegment
from nonebot.typing import T_State
tingsong = on_keyword("music",rule=to_me(), priority=2, block=True)
@tingsong.handle()
async def _(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    import pymysql
    import xxt.setting as xc
    conn = pymysql.connect(**xc.yyk)
    cursor = conn.cursor()
    hard=None
    if hard==None:
        jg=cursor.execute(f"SELECT * FROM `TingSong`")
    else:
        jg=cursor.execute(f"SELECT * FROM `TingSong` WHERE `Hand` LIKE '{hard}'")
    import random
    jg=random.randint(0,jg)
    state['id']=jg
    jg=cursor.execute(f"SELECT * FROM `TingSong` WHERE `id`='{jg}'")
    lists = cursor.fetchall()
    #获取抽到的曲库信息
    state['downlink']=lists[0][3]
    state['singer']=lists[0][2]
    state['name']=lists[0][1]
    conn.close()
@tingsong.got('id')
async def _(bot: Bot, event: Event, state: dict):
    #import os
    #m=os.getcwd()
    name=state['name']
    singer=state['singer']
    dl=state['downlink']
    await tingsong.send(f'欢迎提前来到听歌识曲库，猜猜你能不能猜对(⊙o⊙)哦\nPS:在小管家听歌识曲插件完成前你还有点时间熟悉一下，有需要放入曲库的请剪辑后发送给部落管理员哦\n演示歌曲：{name} By {singer}')
    m=MessageSegment.record(file=f'{dl}',cache=0,magic=1,timeout=30)
    await tingsong.finish(m)