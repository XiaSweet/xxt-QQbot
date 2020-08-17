import datetime
origin_date_str= "20200817T145032.000Z"
utc_date = datetime.datetime.strptime(origin_date_str, "%Y%m%dT%H%M%S.%fZ")
local_date = utc_date + datetime.timedelta(hours=8)
local_date_str = datetime.datetime.strftime(local_date ,'%Y-%m-%d %H:%M:%S')
print("外部时间：%s"%(local_date_str) )    # 2019-07-26 16:20:54
now = datetime.datetime.utcnow()
now_str = datetime.datetime.strftime(now ,'%Y-%m-%d %H:%M:%S')
print("本机时间：%s"%(now_str))
if now - utc_date <= datetime.timedelta(minutes=30):
    print("30分钟前")
else:
    print("Fuck")