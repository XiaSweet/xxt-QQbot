from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from lib.clashroyale.chests import cbx

weather = on_command("天气", rule=to_me(), priority=5)

@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="请回复我您的TAG识别号")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    #if city not in ["上海", "北京"]:
       # await weather.reject("你想查询的城市暂不支持，请重新输入！")
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    return cbx(city)
