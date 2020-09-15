from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging
from nonebot.log import logger
import subprocess
from debuglib import xxt_crapi_log
from nonebot.helpers import render_expression as expr
import systemre as e
@on_command('blzgl', aliases=('部落战概览'),only_to_me=False)
async def blzgl(session: CommandSession):
    
    await session.send(expr(e.SYSTEM_WAITING))
    blzgl_report = await get_blzgl()
    await session.send(blzgl_report,at_sender=True)
    logger.info('[部落战概览]结果已反馈用户,任务结束')
async def get_blzgl() -> str:
    chest = subprocess.getoutput("python lib/clashroyale/clanwar/viewclan.py")
    tc = xxt_crapi_log('[部落战概览]',chest)
    if tc == False:
        return chest
    else:
        return tc