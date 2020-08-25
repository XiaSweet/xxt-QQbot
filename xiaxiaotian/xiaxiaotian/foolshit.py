from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import subprocess
import logging
from nonebot.log import logger
from nonebot.helpers import render_expression as expr
import sys
sys.path.append("/home/xxt-QQbot/xiaxiaotian/lib/smartxxt")
import systemre as e
@on_command('foolshit',aliases=('部落木头人'),only_to_me=True)
async def foolshit(session: CommandSession):
    logger.info('[皇室找队友]用户激活指令开始运行')
    await session.send(expr(e.SYSTEM_WAITING))
    logger.debug('[皇室找队友]向编译库发送请求获取信息')
    foolshit_report = await get_foolshit_of_chat()
    logger.info('[皇室找队友]向用户发送运行结果，任务结束')
    await session.send(foolshit_report,at_sender=True)
async def get_foolshit_of_chat() -> str:
    onechat = subprocess.getoutput("python lib/clashroyale/peoplemmc/foolshit.py")
    return f'{onechat}'
@on_natural_language(keywords={'木头人','部落'})
async def _(session: NLPSession):
    return IntentCommand(70.0, 'foolshit')