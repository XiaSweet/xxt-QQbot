import optparse
import time
import chatlib#夏小甜自有调取库
import json
import ssl
async def anso(chat,TXAI_APP_ID,TXAI_APP_KEY):
    str_question = chat
    session = 10000
    ai_obj = chatlib.AiPlat(TXAI_APP_ID,TXAI_APP_KEY)
    rsp = ai_obj.getNlpTextChat(session,str_question)
    if rsp['ret'] == 0:
        ask = (rsp['data'])['answer']
        chatre = (ask)
    else:
        if rsp['ret'] == 16394:
            chatre = ('')
        elif rsp['ret'] == 16453:
            chatre = ('')
        elif rsp['ret'] < 0:
            chatre = ('')
        elif rsp['ret'] == 16388:
            chatre = ('')
        elif rsp['ret'] == 4096:
            chatre = None
        else:
            chatre = (json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    return chatre