#这个文件用于统一debug模式信息所使用
#基础组件
import logging
from nonebot.log import logger
#皇室战争
def xxt_crapi_log(plugin,jg):
    if jg == 'CRAPI-404':
        logger.debug(plugin+'查询完毕，官方无此TAG信息')
        logger.debug(plugin+'查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info(plugin+'任务处理完成')
        return('出现意外了：\n你想查询的用户被抓到二次元了，请检查一下再重新发送指令查询吧(⊙﹏⊙)')
    elif jg == 'CRAPI-400':
        logger.info(plugin+'出现错误了:官方API查询400,提示详见Debug模式')
        logger.info(plugin+'你可以前往CR开发者网站查询详情')
        logger.debug(plugin+'详细信息:没有使用正确的查询地址或官方关闭API了，或许也倒闭了吧( •̀ ω •́ )')
        logger.debug(plugin+'查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info(plugin+'任务处理完成')
        return('QAQ小管家迷路了，请联系管理员协助修复吧')
    elif jg == 'CRAPI-TimeOut':
        logger.info(plugin+'出现错误了:官方API查询超时,提示详见Debug模式')
        logger.debug(plugin+'详细信息：查询超时.详见小管家Wiki')
        logger.debug(plugin+'查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info(plugin+'任务处理完成')
        return('出现意外了：\n因为连接速度太慢所以主动放弃查询了，请您重新使用指令再查询一下吧')
    elif jg == 'CRAPI-NotSupportChinese':
        logger.info(plugin+'用户意外触发或未正常放弃，查询无效,提示详见Debug模式')
        logger.debug(plugin+'详细信息：包含英文数字以外的其他语言，查询无效.详见小管家Wiki')
        logger.debug(plugin+'查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info(plugin+'任务处理完成')
        return('对不起，你似乎不是来查询信息的(。﹏。)') 
    elif jg == 'ERROR-CRNotMyClans':
        logger.info(plugin+'用户并不在皇家部落内，拒绝查询并回复用户，提示详见Debug模式')
        logger.debug(plugin+'详细信息：用户并不在皇家部落内，主动放弃查询.详见小管家Wiki')
        logger.debug(plugin+'查询脚本执行完毕并返回信息到Nonebot脚本')
        logger.info(plugin+'任务处理完成')
        return('本服务仅对部落内的小伙伴所开放哦，Sorry。QAQ') 
    else:
        logger.info(plugin+'结果无错误并已查询完毕并发送给用户,任务结束')
        return False
 