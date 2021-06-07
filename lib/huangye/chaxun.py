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
        trys='查询时出现了一点小问题，请稍后再试吧'
        return False,trys
    else:
        try:
            trys = json.loads(ty)
        except:
            trys='查询时出现了一点小问题，请稍后再试吧'
            return False,trys
        else:
            return True,trys