from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging
from nonebot.log import logger
import subprocess
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("/home/xxt-QQbot/xiaxiaotian/lib/smartxxt")
import systemre as e
@on_command('goodjuan', aliases=('部落升职'),only_to_me=True)
async def goodjuan(session: CommandSession):
    tag = session.get('tag')
    await session.send(expr(e.SYSTEM_WAITING))
    goodjuan_report = await get_goodjuan(tag)
    if goodjuan == 'ERROR-CR404':
        logger.info('[部落升职]查询完毕，官方无此TAG信息')
        logger.debug('[部落升职]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[部落升职]任务处理完成')
        await session.send('出现意外了：\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)',at_sender=True)
    elif goodjuan == 'ERROR-CR400':
        logger.info('[部落升职]出现错误了:官方API查询400,提示详见Debug模式')
        logger.info('[部落升职]你可以前往CR开发者网站查询详情')
        logger.debug('[部落升职]详细信息:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )')
        logger.debug('[部落升职]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[部落升职]任务处理完成')
        await session.send('QAQ小管家迷路了，请联系管理员协助修复吧',at_sender=True)
    elif goodjuan == 'ERROR-CRTimeOut':
        logger.info('[部落升职]出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug('[部落升职]详细信息：查询超时.详见小管家Wiki')
        logger.debug('[部落升职]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[部落升职]任务处理完成')
        await session.send('出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧',at_sender=True)
    elif goodjuan == 'ERROR-CRNotCallMe':
        logger.info('[部落升职]用户意外触发或未正常放弃，查询无效,提示详见Debug模式')
        logger.debug('[部落升职]详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug('[部落升职]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[部落升职]任务处理完成')
        await session.send('对不起，你似乎不是来查询信息的(。﹏。)',at_sender=True) 
    elif goodjuan == 'ERROR-CRNotError':
        logger.info('[部落升职]用户并不在皇家部落内，拒绝查询并回复用户，提示详见Debug模式')
        logger.debug('[部落升职]详细信息：用户并不在皇家部落内，主动放弃查询.详见小管家Wiki')
        logger.debug('[部落升职]查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info('[部落升职]任务处理完成')
        await session.send('本周暂无捐卡达标的小伙伴，请继续加油(⊙o⊙)哦',at_sender=True) 
        #await session.send('本服务仅对部落内的小伙伴所开放哦，Sorry。QAQ',at_sender=True) 
    else:
        await session.send(goodjuan_report,at_sender=True)
        logger.info('[部落升职]结果无错误并已查询完毕并发送给用户,任务结束')
async def get_goodjuan(tag: str) -> str:
    goodjuan = subprocess.getoutput("python3 lib/clashroyale/donationcard/goodjuan.py -c '%s'"%(tag))
    return f'{goodjuan}'
    #return f'0捐测试功能触发完毕'
@goodjuan.args_parser
async def _(session: CommandSession):
    logger.debug('[部落升职]开始过滤无效字符')
    s = session.current_arg_text
    logger.debug('[部落升职]开始辨别部落代码') 
    if s.find('升') > -1:
            logger.info('[部落升职]用户查询部落可升职长老，作为参数传入并执行查询脚本')
            session.state['tag'] = 'szl'
    elif s.find('降') > -1:
            logger.info('[部落升职]用户查询部落应降职管理，作为参数传入并执行查询脚本') 
            session.state['tag'] = 'dbljiangji'
    elif s.find(f'捐卡' and '信息') or s.find(f'捐卡' and '查询') > -1:
            logger.info('[部落升职]用户查询部落捐卡信息，作为参数传入并执行查询脚本') 
            session.state['tag'] = 'juankaapi'    
    elif not session.is_first_run:
                if s.find(f'嗯' or f'是' or f'继续' or f'还不' or '可以' or f'需要' or f'好') > -1:
                    logger.debug('[部落升职]用户希望继续查询，重置指令')
                    session.pause('请告诉我你的想法，我再帮你查查看吧')                    
                else:
                    logger.info('[部落升职]用户放弃查询，取消指令')
                    session.finish('你还是想好再来找我吧(⊙ω⊙)') 
    else:
            logger.debug('[部落升职]用户二次查询无结果，征求用户意见')
            logger.debug('[部落升职]一次查找无结果，重新查询中')
            session.pause('木有理解你的意思，需要重新查询吗？\n您可以查询：部落本周职位公示（升职、降职）、本周捐卡信息')
@on_natural_language(keywords={'升职',('升'and'长老'),'降职',('不作为' and '伙伴'),'捐卡查询', '捐卡信息'},only_to_me=True)
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.replace(' ','')
    stripped_msg = session.msg_text.replace('#','')
    return IntentCommand(81, 'goodjuan',current_arg=stripped_msg)