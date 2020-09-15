# -*- coding: utf-8 -*-
import sys
sys.path.append('lib/clashroyale/')
#外部函数引入
from apilib import *
from clanrace import *
req = crapi('clans','88GUJ80','currentriverrace')
if req != False:
    cs = 0
    req = sorted(req['clans'],key = lambda e:e.__getitem__('fame'),reverse = True)
    print('部落战排名如下:')
    for item in req:
        cs = cs+1
        print('%s."%s":识别码:"%s",前进：%s米,维修:%s'%(cs,item["name"],item["tag"],item["fame"],item['repairPoints']))
else:
    print(req)