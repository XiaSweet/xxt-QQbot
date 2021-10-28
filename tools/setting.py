print('\033[0m[夏小甜管家Setup]正在设置QQ机器人账户......\033[0m')
import yaml
import argparse
parser = argparse.ArgumentParser(description='CQHTTP设置程序')
parser.add_argument('--qqid','-qi',default='3304871685',help='QQ账户，在Docker中应是QID变量')
parser.add_argument('--qqpasswd','-qp',default=False,help='QQ密码，在Docker中应是QPWD变量')
arg = parser.parse_args()
with open('config.yml','r',encoding='utf-8')as f:
    result=yaml.load(f.read(),Loader=yaml.FullLoader)
#读取文件中的所有数据
#初始化QQid配置
try:
    qid=int(arg.qqid)
    result['account']['uin']=qid
except ValueError:
    print('ERROR:QQ登录账户输入有误，请核对后再试\nPS:在Docker环境中，你无法交互修改账户信息，请尝试修改QID变量后重试')
    exit (2)
if arg.qqpasswd == False:
    print('Warning:阁下似乎没有配置登录密码，可能需要自行登录容器扫码登录\n在Docker环境中，你无法交互修改账户信息，添加QPWD变量将自动解决此问题')
else:
    qpw=arg.qqpasswd
    result['account']['password']=qpw
    print('Warning:阁下似乎时第一次设置机器人账户，请注意在机器人有账户锁的前提下可能需要短信验证。请随时留意实例提示信息！')
#写入文件
with open('/etc/xxt/cq/config.yml','w+',encoding='utf-8') as f:
    try:
        a=yaml.dump(data=result,stream=f,allow_unicode=True)
    except:
        print(a)
    else:
        #执行总结
        print(f'成功配置启动文件：\n登录QQ号：{result["account"]["uin"]}\nCQHTTP日志等级：{result["output"]["log-level"]}')
