# -*- coding: utf-8 -*-
import sys
sys.path.append('lib/clashroyale/')
import argparse
#外部函数引入
from your import *
from apilib import *
#外部函数引入
parser = argparse.ArgumentParser(description='CR查询程序-0捐查询')
parser.add_argument('--tag', '-c', help='填写代码')
args = parser.parse_args()

if args.tag == 'xblszl':
    dbltag = "88GUJ80"
    xbltag = "JY8YVC0"
    shenshou = False
elif args.tag == 'dbljiangji':
    tag = "88GUJ80"
    clanid = '大部落'
    shenshou = True
elif args.tag == 'xbljiangji':
    tag = "JY8YVC0"
    clanid = '小部落'
    shenshou = True
elif args.tag == 'juankaapi':
    print('为防止小管家被滥用，如需查询全部的捐卡信息，敬请手动浏览以下网址(英文):'+'\n'
   +'大部落：https://royaleapi.com/clan/88GUJ80 \n小部落: https://royaleapi.com/clan/JY8YVC0'
    )
    exit()
else:
    print ('ERROR-CRNotMyClans')
    exit()
if shenshou == True:
    ret = crapi('clans',tag,'members')
    print (ret)
elif shenshou == False:
    stat = 0
    for item in request["items"]:
            if item["donationsReceived"]  - item["donations"]  >40:
                stat = 1
                break
            else:
                pass
    if stat == 0:
        print (('%s目前没有发现伸手党，请继续努力哦，Bye(⊙o⊙)！')%(clanid))
    elif stat == 1:
        print(("以下是%s的全部伸手党信息:")%(clanid))
        for item in request["items"]:
            if item["donationsReceived"]  - item["donations"]  >40:
                mem = ("成员：%s,捐卡：%d,接卡:%s,差距:%s,Tag: %s " % (
                    item["name"], 
                    item["donations"],
                    item["donationsReceived"], 
                    item["donationsReceived"] - item["donations"],
                    item["tag"]
                        ))
                print(mem)
            else:
                continue
        print ('注：如果您想继续查询成员信息可使用"用户查询"服务')
    else:
         print('CRNotError')