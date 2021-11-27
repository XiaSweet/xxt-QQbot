import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
nonebot.init()
#nonebot.load_plugin("nonebot_plugin_russian")
#nonebot.load_plugin("nonebot_plugin_test")
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
#nonebot.load_plugin("nonebot_plugin_russian")
nonebot.load_plugins("xxt/plugins")
#时区设置/激活自动任务
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})
nonebot.init(apscheduler_autostart=True)
if __name__ == "__main__":
    nonebot.run()
