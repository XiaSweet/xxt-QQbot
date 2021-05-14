# -*- coding: utf-8 -*-
#debug使用
#import time
#start = time.time()
import argparse
#外部函数引入
import apilib
import fanyi
parser = argparse.ArgumentParser(description='CR宝箱查询程序')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()
tag = (args.usertag)
req,stat = apilib.crapi('players',tag,'upcomingchests')
if stat == True:
    user,clan=apilib.cr_user(tag)
    print ('你好，来自'+clan+'的"'+user+'":')
    chest = ("下个宝箱：%s" % (req["items"][0]["name"]))
    chest = fanyi.chest(chest)
    print (chest)
    stat = 1
    for item in req ["items"]:
        if stat == 1:
            stat = stat+1
            pass
        else:
            chest = ("宝箱位置+%s：%s" % (item["index"],item["name"]))
            chest = fanyi.chest(chest)
            print (chest)
elif stat == False:
    print(req)
    #print('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')
else:
    print('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')