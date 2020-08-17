from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import subprocess
import logging
from nonebot.log import logger
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("/home/xxt-QQbot/xiaxiaotian/lib/smartxxt")
import systemre as e
@on_command('findfrind',aliases=('部落找队友'),only_to_me=True)
async def findfrind(session: CommandSession):
    logger.info('[皇室找队友]用户激活指令开始运行')
    await session.send(expr(e.SYSTEM_WAITING))
    logger.debug('[皇室找队友]向编译库发送请求获取信息')
    findfrind_report = await get_findfrind_of_chat()
    logger.info('[皇室找队友]向用户发送运行结果，任务结束')
    await session.send(findfrind_report,at_sender=True)
async def get_findfrind_of_chat() -> str:
    onechat = subprocess.getoutput("python lib/clashroyale/findfrind.py")
    return f'{onechat}'
@on_natural_language(keywords={'部落找队友','找队友'})
async def _(session: NLPSession):
    return IntentCommand(88.0, 'findfrind')