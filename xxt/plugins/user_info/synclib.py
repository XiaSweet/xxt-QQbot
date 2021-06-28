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
async def cg(qid,gid,tag,gname,clid,clan,args=xc.yyk):
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
        cursor.execute(f"INSERT INTO xiasweet  VALUES ({st},{qid},{z},'{gid}','{tag}','{gname}','{clid}','{clan}')")
    except:
        conn.close()
        return('很抱歉，小管家暂时无法记住你的账号，请稍后再试')
        #return(f'源数据库写入错误,代码提示：{st},{qid},{z},"{gid}","{tag}","{gname}","{clid}","{clan}"') #Debug代码，实际运行应去除
    else:
        conn.commit()
        bd=cursor.execute(f"SELECT * FROM `default_user` WHERE `qid` = {qid} ")
        def re_name(gn):
            if gn=='bs':
                return '荒野乱斗'
            elif gn=='cr':
                return '皇室战争'
        if bd==0:
            import xxt.setting as xs
            stat=duser(qid,gid,clan,gname,tag)
            gid=re_name(gid)
            if stat==True:
                conn.close()
                if xs.Debug==True:
                    return(f'Debug：{gname}@{gid}#{tag}\n本信息理论证明运行成功，且假定为用户设置了默认TAG并修改群昵称')
                return 1
            else:
                conn.close()
                if xs.Debug==True:
                    return(f'Debug：{st},{qid},{z},"{gid}","{tag}","{gname}","{clid}","{clan}"\n在实例环境中理论证明默认TAG未绑定,但账户绑定成功')
                return 2 #第二种错误，合并1情况绑定失败错误
        conn.close()
        return True
#游戏类型检测代码
def jc(data,gameid):
    for das in data:
        if das[3]==gameid:
            return True
    return False
#查询SQL:default_user 用于设置默认账户
#写入默认用户
def duser(qid,gname,clan,name,tag,args=xc.yyk):
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    try:
        lists=cursor.execute(f"SELECT * FROM `default_user` WHERE `qid` = {qid} ")
    except:
        conn.commit()
        conn.close()
        return False
    if lists == 0:
        try:
            lb=cursor.execute(f'INSERT INTO `default_user`  VALUES ({qid},"{gname}","{clan}","{name}","{tag}")')
        except:
            conn.close()
            return False
            #return(f'源代码：{lb}\n错误提示：{qid},"{gname}","{clan}","{name}","{tag}"') #Debug代码，实际运行应去除
        else:
            conn.commit()
            conn.close()
            return True
    else:
        try:
            cursor.execute(f"UPDATE `default_user` SET `gname`='{gname}',`clan`='{clan}',`name`='{name}',`tag`='{tag}' WHERE `default_user`.`qid`='{qid}'")
        except:
            conn.commit()
            conn.close()
            return False
        else:
            conn.commit()
            conn.close()
            return True