# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
#皇室战争API基础应用库
#CR API配置
def crapi(menu,tag,menu2):
    with open("lib/clashroyale/mykey.txt") as f:
        mykey=f.read().rstrip("\n")
        ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1/"
        fj = '/'
        endpoint = "/%23"
        #请求调取官方数据库   
        request = urllib.request.Request(
                base_url+menu+endpoint+tag+fj+menu2,
                None,
            {"Authorization":"Bearer %s" % mykey})
        res = urllib.request.urlopen(request,timeout=8).read().decode("utf-8")
        check = tryapi(res)
        if check == True:
            trys = json.loads(res)
            return trys
        else:
            return check
# API检查模块
def tryapi(source):
    try:
        source
    except urllib.error.URLError as e:
        data = "URLError"
    #HTTP错误
    except urllib.error.HTTPError as e:
        data = ('CRAPI-%s'%(e.code))
    #异常反馈
    except Exception as e:
        data = ("CRAPI-Error:"+e)
    #中文检查
    except UnicodeEncodeError:
        data = "CRAPI-NotSupportChinese"
    else:
        return True
    return data
#获取用户信息
def cr_user(tag):
    with open("lib/clashroyale/mykey.txt") as f:
        mykey=f.read().rstrip("\n")
        ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1"
        endpoint = "/players/%23"
        userstag = (tag)
        request = urllib.request.Request(
                   base_url+endpoint+userstag,
                   None,
                   {
                    "Authorization":"Bearer %s" % mykey
                   }
                )
        data = json.loads(urllib.request.urlopen(request).read().decode("utf-8"))
        return data["name"]
#英文API翻译