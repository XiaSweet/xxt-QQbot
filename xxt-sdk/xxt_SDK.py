# -*- coding: utf-8 -*
#夏小甜的帮助及选项文本
def how_readme(mem):
    try:
        input("输入任意信息以继续......")
    except SyntaxError:
        if mem > 2:
            print('\033[1;31m出现错误了：由于你多次尝试跳过提醒程序，程序已自行退出，请重新打开程序吧\033[0m')
            exit (1)
        if mem == 1:
            print('\033[1;31m这是最后一次提醒！请务必阅读完须知后进行下一步操作\033[0m')
            mem=mem+1
            how_readme(mem)
        print("\033[1;31m安全问题至关重要,请你阅读完毕后再继续下一步操作吧qaq\033[0m")
        mem=mem+1
        how_readme(mem)
    else:
        pass
def menu():
    import yuyan_ch
    import os
    os.system("clear")
    yuyan_ch.menu()
    user_menu = input('请选择你需要选择的选项：')
    return user_menu
def menu_1():
    import subprocess
    #现行备份文件
    subprocess.run('sh shell/backup_miraiok.sh',shell=True)
    menu()