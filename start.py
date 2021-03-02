import nonebot
from sys import path
path.append('/etc/xxt/')
path.append('xxt/')
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugins("xxt/plugins")
if __name__ == "__main__":
    nonebot.run()