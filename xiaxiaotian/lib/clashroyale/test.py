# -*- coding: utf-8 -*-
#外部函数引入
from apilib import *
req = crapi('clans','88GUJ80','currentriverrace')
if tryapi(req) == False:
    print(req)
else:
    print('Error')