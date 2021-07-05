import pymysql
import asyncio
import xxt.setting as xc
#查询歌曲
#听歌数据库使用了Tingsong数据库
async def cg(hard=None,args=xc.yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    if hard==None:
        jg=cursor.execute(f"SELECT * FROM `TingSong`")
    else:
        jg=cursor.execute(f"SELECT * FROM `TingSong` WHERE `Hand` LIKE '{hard}'")
    import random
    jg=random.randint(0,jg)
    state['id']=jg
    jg=cursor.execute(f"SELECT * FROM `TingSong` WHERE `id`='{jg}'")
    lists = cursor.fetchall()
    state['downlink']=lists[0][3]
    state['singer']=lists[0][2]
    state['name']=lists[0][1]
    conn.close()