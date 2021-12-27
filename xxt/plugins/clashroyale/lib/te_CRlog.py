#python兼容模块 3.10
import time
#Debug开始
start_time = time.time()  # 记录程序开始运行时间

#针对部落皇室战争数据库的update更新
#本py文件采取了异步sync运行
#加载基础库
import asyncio
import CR_userlog as cr
from CRapi_lib import datasql as sql
asyncio.run(cr.main())
end_time = time.time()  # 记录程序结束运行时间
print('温馨提示：更新日志整体操作用时 %f 秒' % (end_time - start_time))