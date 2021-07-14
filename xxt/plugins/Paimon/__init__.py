#Nonebot2基础模块
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event,MessageSegment
from nonebot.typing import T_State
paimon = on_keyword("原神",rule=to_me(), priority=2, block=True)
@paimon.handle()
async def _(bot: Bot, event: Event, state: dict):
    await paimon.finish(MessageSegment.record(file=f"https://genshin.minigg.cn/?char=barbara&id=1201&lang=cn",cache=0,magic=1,timeout=30))