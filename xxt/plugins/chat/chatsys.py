async def req_dtb(msg):
    #访问API基础应用库
    import urllib.request
    import urllib.error
    import json
    import ssl
    from urllib.parse import quote
    import string
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}
    url = "https://www.dbbqb.com/api/search/json?w="+msg
    #请求API并检查错误
    reqs=quote(url, safe=string.printable) 
    req=urllib.request.Request(reqs,headers=ua_headers)
    try:
        req=urllib.request.urlopen(req).read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return 'HTTPError出现错误了：%s'%(e.code),False
    except urllib.error.URLError as e:
        return "URLError出现错误了：%s"%(e),False
    except Exception as e:
        return "Exception出现错误了：%s"%(e),False
    #开始分析返回地址
    req = json.loads(req)
    import random
    suiji=random.randint(0,5)
    return req[suiji]['path'],True