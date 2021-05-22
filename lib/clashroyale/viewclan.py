# -*- coding: utf-8 -*-
#外部函数引入
import apilib
req,stat = apilib.crapi('clans','88GUJ80',menu2='currentriverrace')
if stat == True:
    cs = 0
    req = sorted(req['clans'],key = lambda e:e.__getitem__('fame'),reverse = True)
    print('部落战排名如下:')
    for item in req:
        cs = cs+1
        print('%s."%s":识别码:"%s",前进：%s米,维修:%s'%(cs,item["name"],item["tag"],item["fame"],item['repairPoints']))
elif stat == False:
    print('小管家无法与CR服务器联络，请重新尝试一下吧owo')
else:
    print(req)