from cloud_chat import txNLP
#腾讯云NLP变成账户id，智能闲聊需授权NLP权限
TXCloud_id = "AKIDDDySgiTw95k8F6gz0mHVS9ZibFdka8A1"
TXCloud_key = "cz7zby6zWqujIbeS0IK6dvxjGYaMtAAu"
#wenti=input('你向如何和夏小甜交流？\n请输入：')
wenti='alice'
try:
    daan=await txNLP.chat(wenti,TXCloud_id,TXCloud_key)
except:
    print(daan)
else:
    #daan=json.loads(daan)
    #daan=daan['Reply']+f'\n回答信心度：{daan["Confidence"]}'
    if daan['stat']==False:
        print(f'ERROR:{daan["code"]}\n出现错误了：{daan["msg"]}')
    elif daan['stat']==True:
        print(f'来自夏小甜的回复：{daan["reply"]}\n自信度{daan["Confidence"]}')
    else:
        print('其他的未知错误')