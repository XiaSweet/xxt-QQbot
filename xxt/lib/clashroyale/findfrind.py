# -*- coding: utf-8 -*-
import datetime
#外部函数引入
import apilib
dbltag = "88GUJ80"
xbltag = "JY8YVC0"
dblret,stat = apilib.crapi('clans',dbltag,'members')
if dblret == (400 or 404 or 403 or CRTimeOut or CRNotCallMe):
    print('出现错误了，请稍候再查询一下吧')
    exit()
xblret,stat = apilib.crapi('clans',xbltag,'members')
now = datetime.datetime.utcnow()
#初始化变量数据
match = 0
for item in dblret["items"]:
    item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
    if now - item_utc <= datetime.timedelta(minutes=30):
        dblshow = True
        show = True
        break
    else:
        pass
for item in xblret["items"]:
    item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
    if now - item_utc <= datetime.timedelta(minutes=30):
        xblshow = True
        show = True
        break
    else:
        pass
if show != True:
    print("全部落的队友最近都不在线哦，稍候再看看吧")
elif show == True:
    print("以下是最近上线的队友:")
    if dblshow == True:
        print('大部落：')
        for item in dblret["items"]:
                #格式化时间
            item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
            if match > 10:
                print('刚才可能还有更多的伙伴在线哦，请登录皇室战争客户端核实一下吧')
                break
            elif now - item_utc <= datetime.timedelta(minutes=30):
                match = match + 1
                date_str = datetime.datetime.strftime(item_utc ,'%Y-%m-%d %H:%M:%S')
                local_date = item_utc + datetime.timedelta(hours=8)
                local_date_str = datetime.datetime.strftime(local_date ,'%m-%d %H:%M')
                memstat =  ("成员：%s,上线时间：%s" % (
                    item["name"],
                    local_date_str))
                print(memstat)
    if xblshow == True:
        print('小部落：')
        for item in xblret["items"]:
            #格式化时间
            item_utc = datetime.datetime.strptime(item["lastSeen"], "%Y%m%dT%H%M%S.%fZ")
            if match > 10:
                print('刚才可能还有更多的伙伴在线哦，请登录皇室战争客户端核实一下吧')
                break
            elif now - item_utc <= datetime.timedelta(minutes=30):
                match = match + 1
                date_str = datetime.datetime.strftime(item_utc ,'%Y-%m-%d %H:%M:%S')
                local_date = item_utc + datetime.timedelta(hours=8)
                local_date_str = datetime.datetime.strftime(local_date ,'%m-%d %H:%M')
                memstat =  ("成员：%s,上线时间：%s" % (
                    item["name"],
                    local_date_str))
                print(memstat)
    else:
        print('CRNotError')