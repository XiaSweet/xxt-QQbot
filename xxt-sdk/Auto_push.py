# -*- coding: utf-8 -*
import xxt_SDK
import yuyan_ch
# 介绍页面
yuyan_ch.readme()
xxt_SDK.how_readme(0)
#菜单页面
page_err=0
def menu():
    global page_err
    page=xxt_SDK.menu()
    if page_err > 2:
        print('多次选择错误，请重新运行程序吧')
    elif page == '1':
        xxt_SDK.menu_1()
        menu()
    elif page == '2':
        print('本功能暂未开放，请君返回首页望望吧')
        menu()
    elif page == '3':
        yuyan_ch.menu_help()
        menu()
    else:
        import time
        page_err=page_err+1
        print('出现错误了:\n请正确的输入数字以进入相应的插件，稍后再重新尝试一下吧')
        time.sleep(2)
        menu()
menu()