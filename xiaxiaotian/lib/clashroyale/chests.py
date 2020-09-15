# -*- coding: utf-8 -*-
#debug使用
#import time
#start = time.time()
import argparse
#外部函数引入
from apilib import crapi,cr_user
parser = argparse.ArgumentParser(description='CR宝箱查询程序')
parser.add_argument('--usertag','-u',help='你的Tag')
args = parser.parse_args()
tag = (args.usertag)
req = crapi('players',tag,'upcomingchests')
if req != False:
    print ('查询的用户:'+cr_user(tag)+',未来的宝箱如下Ovo:')
    for item in req ["items"]:
                    chest = ("宝箱位置:+%s,宝箱名称:%s" % (
                                    item["index"], 
                                    item["name"]
                            ))  
                    chest = chest.replace('Silver Chest','普通银箱')
                    chest = chest.replace('Magical Chest','魔法紫箱')
                    chest = chest.replace('Golden Chest','黄金宝箱')
                    chest = chest.replace('Giant Chest','巨型宝箱')
                    chest = chest.replace('Mega Lightning Chest','国王闪电宝箱（提前恭喜啦Ovo）')
                    chest = chest.replace('Legendary Chest','传奇宝箱')
                    chest = chest.replace('Epic Chest','史诗宝箱')
                    chest = chest.replace('+0','下个宝箱')
                    print (chest)
else:
    print(req)