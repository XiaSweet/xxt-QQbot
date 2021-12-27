# -*- coding: utf-8 -*-
#开始加载基础应用库
from .CRapi_lib import crlib
#APIlib模块用于为皇室战争类基础调取提供运行基础与错误排查
class ClashRoyaleAPIError(Exception):
    pass
class KnowError(Exception):
    pass
#皇室战争API基础应用库
#本应用库为异步优化版本，进行了部分精简化的代码
#秘密基地实验室，2021年末
#错误代码与初始化
#部落代码类
class clans:
    async def memlist(cltag):
        try:
            re={}
            tag=[]
            req=await crlib('clans',cltag,menu2='members')
            if req['CRapi_Stat']==True:
                re['stat']=True
                for req in req['items']:
                    a=req['tag'].replace('#','')
                    tag.append({'tag':a})
                re['tag']=tag
                return re
            else:
                raise ClashRoyaleAPIError(re['CRapi_Debag'])
        except ClashRoyaleAPIError:
            re['stat']=False
            re['Debag']='CRapi-memlist出现错误了:'+info['CRapi_Debag']
            return re
        finally:
            return re
    #尝试get相关部落信息
    async def members(user,tag,info=None):
        try:
            if info==None:
                re={}
                req=await crlib('clans',tag,menu2='members')
            if req['CRapi_Stat']==True:
                re['stat']=True
                tag='#'+user
                import datetime as dt
                for req in req['items']:
                    if req['tag']==tag: #次数返回的都是API可以用到的信息
                        re['role']=req['role']
                        re['expLevel']=req['expLevel']
                        re['donations']=req['donations']
                        re['donationsReceived']=req['donationsReceived']
                        re['clanRank']=req['clanRank']
                        req['lastSeen']=dt.datetime.strptime(req["lastSeen"], "%Y%m%dT%H%M%S.%fZ") #转换时间差
                        req['lastSeen']=req['lastSeen']+dt.timedelta(hours=8)
                        re['lastlogin'] = dt.datetime.strftime(req['lastSeen'] ,'%Y-%m-%d %H:%M:%S')
                        re['previousClanRank']=req['previousClanRank']
                        break
                    else:
                        pass
            else:
                raise ClashRoyaleAPIError(re['CRapi_Debag'])
        except ClashRoyaleAPIError:
            re["stat"]=False
            re['Debag']='CRapi出现错误了:'+info['CRapi_Debag']
            return re
        finally:
            return re
    #获取部落战信息,针对个人
    async def clanwar(user,tag,info=None):
        try:
            if info==None:
                re={}
                req=await crlib('clans',tag,menu2='currentriverrace')
            if req['CRapi_Stat']==True:
                re['stat']=True
                tag='#'+user
                for req in req['clan']['participants']:
                    if req['tag']==tag:
                        re['fame']=req['fame']
                        re['repairPoints']=req['repairPoints']
                        re['boatAttacks']=req['boatAttacks']
                        re['decksUsed']=req['decksUsed']
                        re['decksUsedToday']=req['decksUsedToday']
                        return re
                    else:
                        pass
                re['stat']=False
        except ClashRoyaleAPIError:
            re["stat"]=False
            re['Debag']='CRapi出现错误了:'+info['CRapi_Debag']
            return re
        finally:
            return re
#用户信息类
class players:
    #用户info类获取，返回值对应API：APIurl/players/{playerTag} 
    async def get_info(tag,info=None):
        try:
            if info==None:
                re={}
                info=await crlib('players',tag)
            if info['CRapi_Stat']==True:
                #部落检测
                if 'clan' in info:
                    if info["clan"]["tag"]=='#88GUJ80': 
                        re["clantag"]=info["clan"]["tag"]
                        re["clan"]='大部落'
                    elif info["clan"]["tag"]=='#JY8YVC0':
                        re["clantag"]=info["clan"]["tag"]
                        re["clan"]='小部落'
                    else:
                        re["clantag"]=info["clan"]["tag"]
                        re["clan"]=info["clan"]["name"]
                re["stat"]=True
                re["name"]=info["name"]
                re["trophies"]=info['trophies']
                #计算胜率
                re["wins"]=info["wins"]
                re["losses"]=info["losses"]
                wl=re["wins"]+re["losses"]
                wl=re["wins"]/wl
                re["w/l"]=format(wl,'.2f')
                re["usertag"]=str(tag)
                return re
            else:
                raise ClashRoyaleAPIError(info['CRapi_Debag'])
        except ClashRoyaleAPIError:
            if info['CRapi_Debag']:
                re["stat"]=False
                re['Debag']='CRapi出现错误了:'+info['CRapi_Debag']
                return re
        except Exception as e:
            re['stat']=False
            if info['CRapi_Debag']:
                re['Debag']='CRapi出现错误了:'+info['CRapi_Debag']+str(e)
            else:
                re['Debag']=str('用户信息获取错误：\n',re)
            return re
class other:
    #获取存量未更新数据
    async def olddata():
        import asyncio
        import datetime as dt
        from CRapi_lib import datasql as sql
        uputc=dt.datetime.utcnow()+dt.timedelta(hours=7)
        sq=f"SELECT * FROM `CR_userlog` WHERE `UpdateTime` < '{uputc}' ORDER BY `UpdateTime` ASC "
        a=await asyncio.gather(sql.query(sq))
        return a
#勿开启错误提醒
#print('出现错误了：CRapi实用应用程序缺失依赖，无法单独运行；请使用夏小甜机器人调度功能')
#print('秘密基地同好会：2021-12 by XiaSweet')
#exit(0)