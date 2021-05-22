import pymysql
import asyncio
from xxt.setting import yyk
#调取查询时使用
def cx(qid,args=yyk):
    #游戏类型检测代码
    def jc(c):
        if c >1:
            return True,2
        elif c == 1:
            return True,1
        else:
            return False,0
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    lb = cursor.execute(f"SELECT * FROM `xiasweet` WHERE `qid` = {qid}  and `game` = 'cr'")
    conn.commit()
    conn.close()
    cr,stat=jc(lb)
    if cr==True and stat==1:
        lb = cursor.fetchall()
        return lb[0][4],True
    elif cr==True and stat==2:
        lb = cursor.fetchall()
        jg=('请@你需要查询的ID号以继续查询\n')
        jg=(jg+'皇室战争：')
        for data in lb:
            if data[1]==qid and data[3]=='cr':
                jg=(jg+'\n')
                jg=(jg+f'@{data[2]}:{data[5]}'
                )
        return jg,'Wait'
    else:
        return '404',False