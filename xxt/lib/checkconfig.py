#加载变量
import sys
sys.path.append("/home/xxt-QQbot/xiaxiaotian")
sys.path.append("/home/xxt-QQbot/xiaxiaotian/lib/smartxxt")
import config
import smartlib as es
from nonebot.helpers import render_expression as expr
def check_main():
    if config.Maintenance == True:
        return(expr(es.Maintenance_CHAT))
    elif config.Maintenance == False:
        return
    else:
        config.Maintenance = True
        return('配置文件有错误，请联系管理员修复吧')