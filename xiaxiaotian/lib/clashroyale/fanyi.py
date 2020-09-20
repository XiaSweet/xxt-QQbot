#小管家的API中文化翻译模块
def clans(req):
    req = req.replace('inviteOnly','需批准')
    req = req.replace('closed','不可进入')
    req = req.replace('open','自由进入')
    return req
def chest(ce):
    ce = ce.replace('Silver Chest','普通银箱')
    ce = ce.replace('Magical Chest','魔法紫箱')
    ce = ce.replace('Golden Chest','黄金宝箱')
    ce = ce.replace('Giant Chest','巨型宝箱')
    ce = ce.replace('Mega Lightning Chest','国王闪电宝箱%s'%(lucky(ce)))
    ce = ce.replace('Legendary Chest','传奇宝箱')
    ce = ce.replace('Epic Chest','史诗宝箱%s'%(lucky(ce)))
    ce = ce.replace('+0','下个宝箱')
    return ce
#宝箱幸运值
def lucky(ce):
    import re
    try:
        lck_po = re.search('\+[0-9]*',ce).group()
    except AttributeError:
        return ''
    else:
        lck_po = lck_po.replace('+','')
        lck_po = int(lck_po)
        if lck_po < 100:
            return '(有点距离了)'
        elif lck_po < 300:
            return '(还早呢QAq)'
        elif lck_po < 50:
            return '(加油，不远了owo)'
        elif lck_po < 30:
            return '(提前恭喜啦(。・∀・)ノ)'
        return ''
#竞技场段翻译
def aruna(user):
    user = user.replace('Ultimate Champion','终极冠军联赛')
    user = user.replace('Royal Champion','皇室冠军联赛')
    user = user.replace('Grand Champion','超级冠军联赛')
    user = user.replace('Champion','冠军联赛')
    user = user.replace('Master','大师联赛')
    user = user.replace('Legendary','普通联赛')
    user = user.replace('Challenger''挑战者联赛')
    user = user.replace('Arena','普通竞技场')
    return user
#部落职位翻译
def cl_zw(clan):
    clan = clan.replace('coLeader','副首领')
    clan = clan.replace('leader','首领')
    clan = clan.replace('member','成员')
    clan = clan.replace('elder','长老')
    return clan
#罗马数字翻译
def gr_dj(req):
    req = req.replace('V','5级')
    req = req.replace('IV','4级')
    req = req.replace('III','3级')
    req = req.replace('II','2级')
    req = req.replace('I','1级')
    return req