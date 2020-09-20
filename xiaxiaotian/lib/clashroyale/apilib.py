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
        res,check = tryapi(request)
        if check == True:
            trys = json.loads(res)
            return trys,True
        else:
            return res,False
# API检查模块
def tryapi(request):
    try:
        ty = urllib.request.urlopen(request,timeout=8).read().decode("utf-8")
    #HTTP错误
    except urllib.error.HTTPError as e:
        return 'CRAPI-%s'%(e.code),False
    except urllib.error.URLError as e:
        return "URLError-%s"%(e),False
    #异常反馈
    except Exception as e:
        return "CRAPI-Error:%s"%(e),False
    #中文检查
    except UnicodeEncodeError:
        return "CRAPI-NotSupportChinese",False
    else:
        return ty,True
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