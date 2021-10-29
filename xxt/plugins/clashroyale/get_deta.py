#导入插件的小技巧：没有必要为了节约空间而浪费时间去处理事情。请注意备注好你需要的代码
#部落查宝箱模块
async def cbx(tag: str,rw):
    #外部函数引入
    import lib.cr.apilib as apilib
    import lib.cr.fanyi as fanyi
    req,stat = apilib.crapi('players',tag,'upcomingchests')
    if stat == True:
        user,clan=apilib.cr_user(tag)
        chest=(f'你好，{clan}{user}:\n下个宝箱：{req["items"][0]["name"]}')
        chest = fanyi.chest(chest)
        stat = 1
        for item in req ["items"]:
            if stat == 1:
                stat = stat+1
                pass
            else:
                chest=(chest+'\n')
                chest=(chest+f"宝箱+{item['index']}：{item['name']}" )
                chest= fanyi.chest(chest)
        return chest
    elif stat == False:
        return req
        #print('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')
    else:
        return('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')
#毫无作用的初始化代码
async def bdk(qid,idh,yyk):
    import pymysql
    conn = pymysql.connect(**yyk)
    cursor = conn.cursor()
    e=cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid} and `id` = {idh}")
    if e >0:
        lists = cursor.fetchall()
        return lists[0][4]
    else:
        return None
#部落战查询代码
async def cr_blzgl(bl):
    if bl=='dbl':
        tag='88GUJ80'
    else:
        return('我似乎不太理解你想查询那个部落'),False
    import lib.cr.apilib as apilib
    req,stat = apilib.crapi('clans',tag,menu2='currentriverrace')
    req2,stat2 = apilib.crapi('clans',tag,menu2='riverracelog')
    if stat == True:
        if stat2==True:
            import datetime
            now = datetime.datetime.utcnow()
            zbr_s=datetime.datetime.strptime(req2['items'][0]["createdDate"], "%Y%m%dT%H%M%S.%fZ")
            zbr_e=zbr_s+datetime.timedelta(days=3)
            #战斗日判定 
            if now<zbr_e:
                zbr=zbr_e-now
                wb=f'今日是准备日第{zbr.days+1}天,'
                zbr=True
            elif now>zbr_e: 
                zbr=now-zbr_e
                wb=f'今日是战斗日第{zbr.days+1}天,'
                zdr=False
            else:
                wb=''
                zbr=None
        elif stat2==False:
            wb=''
            zbr=None
        if zbr==False:
            cs = 0
            req = sorted(req['clans'],key = lambda e:e.__getitem__('fame'),reverse = True)
            rt='部落战概览:'
            rt=rt+f'\n{wb}部落战况：'
            for item in req:
                cs = cs+1
                rt=rt+f'\n{cs}."{item["name"]}":识别码:"{item["tag"]}",前进：{item["fame"]}米'
            return rt
        elif zbr==True:
            cs = 0
            req = sorted(req['clans'],key = lambda e:e.__getitem__('clanScore'),reverse = True)
            rt='部落战概览:'
            rt=rt+f'\n{wb}实力分析如下:'
            for item in req:
                cs = cs+1
                rt=rt+f'\n{cs}.{item["name"]}:"{item["tag"]}"部落奖杯:{item["clanScore"]}'
            rt=rt+'\n如需查询对方部落实力请使用部落查询小程序owo'
            return rt
    elif stat == False:
        return('小管家无法与CR服务器联络，请重新尝试一下吧owo')
    else:
        return(req)