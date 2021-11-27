#lib插件：皇室战争基础API/翻译模块
import lib.cr.apilib as apilib
import lib.cr.fanyi as fanyi
tag = "88GUJ80"
#插件：生成部落捐卡排名（前五）
def bljk(tag):
    req,stat = apilib.crapi('clans',tag,'members')
    if stat == False:
        raise ClanDonationsError(req)
    else:
        re="\n目前本周的部落捐卡排名（前五）："
        req = sorted(req['items'],key = lambda e:e.__getitem__('donations'),reverse = True)
        a=0
        for item in req:
            a=a+1
            if a==6:
                break
            re=re+f"\n{item['name']}：捐卡{item['donations']}，收卡{item['donationsReceived']}"
        return re
#插件：部落战日报
def blz(tag):
    #插件：判定部落战进度
    def zdr(tag):
        req,stat = apilib.crapi('clans',tag,menu2='riverracelog')
        if stat==True:
            import datetime
            now = datetime.datetime.utcnow()
            zbr_s=datetime.datetime.strptime(req['items'][0]["createdDate"], "%Y%m%dT%H%M%S.%fZ")
            zbr_e=zbr_s+datetime.timedelta(days=3)
            #战斗日判定 
            if now<zbr_e:
                zbr=zbr_e-now
                re=f'今日是准备日第{zbr.days+1}天,'
                return re,False
            elif now>zbr_e: 
                zbr=now-zbr_e
                re=f'今日是战斗日第{zbr.days+1}天,'
                return re,True
            else:
                return '',None
        elif stat==False:
            print("出现错误了：无法查询战斗日")
            return '',None
    #根据部落战进度，可选生成贡献前五排名信息与部落战总体排名
    zdr,stat=zdr(tag)
    if stat==True:
        #获取部落战总体排名
        req,stat=apilib.crapi('clans',tag,menu2='currentriverrace')
        if stat == True:
            re="\n部落战日览："
            a=-1
            req = sorted(req['clans'],key = lambda e:e.__getitem__('fame'),reverse = True)
            for item in req:
                a=a+1
                if item['tag']==tag:
                    break
                if a>5:
                    stat=False
                    break
            if stat != False:
                re=re+zdr+f"大部落排名第{a}名。"
                print(f'log：大部落排名：{a}')
        req,stat=apilib.crapi('clans',tag,menu2='currentriverrace') 
        if stat == False:
            raise CRAPI.Error(f'很抱歉，出现了一点小问题，请留意下方错误日志：{req}')
        else:
            req = sorted(req['clan']['participants'],key = lambda e:e.__getitem__('fame'),reverse = True)
            a=0
            re=re+f"以下是目前部落战总体贡献度前五："
            for item in req:
                if a==5:
                    break
                re=re+f"\n成员：{item['name']}，部落战贡献:{item['fame']}"
                a=a+1
            re=re+"\n没有上榜的伙伴不要灰心，多多挂机增加贡献相信下一个上榜的就是你哦"
            return re
    elif stat==False:
        re=re+"请不要忘记每周四下午的部落战战斗日(⊙o⊙)哦，挂机也可。多多刷贡献，为部落战丰厚的奖励努力吧\n"
        return re
#获取今日时间
import time
re=f"部落战营运概览owo({time.strftime('%Y/%m/%d', time.localtime())})：\n\n"
#lib插件：获取每日一言
import lib.yiyan as yiyan
try:
    req=yiyan.yiyan()
    re=re+f"每日一言：\n{req['hitokoto']}@{req['from']}\n"
    jk=bljk(tag)
    blz=blz(tag)
    re=re+jk+blz
finally:
    #部落日报栏PS声明
    re=re+"\nPS：\n(1)本日公告栏由人工智障夏小甜自动填写，如有疑问请私信@Ver.冬瓜萌萌，具体通知事项请以部落公告版为准\n(2)数据来源：RoyaleAPI官方数据\n@皇家.部落--------秘密基地CR自动化运营部；2021版权所有"
    print(re)


# 获取部落战详细数值 Demo，此处代码已结束 
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