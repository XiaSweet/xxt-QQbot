import subprocess
async def cr_cbx(tag: str):
    req = subprocess.getoutput("python xxt/plugins/clashroyale/lib/chests.py -u '%s'"%(tag))
    return req
async def cr_xyh(tag: str):
    req = subprocess.getoutput("python xxt/plugins/clashroyale/lib/user.py -u '%s'"%(tag))
    return req
async def cr_zdy():
    req = subprocess.getoutput("python xxt/plugins/clashroyale/lib/findfrind.py")
    return req
async def cr_cwgl():
    req = subprocess.getoutput("python xxt/plugins/clashroyale/lib/viewclan.py")
    return req