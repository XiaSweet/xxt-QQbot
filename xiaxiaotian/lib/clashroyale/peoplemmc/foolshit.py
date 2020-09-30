# -*- coding: utf-8 -*-
import datetime
#外部函数引入
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("/home/xxt-QQbot/xiaxiaotian/lib/smartxxt")
sys.path.append("lib/clashroyale")
import apilib
import systemre as e
dbltag = "88GUJ80"
xbltag = "JY8YVC0"
dblret = apilib.crapi('clans',dbltag,'members')
if dblret == (400 or 404 or 403 or CRTimeOut or CRNotCallMe):
    print('出现错误了，请稍候再查询一下吧')
    exit()
xblret = apilib.crapi('clans',xbltag,'members')
now = datetime.datetime.utcnow()
#初始化变量数据
match = 0
dblshow = False
xblshow = False
for item in dblret["items"]:
    item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
    if now - item_utc > datetime.timedelta(days=5):
        dblshow = True
        show = True
        break
    else:
        pass
for item in xblret["items"]:
    item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
    if now - item_utc > datetime.timedelta(days=7):
        xblshow = True
        show = True
        break
    else:
        pass
if show != True:
    print("Very Good,没有部落的伙伴是木头人，加油owo")
elif show == True:
    print("%s木头人清单如下:"%(expr(e.APP_FOOLSHIT)))
    if dblshow == True:
        print('大部落：')
        for item in dblret["items"]:
                #格式化时间
            item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
            if match > 8:
                print('还有不少木头人，管理怎么看的部落啊，请自己前往游戏查看吧')
                break
            elif now - item_utc > datetime.timedelta(days=5):
                match = match + 1
                date_str = datetime.datetime.strftime(item_utc ,'%Y-%m-%d %H:%M:%S')
                memstat =  ("成员：%s,Tag:%s,%s天未登录" % (
                    item["name"],
                    item["tag"],
                    now.day - item_utc.day))
                print(memstat)
    if xblshow == True:
        print('小部落：')
        for item in xblret["items"]:
            #格式化时间
            item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
            if match > 10:
                break
            elif now - item_utc > datetime.timedelta(days=7):
                match = match + 1
                date_str = datetime.datetime.strftime(item_utc ,'%Y-%m-%d %H:%M:%S')
                memstat =  ("成员：%s,Tag:%s,%s天未登录" % (
                    item["name"],
                    item["tag"],
                    now.day - item_utc.day))
                print(memstat)
    else:
        print('出现错误了，请稍后再试试吧')