import sys
sys.path.append('lib/clashroyale/')
import apilib
import fanyi
import argparse
parser = argparse.ArgumentParser(description='夏小甜管家 - 部落战查询')
parser.add_argument('--Tag','-t',help='查询的部落TAG')
args = parser.parse_args()
#开始运行
tag = (args.Tag)
req,stat = apilib.crapi('clans',tag,'')
if stat == True:
    print('久等了，查询的部落: %s'%(req['name']))
    print('部落战杯数:%s 部落总杯数:%s 成员:%s 部落周捐:%s \n部落要求:%s 进入门槛:%s\n部落简介:\n%s'%(
     req['clanWarTrophies'],req['clanScore'],req['members'],req['donationsPerWeek'],fanyi.clans(req['type']),req['requiredTrophies'],req['description']))
    print('请在RoyaleAPI查阅详细信息:https://royaleapi.com/clan/%s'%(tag))
else:
    print(req)