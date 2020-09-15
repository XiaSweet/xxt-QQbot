import subprocess
from debuglib import xxt_crapi_log
async def get_nextchest_of_tag(tag: str) -> str:
    chest = subprocess.getoutput("python lib/clashroyale/chests.py -u '%s'"%(tag))
    tc = xxt_crapi_log('[宝箱查询]',chest)
    if tc == False:
        return chest
    else:
        return tc