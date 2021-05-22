#Nonebot2基础模块
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.typing import T_State
yhbd = on_keyword("绑定账号", rule=to_me(), priority=5,block=True)
@yhbd.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.message).strip()  # 原始信息
    if args:    # 过滤可用信息
        import re
        try:
            tag=re.search('[A-Za-z0-9]+',args).group()
        except AttributeError:
            await cr_cbx.reject('您的TAG似乎不对，再试试吧',at_sender=True)
        else: 
            import pymysql
            from .synclib import yyk
            conn = pymysql.connect(**yyk)
            cursor = conn.cursor()
            lists=cursor.execute(f'SELECT * FROM `xiasweet` WHERE `tag` = "{tag}" and `qid`={event.user_id}')
            if lists == 0:
                state["tag"]=tag.upper()
                state["qid"]=event.user_id
            else:
                lists = cursor.fetchall()
                if lists[0][3]=='bs':
                    gname='荒野乱斗'
                elif lists[0][3]=='cr':
                    gname='皇室战争'
                await yhbd.finish(f'你已在小管家这里登记这个TAG哦，重新绑定请联系部落首领@Ver.冬瓜萌萌！\n\
TAG绑定信息：{gname}@{lists[0][5]}')
    else:
        await yhbd.finish('或许你的账户实力婉如天上的星星令人难以分清，请根据使用指引修改的你命令参数QAQ\n\
使用指引：用户绑定+你的游戏TAG，不需要备注游戏我会自动识别')
#登记用户信息
@yhbd.got("tag", prompt="告诉我你想绑定的TAG号，不区分荒野和皇室哦")
async def handle_msg(bot: Bot, event: Event, state: T_State):
    import pymysql
    #获取变量
    tag=state["tag"]
    qid=state["qid"]
    from lib.clashroyale import apilib as crapi
    gname,clans=crapi.cr_user(tag)
    if gname != None:
        game='cr'
    else:
        from xxt.plugins.huangye.lib import chaxun as bsapi
        stat,info=bsapi.req_bs(tag)
        if stat == True:
            game='bs'
            yh=info['player_info']
            gname=yh['name']
        else:
            await yhbd.finish('你的游戏TAG在支持游戏数据库内均无法搜索到，请检查后再试')
    import xxt.plugins.user_info.synclib as sc
    sc.cg(qid,game,tag,gname)
    conn = pymysql.connect(**sc.yyk)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid} ")
    lists = cursor.fetchall()
    cr=sc.jc(lists,'cr')
    bs=sc.jc(lists,'bs')
    if cr == True or bs == True:
        jg=('操作成功owo，以下是你目前绑定/关注的账户\n')
        if cr==True:
            jg=(jg+'皇室战争：')
            for data in lists:
                if data[1]==qid and data[3]=='cr':
                    jg=(jg+'\n')
                    jg=(jg+f'{data[2]}.{data[5]}#{data[4]}'
                    )
        if bs == True:
            if cr==True:
                jg=(jg+'\n')
            jg=(jg+'荒野乱斗：')
            for data in lists:
                if data[1]==qid and data[3]=='bs':
                    jg=(jg+'\n')
                    jg=(jg+f'{data[2]}.{data[5]}#{data[4]}'
                    )
        conn.commit()
        conn.close()
        await yhbd.finish(jg)
    else:
        await yhbd.finish('出现了一些无法解决的小错误，账户绑定失败，请稍后再试qaq')