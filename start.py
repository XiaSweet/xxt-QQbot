import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
nonebot.init()
#nonebot.load_plugin("nonebot_plugin_russian")
#nonebot.load_plugin("nonebot_plugin_test")
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugins("xxt/plugins")
if __name__ == "__main__":
    nonebot.run()
