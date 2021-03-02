# -*- coding: utf-8 -*-
import argparse
import datetime
#外部函数引入
import apilib
import fanyi
#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序 - 用户详细信息')
parser.add_argument('--usertag','-u',help='你要查询的Tag')
args = parser.parse_args()
tag = (args.usertag)
data,stat = apilib.crapi('players',tag)
if stat == False:
    print(req)
if stat == True:
    user,clan=apilib.cr_user(tag)
    print('久等了，用户"'+user+'"的详细信息：')
    user = ("个人信息:\n所在竞技场:%s ，国王塔等级:%s\n目前杯数:%s，最高杯数:%s")%(
        data["arena"]["name"],
        data["expLevel"],
        data["trophies"],
        data["bestTrophies"])
    clan = ("部落信息:\n所在部落:%s，部落Tag:%s\n本周捐卡:%s，本周收卡:%s\n部落职位:%s") %(
        data["clan"]["name"],
        data["clan"]["tag"],
        data["donations"],
        data["donationsReceived"],
        data["role"],)
    user = fanyi.aruna(user)
    user = fanyi.gr_dj(user)
    clan = fanyi.cl_zw(clan)
    print(user)
    print(clan)
    print('想查询更加详细的用户信息吗？敬请浏览：')
    royapi = ("https://royaleapi.com/player/%s（英文）")%(args.usertag)
    print(royapi)
    print('小管家猜测您似乎需要:"宝箱查询"或"部落查询"可以发送指令查询(⊙o⊙)哦')
else:
    print('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')