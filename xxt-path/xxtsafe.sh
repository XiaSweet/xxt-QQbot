#!/bin/bash
miraiok=$(find /home -name 'xxt-Storymoon')
mirai=$(find /home -name 'mirai-co*.jar')
echo '[夏小甜安全卫士]正在检测程序完整性'

if ["$mirai" != ""] || ["$miraiok" != ""];then
    echo '[安全卫士]出现问题了：你的小管家被意外修改了，无法运行QAQ'
	echo '[安全卫士]正在重新下载小管家程序，请稍等一会吧owo'
    cd /home
	rm -r -f xxt-QQbot
    git clone https://github.com/XiaSweet/xxt-QQbot
    echo '[安全卫士]程序完整性已修复完成'
else
    echo '[安全卫士]程序完整性检测完毕'
fi

if [ "$qquser" =="" -o "$qqpass" ==""];then
    echo '[安全卫士]出现致命错误，您没有输入QQ信息'
	echo '请在Docker容器运行前添加qquser和qqpass的变量'
	echo -e '\e[1;36qquser变量：你的QQ账号'
	echo -e 'qqpass变量：你的QQ密码\e[1;0m'
	xxtsafe-passwd=$('Error')
	exit 1
else
    echo '[安全卫士]已检测到QQ信息，正在初始化'
	sed -i "s/Im-><qquser/$qquser/g" /home/xxt-QQbot/xxt-bin/config.txt
	sed -i "s/Im-><qqpass/$qqpass/g" /home/xxt-QQbot/xxt-bin/config.txt
	echo '基础运行程序已执行完毕，小管家稍后将会启动,使用愉快owo'
	cd /home/xxt-QQbot/xxt-bin
	/usr/bin/supervisord -c /etc/xiaxiaotian/supervisord.conf
fi