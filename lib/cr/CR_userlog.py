#针对部落皇室战争数据库的update更新
#本py文件采取了异步sync运行
#加载基础库
import asyncio
import sys
sys.path.append("/home/xxt-QQbot/lib/cr")
from CRapi_lib import datasql as sql
async def war(tag,cltag): #获取部落战有关信息
    from crapi import clans
    req=await clans.clanwar(tag,cltag)
    try:
        if req['stat']==True:
            return req
        elif req["stat"]==False:
            print('出现以外的错误了：',req['Debag'],f'\ntag:{tag},cltag:{cltag}')
            return req
        else:
            print('War未知错误')
    except Exception as e:
        print("部落战模块出现错误了，以下是调试信息：")
        print('tag：',tag,'cltag:',cltag,f'Debug:',e)
        return req
async def user(tag): #获取用户信息
    from crapi import players as crplayer
    re=await crplayer.get_info(tag)
    try:
        if re["stat"]==True:
            re["usertag"]=tag
            #开始写入数据库
        elif re["stat"]==False:
            print(re['Debag'])
        else:
            print('user未知错误')
    finally:
        return re
async def clan(tag,cltag): #根据成员tag获取部落信息
    from crapi import clans
    req=await clans.members(tag,cltag)
    try:
        if req['stat']==True:
            return req
        elif req["stat"]==False:
            print(re['Debag'])
        else:
            print('clan未知错误')
    except:
        print(req)
async def getmem_list(cltag): #获取成员列表
    from crapi import clans
    a=await clans.memlist(cltag)
    if a['stat']==True:
        return a['tag']
    elif a['stat']==False:
        return a['Debag']
    else:
        print(a)
        exit(0)
async def req_data(tag): #获取基础数据
    b=await user(tag)
    if "clantag" in b:
        clt=str(b["clantag"])
        clt=clt.replace('#','')
        #print(f'开始获取用户部落信息，查询用户和部落：{tag}@{clt}')
        a=await clan(tag,clt)
        b.update(a)
        try:
            a=b["donationsReceived"]/b["donations"]
            b["sjb"]=format(a,'.2f')
        except ZeroDivisionError:
            b["sjb"]='0.00'
        try:
            a=await war(tag,clt)
            if a['stat'] != False:
                b.update(a)
        except Exception as e:
            return b
    else: #针对无部落信息的反馈空白值
        b['lastlogin']='2014-01-01 00:00:00'
        b['clan']='外星同好会'
        b["clantag"]='None'
        b['fame']='0'
        b['clanRank']='0'
        b['repairPoints']='0'
        b['boatAttacks']='0'
        b['decksUsed']='0'
        b['decksUsedToday']='0'
        b["donationsReceived"]='0'
        b["donations"]='0'
        #except ZeroDivisionError:
        b["sjb"]='0.00'
    return b
