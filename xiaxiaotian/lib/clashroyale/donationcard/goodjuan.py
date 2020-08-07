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
    for item in ret["items"]:
            #检查部落是否有捐卡不合格长老
            if item["donations"] < 360 and item["role"] == 'elder':
                good = False
                break
            else:
                pass
    if not good == False:
        print (('恭喜恭喜，目前还没有可需要降级的伙伴，请继续努力哦(⊙o⊙)！'))
    elif good == False:
        print(("又到一周长老时，有人欢喜有人忧owo\n以下是%s部落未通过考核的清单:"))%(clanid)
        for item in retdbl["items"]:
            #部落长老留职条件对比
            if item["role"] == 'elder':
                if item["donations"] > 359 and item["donationsReceived"] - item["donations"] < 1:
                    continue
                elif item["donations"] > 359 and item["donationsReceived"] - item["donations"] > 0:
                    yuanyin = '\n考核通过但卡牌收大于捐，提醒1次。捐收差距：%s'%(item["donationsReceived"] - item["donations"])
                elif item["donations"] < 359 and item["donations"] > 10 and item["donationsReceived"] - item["donations"] < 100:
                    yuanyin = '\n周捐未达标，捐卡：%s'%(item["donations"])
                elif item["donations"] < 359 and item["donations"] > 10 and item["donationsReceived"] - item["donations"] > 100:
                    yuanyin = '\n周捐未达标且伸手较广，警告1次并降职wow捐收差距：%s'%(item["donationsReceived"] - item["donations"])
                elif item["donations"] < 10 and item["donationsReceived"] - item["donations"] > 0:
                    yuanyin = '\n米奇妙妙屋一般的妙！捐卡木有伸手强，又凉部落又凉心，3天不解释，飞机票走好！捐收差距：%s'%(item["donationsReceived"] - item["donations"])
                elif item["donations"] < 10 and item["donationsReceived"] - item["donations"] < 0:
                    yuanyin = '\n本周伸手党，捐收差距：%s'%(item["donationsReceived"] - item["donations"])
                mem = ("成员：%s，识别码:%s，详细原因：%s" % (
                    item["name"], 
                    item["tag"],
                    yuanyin
                        ))
                print(mem)
    else:
        print('CRNotError')
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