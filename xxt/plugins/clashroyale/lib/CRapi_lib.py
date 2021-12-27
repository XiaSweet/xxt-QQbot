#python兼容模块 3.10
#开始加载基础应用库
import aiohttp
import asyncio
import json
import aiomysql
from xxt.setting import yyk
#CR 基础API调取模块
async def crlib(menu,tag,menu2='',stat=0):
    cr_key='mykey.txt'
    with open(cr_key) as f:
        mykey=f.read().rstrip("\n")
        #ssl._create_default_https_context = ssl._create_unverified_context
        base_url = "https://api.clashroyale.com/v1/"+menu+"/%23"+tag+'/'+menu2
        #请求调取官方数据库
        async with aiohttp.ClientSession() as session:
            res={}
            try:
                req=await session.get(base_url,timeout=10,headers={"Authorization":f"Bearer {mykey}" })
                if req.status==200:
                    res = await req.read()
                    res = json.loads(res)
                    res['CRapi_Stat']=True
                    res['CRapi_Debag']='Req OK Not Bug OwO'
                elif req.status==404:
                    res['CRapi_Stat']=False
                    res['CRapi_Debag']=f'很抱歉，您提供的结果在系统内无记录(HTTP{req.status})'
                elif req.status==403:
                    res['CRapi_Stat']=False
                    res['CRapi_Debag']=f'小管家IP未经过API授权认证，无法查询(HTTP{req.status})'
                else:
                    res = await req.read()
                    res = json.loads(res)
                    res['CRapi_Stat']=False
                    if res["reason"]:
                        res["reason"]=f'\nAPI服务提示：{res["reason"]}'
                    res['CRapi_Debag']=f'与API联机时出现了HTTP{req.status}错误{res["reason"]}'
                    #raise ClashRoyaleAPIError(f'出现错误了：与API联机时出现了HTTP{req.status}错误\n错误原因：{res["reason"]}')
            except asyncio.TimeoutError:
                res['CRapi_Stat']=False
                res['CRapi_Debag']=f'API联机时超预期时间，可能是网络波动所致'
                #raise KnowError(req)
            except:
                res['CRapi_Stat']=False
                res['CRapi_Debag']=f'与API联机以外出现了错误:{e}'
            return res
#SQL异步模块
class datasql():
    async def batchInsert(sql, values,yyd=yyk):
        async def getCurosr(pool):
            '''
            获取db连接和cursor对象，用于db的读写操作
            :param pool:
            :return:
            '''
            conn = await pool.acquire()
            cur = await conn.cursor()
            return conn, cur
        '''
        初始化，获取数据库连接池
        :return:
        '''
        try:
            #print("[ClashRoyaleAPI]正在尝试链接数据库")
            pool = await aiomysql.create_pool(**yyd)
            #print(f"[ClashRoyaleAPI]数据库链接成功：欢迎你，亲爱的“{yyk['user']}@{yyk['host']}”")
            print('[ClashRoyaleAPI]数据统计完成，正在写入数据库中，请勿随意关闭电脑！')
        except asyncio.CancelledError:
            raise asyncio.CancelledError
        except Exception as ex:
            print("mysql数据库连接失败：{}".format(ex.args[0]))
            return False
        # 第一步获取连接和cursor对象
        conn, cur = await getCurosr(pool)
        try:
            # 执行sql命令
            await cur.executemany(sql, values)
            await conn.commit()
            # 返回sql执行后影响的行数
            return cur.rowcount
        finally:
            # 最后不能忘记释放掉连接，否则最终关闭连接池会有问题
            await pool.release(conn)
            print("[ClashRoyaleAPI]数据保存成功，执行sql命令后影响的行数: ", cur.rowcount)
            #print('[ClashRoyaleAPI]数据库链接已主动断开')
    async def query(sql,yyd=yyk):
        '''
        查询, 一般流程是首先获取连接，光标，获取数据之后，则需要释放连接
        :param pool:
        :return:
        '''
        async def getCurosr(pool):
            conn = await pool.acquire()
            cur = await conn.cursor()
            return conn, cur
        '''
        初始化，获取数据库连接池
        :return:
        '''
        try:
            #print("[ClashRoyaleAPI]正在尝试链接数据库")
            pool = await aiomysql.create_pool(**yyd)
            #print(f"[ClashRoyaleAPI]数据库链接成功：欢迎你，亲爱的“{yyk['user']}@{yyk['host']}”")
        except asyncio.CancelledError:
            raise asyncio.CancelledError
        except Exception as ex:
            print("mysql数据库连接失败：{}".format(ex.args[0]))
            return False
        # 第一步获取连接和cursor对象
        conn, cur = await getCurosr(pool)
        try:
            await cur.execute(sql)
            return await cur.fetchall()
        finally:
            await pool.release(conn)