import pymysql
import asyncio
import xxt.setting as xc
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
    for l in lb:
        if l[2] != None:
            z=z+1
        elif l[2] == None:
            break
    cursor.execute(f"SELECT * FROM `xiasweet`")
    lb = cursor.fetchall()
    st=1
    for l in lb:
        if l[0] == st:
            st=st+1
        elif l[0] != st:
            break
    try:
        cursor.execute(f'INSERT INTO `xiasweet`  VALUES ({st},{qid},{z},"{gid}","{tag}","{gname}")')
    except:
        conn.commit()
        conn.close()
        return('很抱歉，小管家暂时无法记住你的账号，请稍后再试')
        #return(f'源代码：{lb}\n错误提示：{st},{qid},{z},"{gid}","{tag}","{gname}"') #Debug代码，实际运行应去除
    else:
        conn.commit()
        conn.close()
        return True
#游戏类型检测代码
def jc(data,gameid):
    for das in data:
        if das[3]==gameid:
            return True
    return False