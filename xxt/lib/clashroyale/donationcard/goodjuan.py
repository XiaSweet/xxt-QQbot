# -*- coding: utf-8 -*-
import sys
sys.path.append('lib/clashroyale/')
import argparse
import asyncio
#自有api
import apilib
#外部取值
parser = argparse.ArgumentParser(description='长老查询程序')
parser.add_argument('--tag', '-c', help='识别代码',default='dbl')
parser.add_argument('--one', '-o', help='个人模式输入tag用的',default=False)
args = parser.parse_args()
#这里是捐卡数单项统计
if args.one == False:
    a_person=False
else:
    user_tag=args.one
    a_person=True
#以下是正文
if args.tag == 'xbl':
    tag = "JY8YVC0"
    clanid = '小部落'
elif args.tag == 'dbl':
    tag = "88GUJ80"
    clanid = '大部落'
else:
    print ('ERROR-CRNotMyClans')
    exit()
#开始模块
if a_person == False:
    bs_ret,bs_stat = apilib.crapi('clans',tag,'members')
    if bs_stat == True:
        bs_ret = sorted(bs_ret['items'],key = lambda e:e.__getitem__('donations'),reverse = True)
        jk_mem,jk_stat = apilib.bl_upgrade_jk(bs_ret,juanka=200)
        if jk_stat == False:
            print('现在还没有符合条件的伙伴可以升职，请加油哦')
        else:
            print('以下是%s本周可以升职的长老:'%(clanid))
            for item in jk_mem:
                print(item)
    else:
            print('出现错误了,详细信息如下：%s'%(bs_ret))
elif a_person == True:
    user_name,user_clantag,clan_id=apilib.get_userclans(user_tag)
    if user_clantag == None:
        print('出现错误了：我们暂时无法确定您的职位情况，请稍后再尝试吧')
    elif user_clantag == 'Don,t_huangjia_clan':
        print('很抱歉，这项功能无法为茶话会部落以外的伙伴服务，敬请谅解')
    else:
        #开始现行异步查询部落贡献
        #本demo代码为小管家异步技术性测试代码owo
        #XiaSweet Labs 2020.10.3
        async def gongxian(clan,user):
            blz_sz,up_sum=apilib.get_user_blzgx(user,clan,blzgx=1233)
            if blz_sz == True:
                blz_sz = '是'
            else:
                blz_sz = '否'
            return blz_sz,up_sum
        async def juanka(user_clantag,user_tag):
            bl_ret,ret_stat=apilib.crapi('clans',user_clantag,menu2='members')
            if ret_stat == True:
                bl_jk,jk_sum=apilib.bl_upgrade_jk(bl_ret,juanka=450,tag=user_tag)
                return bl_jk,jk_sum
            else:
                return None,0
        async def main():
            blz_sz,blz_gx=await  gongxian(user_clantag,user_tag)
            jk_up,jk_sum=await  juanka(user_clantag,user_tag)
            return blz_sz,blz_gx,jk_up,jk_sum
        blz_sz,blz_gx,jk_up,jk_sum=asyncio.run(main())
        if jk_sum != None:
            print('感谢您的耐心等待owo，来自'+clan_id+'的'+user_name+'\n以下是小管家核对后的个人数据：')
            print('捐卡合格:%s '%(jk_up)+jk_sum)
            print('部落战贡献:%s'%(blz_sz)+blz_gx) 
            if jk_up== '是' or blz_sz== '是':
                print('恭喜你，你已经达成升职长老所需要的条件。\n小管家已知会首领了，最迟将在24小时内升职完毕，请您耐心等待哦owo')
            else:
                print('虽然不能升职，但是相比也不远了。请继续努力吧，加油')
        else:
            print('来自'+clan_id+'的'+user_name+'欢迎你:')
            print('目前小管家的功能还没有完善，所以部落目前除3天内在线外无降职要求\n你的职位是：%s，所以你并不需要使用这个功能-------@Ver.冬瓜萌萌'%(jk_up))
else:
         print('CRNotError')