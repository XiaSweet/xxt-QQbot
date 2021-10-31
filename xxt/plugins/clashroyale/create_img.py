import lib.apilib as apilib
import json
dbltag = "88GUJ80"
qingqiu,stat =apilib.crapi('clans',dbltag,menu2='currentriverrace')
if stat == False:
    print('很抱歉，出现了一点小问题，请留意下方错误日志：')
    print(qingqiu)
    exit(2)
else:
    try:
        qingqiu = sorted(qingqiu['clan']['participants'],key = lambda e:e.__getitem__('fame'),reverse = True)
    except:
        print(qingqiu)
    else:
        print('部落战数据请求完成')
        qingqiu=json.dumps(qingqiu)
        print(qingqiu)
    
