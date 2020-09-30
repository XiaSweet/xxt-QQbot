# -*- coding: utf-8 -*
#夏小甜的帮助及选项文本
def readme():
    print('运行须知：')
    print('由于Mirai的机制目前不存在自动登陆系统，而MiraiOK的自动登陆模式为明文密码模拟用户输入的方式\
来进行登陆。在Push的过程中如果不将密码明文删除的话会跟随代码一起自动上传，存在严重的安全隐患\
本程序初衷在于自助构建并发布程序，在Push前会将你的密码文件暂时移除并在Push完成后完璧归赵.\n特别提示：如果程序出现的BUG\
导致密码文件无法恢复，请自行Copy MiraiOK的demo设置文件即可')
    print('\033[1;31m存在严重的安全隐患无法自行关闭！！\033[0m')
def menu():
    print('夏小甜小管家De程序菜单：')
    print("\n(1)自助构建小管家程序并Push到Github仓库 \n\
(2)使用Docker映像重新部署小管家 \n\
(3)帮助与支持 \n\
    ")
def menu_help():
    print('夏小甜同步助手：\n本组件为小管家夏小甜的一部分，使用这个组件可以快捷安全的用来同步源码到仓库内而不需要担心明文密码泄露的问题。\n\
友情感谢： \n\
官方仓库：https://github.com/XiaSweet/xxt-QQbot \n\
秘密基地: https://notes.xiasweet.com \n\
本组件基于LGPLv3.0开源，XiaSweet Lab版权所有')
    input("输入任意信息以返回主菜单......")