import pymysql
import asyncio
yyk = dict(
        host = 'localhost',
        user = 'xiasweet',
        passwd = 'asNhZFw7BYCcTksZ',
        db = 'xiasweet',
        charset = 'utf8'
)
#sql初始化
def csh(args=yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    cursor.execute("drop table if exists xiasweet")
    cursor.execute("create table xiasweet(qid bigint,id int,game varchar(20),tag varchar(20),name varchar(20),state int)")
#查询并写入用户
def cg(qid,gid,tag,gname,args=yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid} ")
    lb = cursor.fetchall()
    z=1
    st=1
    for l in lb:
        if l[1] != None:
            z=z+1
        if l[1] == None:
            break
    for l in lb:
        if l[5] != None:
            st=st+1
        if l[5] == None:
            break
    cursor.execute(f'INSERT INTO `xiasweet`  VALUES ({qid},{z},"{gid}","{tag}","{gname}",{st})')
    conn.commit()
    conn.close()
#游戏类型检测代码
def jc(data,gameid):
    for das in data:
        if das[2]==gameid:
            return True
    return False
#专用测试代码
def cx(args=yyk):
    return None