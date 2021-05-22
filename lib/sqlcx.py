import pymysql
import asyncio
yyk = dict(
        host = 'localhost',
        user = 'xiasweet',
        passwd = 'asNhZFw7BYCcTksZ',
        db = 'xiasweet',
        charset = 'utf8'
)
#调取查询时使用
def cx(qid,args=yyk):
    #游戏类型检测代码
    def jc(data):
        c=0
        while c > 1:
            return True,2
        if c == 1:
            return True,1
        else:
            return False,0
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid}  and `game` = 'cr'")
    lb = cursor.fetchall()
    conn.commit()
    conn.close()
    cr,stat=jc(lb)
    if cr==True and stat==1:
        return lb[0][4],True
    elif cr==True and stat==2:
        jg=('请二次确认你需要查询的ID号@机器人发送\n')
        jg=(jg+'皇室战争：')
        for data in lb:
            if data[1]==qid and data[3]=='cr':
                jg=(jg+'\n')
                jg=(jg+f'{data[2]}.{data[5]}#{data[4]}'
                )
        return jg,'Wait'
    else:
        return '404',False