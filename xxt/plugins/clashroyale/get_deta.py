async def cbx(tag: str,rw):
    #外部函数引入
    import lib.clashroyale.apilib as apilib
    import lib.clashroyale.fanyi as fanyi
    req,stat = apilib.crapi('players',tag,'upcomingchests')
    if stat == True:
        user,clan=apilib.cr_user(tag)
        chest=(f'你好，来自{clan}的{user}:\n下个宝箱：{req["items"][0]["name"]}')
        chest = fanyi.chest(chest)
        stat = 1
        for item in req ["items"]:
            if stat == 1:
                stat = stat+1
                pass
            else:
                chest=(chest+'\n')
                chest=(chest+f"宝箱位置+{item['index']}：{item['name']}" )
                chest= fanyi.chest(chest)
        return chest
    elif stat == False:
        return req
        #print('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')
    else:
        return('出现无法解决的错误了，请联系管理员帮忙维护吧(⊙o⊙)')
async def bdk(qid,idh):
    import pymysql
    yyk = dict(
        host = 'localhost',
        user = 'xiasweet',
        passwd = 'asNhZFw7BYCcTksZ',
        db = 'xiasweet',
        charset = 'utf8'
    )
    conn = pymysql.connect(**yyk)
    cursor = conn.cursor()
    e=cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid} and `id` = {idh}")
    if e >0:
        lists = cursor.fetchall()
        return lists[0][4]
    else:
        return None