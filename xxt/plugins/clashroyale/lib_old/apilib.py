# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import json
import ssl
#皇室战争API基础应用库
#CR 基础API模块
def crapi(menu,tag,menu2='',stat=0):
    cr_key='lib/mykey.txt'
    with open(cr_key) as f:
        mykey=f.read().rstrip("\n")
        ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1/"
        #请求调取官方数据库
        request = urllib.request.Request(
                base_url+menu+"/%23"+tag+'/'+menu2,
                None,
                headers={"Authorization":"Bearer %s" % mykey})
        res,check = tryapi(request)
        if check == True:
            trys = json.loads(res)
            return trys,True
        else:
            if stat == 0:
                return res,False
                #return '小管家多次尝试均无法连接，请稍后再试试吧(⊙o⊙)',False
            else:
                stat=stat+1
                crapi(menu,tag,menu2='',stat=stat)
# API检查模块
def tryapi(req):
    try:
        ty = urllib.request.urlopen(req,timeout=8).read().decode("utf-8")
    #HTTP错误
    except urllib.error.HTTPError as e:
        return 'CRAPI-%s'%(e.code),False
    except urllib.error.URLError as e:
        return "URLError-%s"%(e),False
    except TypeError:
        return "出现了异常错误，请稍后再试或耐心等待部落管理员更新QaQ",False
    #异常反馈
    except Exception as e:
        return "CRAPI-Error:%s"%(e),False
    #中文检查
    except UnicodeEncodeError:
        return "CRAPI-NotSupportChinese",False
    except TypeError:
        return "restart-search",False
    else:
        return ty,True
#用户信息获取模块
def cr_user(tag):
    info,stat=crapi('players',tag)
    if stat == True:
        if info["clan"]["tag"]=='#88GUJ80':
            info_bl='大部落'
        elif info["clan"]["tag"]=='#JY8YVC0':
            info_bl='小部落'
        else:
            info_bl='其他部落'
        return info["name"],info_bl
    else:
        return None,False
#皇家部落-长老捐卡审核
def bl_upgrade_jk(ret,juanka=450,tag=None):
    if tag == None:
        lis=[]
        jk_mem=0
        for item in ret:
            if item['donations'] > juanka and item['role'] == 'member':
                if item['donationsReceived'] < item['donations']:
                    jk_mem=jk_mem+1
                    lis.append ('用户：%s,周捐：%s'%(item['name'],item['donations']))
            else:
                pass
        if lis !=[]:
            return lis,True
        return lis,False
    else:
        for item in ret['items']:
            if item['tag']=='#'+tag:
                if item['donations'] > juanka and item['role'] == 'member':
                    if item['donationsReceived'] < item['donations']:
                        return '是','个人周捐:%s'%(item['donations'])
                    if item['donations']<item['donationsReceived']:
                        return '否','个人周捐:%s，收卡:%s'%(item['donations'],item['donationsReceived'])
                else:
                    import fanyi
                    role = fanyi.cl_zw(item['role'])
                    return role,None
            else:
                pass
        return False,None
#获取所在部落TAG
def get_userclans(tag):
    user_info,get_stat=crapi('players',tag)
    if get_stat == True:
        user_clantag=user_info['clan']['tag']
        if user_clantag == ('#JY8YVC0'):
            clantag=user_clantag.replace('#','')
            clanid='小部落'
            return user_info['name'],clantag,clanid
        if user_clantag == ('#88GUJ80'):
            clantag=user_clantag.replace('#','')
            clanid='大部落'
            return user_info['name'],clantag,clanid
        else:
            return user_info['name'],'Don,t_huangjia_clan',None
    else:
        return None,None,None
#部落战贡献查询
def  get_user_blzgx(usertag,clantag,blzgx=1233):
    req,req_stat = crapi('clans',clantag,menu2='currentriverrace')
    if req_stat == True:
        for item in req['clan']['participants']:
            if item['tag'] == '#'+usertag and get_user_clanrole(usertag,clantag)=='member':
                user_gx=item['fame']+item['repairPoints']
                user_up=blzgx-user_gx
                if user_up<0:
                    return True,' 本周贡献：%s'%(user_gx)
                else:
                    return False,' 你的贡献：%s'%(user_gx)
            else:
                pass
        return False,None
    else:
        return '出现以外了,暂时无法连接',0
#部落职位校对
def get_user_clanrole(usertag,clantag):
    reqs,req_stat=crapi('clans',clantag,menu2='members')
    if req_stat == True:
        for req in reqs['items']:
            if req['tag'] == '#'+usertag:
                return req['role']