import pymysql
import asyncio
import xxt.config as xc
#sql初始化
def csh(args=xc.yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    cursor.execute("drop table if exists xiasweet")
    cursor.execute("create table xiasweet(qid bigint,id int,game varchar(20),tag varchar(20),name varchar(20),state int)")
#查询并写入用户
def cg(qid,gid,tag,gname,args=xc.yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid} ")
    lb = cursor.fetchall()
    z=1
    st=1
    for l in lb:
        if l[2] != None:
            z=z+1
        if l[2] == None:
            break
    cursor.execute(f"SELECT * FROM `xiasweet`")
    lb = cursor.fetchall()
    for l in lb:
        if l[0] != None:
            st=st+1
        if l[0] == None:
            break
    cursor.execute(f'INSERT INTO `xiasweet`  VALUES ({st},{qid},{z},"{gid}","{tag}","{gname}")')
    conn.commit()
    conn.close()
#游戏类型检测代码
def jc(data,gameid):
    for das in data:
        if das[3]==gameid:
            return True
    return False