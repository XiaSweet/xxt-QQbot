print('\033[0m[夏小甜管家]正在设置QQ机器人账户......\033[0m')
import hjson
import argparse
parser = argparse.ArgumentParser(description='CQHTTP设置程序')
parser.add_argument('--qqid','-qi',default='3304871685',help='QQ账户，在Docker中应是QID变量')
parser.add_argument('--qqpasswd','-qp',default=False,help='QQ密码，在Docker中应是QPWD变量')
arg = parser.parse_args()
ry=open('config.hjson','r')
r=hjson.loads(ry.read())
try:
    qid=int(arg.qqid)
except ValueError:
    print('在Docker环境中，你无法交互修改账户信息，请调整变量和容器后重试')
    exit (2)
if arg.qqpasswd == False:
    print('在Docker环境中，你无法交互修改账户信息，请添加QPWD变量后再试')
    exit (3)
qpw=arg.qqpasswd
r['password']=qpw
r['uin']=qid
r['encrypt_password']=False
print('\033[31m[夏小甜管家]为了保护机器人账户的安全，推荐自行配置CQHTTP并开启加密！\033[0m')
print('[夏小甜管家]正在保存配置信息......')
rw=open('/etc/xiaxiaotian/cq/config.hjson','w+')
rw.write(hjson.dumps(r))
print('\033[32m[夏小甜管家]配置信息保存成功')