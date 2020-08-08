#!/bin/sh
hasexe=$(find /home -name '*.jar')
if [ "$hasexe" != "" ];then
    echo '[xxtsafe]xxt-qqbot 已安装完毕，将会正常启动.'
    cd /home/xxt-QQbot
    /usr/bin/supervisord -c /etc/xiaxiaotian/supervisord.conf
else
    echo '[xxtsafe]未检测到夏小甜程序，正在下载中owo'
    cd /home
    git clone https://github.com/XiaSweet/xxt-QQbot
    echo '[xxtsafe]下载完成，稍后将会自动启动!'
    cd xxt-QQbot
    /usr/bin/supervisord -c /etc/xiaxiaotian/supervisord.conf
fi