#开始执行异步,封装自动刷新部落成员内数据
async def main():
    tasks = []
    a=await getmem_list('88GUJ80')
    #异步任务添加
    for i in a:
        tasks.append(req_data(i['tag']))
    a=await asyncio.gather(*tasks)
    #此处开始异步同步了,开始加载UTC计时组件
    tasks = []
    import datetime as dt
    try:
        for a in a:
            if a["stat"]==True:
                uputc=dt.datetime.utcnow()+dt.timedelta(hours=8)
                tasks.append((uputc,a["usertag"],a["name"],a["trophies"],
                a["clan"],a["clantag"],a["w/l"],a['lastlogin'],a["donations"],a["donationsReceived"],
                a['fame'],a['repairPoints'],a['decksUsed'],a['clanRank'],a["sjb"]))
                '''
                print(f'查询用户：{a["name"]},所在部落：{a["clan"]},部落Tag:{a["clantag"]},个人杯数：{a["trophies"]}',
                f'\n近期胜率：{a["w/l"]},最近捐卡：{a["donations"]},最近收卡：{a["donationsReceived"]}')
                '''
            else:
                pass
    except KeyError:
        task2=[]
        print(f'[ClashRoyaleAPI]部落战信息获取失败，本次将不会更新部落战内容\n@{a["name"]}#{a["usertag"]}')
        task2.append((uputc,a["usertag"],a["name"],a["trophies"],
                a["clan"],a["clantag"],a["w/l"],a['lastlogin'],a["donations"],a["donationsReceived"],a["sjb"]))
    #开始统计数据并写入
    try:
        sq=f"INSERT INTO `CR_userlog` (`UpdateTime`,`tag`, `name`, `trophies`, \
                    `clanname`,`clantag`,`Winlate`,`LASTlogin`,`Doation_Card`,`Req_Card`,`ClanGR`) \
                    VALUES (%s,%s,%s,%s,\
                    %s,%s,%s,%s,%s,%s,%s) \
                    ON DUPLICATE KEY UPDATE \
                    UpdateTime=values(UpdateTime) ,\
                    tag=values(tag) , \
                    name=values(name), \
                    trophies=values(trophies), \
                    clanname=values(clanname), \
                    clantag=values(clantag), \
                    Winlate=values(Winlate), \
                    LASTlogin=values(LASTlogin),\
                    Doation_Card=values(Doation_Card),\
                    Req_Card=values(Req_Card),\
                    ClanGR=values(ClanGR)"
                    
        await asyncio.gather(sql.batchInsert(sq,task2))
    except UnboundLocalError:
        print('[ClashRoyaleAPI]大家似乎都打部落战了呢，稍后将统计数据并更新owo')
        pass
    except Exception as e:
        print(e)
        print([task2])
    #解决兼容性问题单独无视的log
    sq =f"INSERT INTO `CR_userlog` (`UpdateTime`,`tag`, `name`, `trophies`, \
            `clanname`,`clantag`,`Winlate`,`LASTlogin`,`Doation_Card`,`Req_Card`,`ClanWar_contribute`,`ClanWar_Repair`,`ClanWar_DattleSum`,`clanRank`,`ClanGR`) \
            VALUES (%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s) \
            ON DUPLICATE KEY UPDATE \
            UpdateTime=values(UpdateTime) ,\
            tag=values(tag) , \
            name=values(name), \
            trophies=values(trophies), \
            clanname=values(clanname), \
            clantag=values(clantag), \
            Winlate=values(Winlate), \
            LASTlogin=values(LASTlogin),\
            Doation_Card=values(Doation_Card),\
            Req_Card=values(Req_Card),\
            ClanWar_contribute=values(ClanWar_contribute),\
            ClanWar_Repair=values(ClanWar_Repair),\
            ClanWar_DattleSum=values(ClanWar_DattleSum),\
            clanRank=values(clanRank), \
            ClanGR=values(ClanGR)"
    await asyncio.gather(sql.batchInsert(sq,tasks))
    print('[ClashRoyaleAPI]部落在册数据已更新完毕owo')
    from crapi import other
    a=await other.olddata()
    b=[]
    for a in a:
        for a in a:
            b.append(a[1])
    if b !=[]:
        print('[ClashRoyaleAPI]检测到其他部落成员，正在更新存量数据，请勿关闭计算机！')
        tasks = []
        #异步任务添加
        for i in b:
            tasks.append(req_data(i))
        a=await asyncio.gather(*tasks)
        tasks = []
        try:
            for a in a:
                uputc=dt.datetime.utcnow()+dt.timedelta(hours=8)
                tasks.append((uputc,a["usertag"],a["name"],a["trophies"],
                        a["clan"],a["clantag"],a["w/l"],a['lastlogin'],a["donations"],a["donationsReceived"]))
        #开始统计数据并写入
            sq=f"INSERT INTO `CR_userlog` (`UpdateTime`,`tag`, `name`, `trophies`, \
                        `clanname`,`clantag`,`Winlate`,`LASTlogin`,`Doation_Card`,`Req_Card`) \
                        VALUES (%s,%s,%s,%s,\
                        %s,%s,%s,%s,%s,%s) \
                        ON DUPLICATE KEY UPDATE \
                        UpdateTime=values(UpdateTime) ,\
                        tag=values(tag) , \
                        name=values(name), \
                        trophies=values(trophies), \
                        clanname=values(clanname), \
                        clantag=values(clantag), \
                        Winlate=values(Winlate), \
                        LASTlogin=values(LASTlogin),\
                        Doation_Card=values(Doation_Card),\
                        Req_Card=values(Req_Card)"
            await asyncio.gather(sql.batchInsert(sq,tasks))
        except UnboundLocalError:
            pass
        except Exception as e:
            print(e)
            print(a)
        print('[ClashRoyaleAPI]部落数据全部更新完毕owo')