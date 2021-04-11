# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
import argparse
parser = argparse.ArgumentParser(description='荒野战绩查询程序')
parser.add_argument('--usertag','-u',help='你的Tag，仅限国服')
args = parser.parse_args()
def req_bs(tag):
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = "https://bs.dmzgame.com/lib/json_myrecord_new.php?tag="
    #请求调取数据库
    head={'User-Agent':'Mozilla/5.0 (Linux; Android 11; M2007J17C Build/RKQ1.200826.002; wv) \
    AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 \
    Mobile Safari/537.36 MMWEBID/8504 MicroMessenger/7.0.21.1783(0x27001543) Process/appbrand0 \
    WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
          'charset':'utf-8',
          'Referer':'https://servicewechat.com/wxff59864e49e9d1f6/4/page-frame.html'}
    req = urllib.request.Request(
            base_url+tag,
            None,
            headers=head)
    try:
        ty = urllib.request.urlopen(req,timeout=8).read().decode("utf-8")
    except:
        print('查询时出现了一点小问题，请稍后再试吧')
        exit(1)
    else:
        try:
            trys = json.loads(ty)
        except:
            print('查询时出现了一点小问题，请稍后再试吧')
            exit(2)
        else:
            return ty,trys
bl,gt=req_bs(args.usertag)
def req_bs(tag):
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = "https://bs.dmzgame.com/lib/json_rank_team_member_new.php?tag="
    #请求调取数据库
    head={'User-Agent':'Mozilla/5.0 (Linux; Android 11; M2007J17C Build/RKQ1.200826.002; wv) \
    AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 \
    Mobile Safari/537.36 MMWEBID/8504 MicroMessenger/7.0.21.1783(0x27001543) Process/appbrand0 \
    WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
          'charset':'utf-8',
          'Referer':'https://servicewechat.com/wxff59864e49e9d1f6/4/page-frame.html'}
    req = urllib.request.Request(
            base_url+tag,
            None,
            headers=head)
    ty = urllib.request.urlopen(req,timeout=8).read().decode("utf-8")
yh=gt['player_info']
print('你好：'+yh['name']+'\n\
所在战队：'+yh["club_name"]+'，战队TAG：'+yh["club_tag"]+'\n\
当前奖杯：'+str(yh["trophies"])+'，近期胜率：'+str(gt["overview"][1]['value'])+'\n\
以下是近期的对战情况：')
count=0
for mc in gt['matches']:
    if count <5:
        print(mc['eventmode']+':'+mc["eventmap"]+'\
，对战英雄：'+str(mc['power'])+'级'+mc['hero_info']['name']+'\n\
比赛结果：'+mc['result']+'，英雄杯数：'+str(mc['trophies']))
        count = count + 1
    else:
        break