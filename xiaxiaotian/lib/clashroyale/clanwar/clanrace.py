# -*- coding: utf-8 -*-
import sys
sys.path.append('lib/clashroyale/')
import apilib
def views(req):
    cs = 0
    print('部落战排名如下:')
    for item in req:
        cs = cs+1
        print('%s."%s":识别码:"%s",前进：%s米,维修:%s'%(cs,item["name"],item["tag"],item["fame"],item['repairPoints']))