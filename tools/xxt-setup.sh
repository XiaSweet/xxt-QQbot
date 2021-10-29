#!/bin/bash
echo '[夏小甜Setup]正在检测程序完整性'
#主程序Git检测
if [ ! -d "/home/xxt-QQbot" ]; then
	echo '[夏小甜Safe]小管家主程序需要初始化，请稍后......'
	cd /home
	git clone --depth=1 -b master https://github.com/XiaSweet/xxt-QQbot
	if [ $? -eq 0 ]; then
		echo "[夏小甜Safe]小管家程序初始化完成owo"
	else
		echo -e "\033[31m[夏小甜]小管家主程序下载失败，请在网络通畅的时候再试试吧QAQ\033[0m"
		echo "[夏小甜Safe]请注意目前有20分钟的时间用来手动进入容器排查，请注意！"
		sleep 1200
		echo "[夏小甜Safe]默认为问题已解决，正在自动重启"
		exit 1
	fi
fi
#CQHTTP检测
if [ ! -d "/etc/xxt/cq" ]; then
  echo '[夏小甜Setup]未检测到QQ中转组件，正在尝试修复'
  mkdir /etc/xxt/cq
fi
cqstat=$(find /etc/xxt/cq -name 'cqhttp')
if [ ! -f "$cqstat" ];then
	echo '[夏小甜Setup]正在部署CQHTTP组件........'
	cq_ver=$(wget -qO- -t1 -T2 "https://api.github.com/repos/Mrs4s/go-cqhttp/releases/latest" | grep "tag_name" | head -n 1 | awk -F ":" '{print $2}' | sed 's/\"//g;s/,//g;s/ //g')
	if [ $? -ne 0 ]; then
		echo -e "\033[31m[夏小甜Setup]暂时无法获取版本信息，将采用默认版本\033[0m"
		cq_ver="v1.0.0-beta7-fix2"
	fi
	os=$(uname)
	osc=$(uname -m)
	if [ $os = "Linux" ];then
		os="linux"
	elif [ $os = "FreeBSD" ];then
		os="FreeBSD"
	elif [ $os = "Solaris" ];then
		os="Solaris"
	else
		echo "What? 很抱歉夏小甜Setup无法兼容这个系统QAQ"
	    echo "[夏小甜Safe]请注意目前有20分钟的时间用来手动进入容器排查，请注意！"
	    sleep 1200
	    echo "[夏小甜Safe]默认为问题已解决，正在自动重启"
		exit 2
	fi
	if [ $osc = "x86_64" ];then
		os_type="amd64"
	elif [ $osc = "armv7l" ];then
		os_type="armv7"
	elif [ $osc = "aarch64" ];then
		os_type="arm64"
	else
		os_type=$(uname -m)
	fi
	echo -e '\033[33m[夏小甜Setup]最新的CQHTTP版本：'${cq_ver}''
	echo 'os：'$os
	echo 'OS架构：'$os_type
	echo '测试时间：'$(date)
	echo -e '正在加载CQHTTP\033[32m'
	wget "https://github.com/Mrs4s/go-cqhttp/releases/download/${cq_ver}/go-cqhttp_${os}_${os_type}.tar.gz" -O /etc/xxt/cq/cqhttp.tar.gz
	if [ $? -ne 0 ]; then
		echo -e "\033[31m[夏小甜Setup]很抱歉CQHTTP下载失败，请在网络通畅的时候再试试吧QAQ\033[0m"
	    echo "[夏小甜Safe]请注意目前有20分钟的时间用来手动进入容器排查，请注意！"
		sleep 1200
		echo "[夏小甜Safe]默认为问题已解决，正在自动重启"
		exit 1
	else
		cd /etc/xxt/cq && tar -zxvf cqhttp.tar.gz && mv go-cqhttp cqhttp
		chmod -R 744 /etc/xxt/cq/cqhttp && rm -f cqhttp.tar.gz
		echo -e "\033[32m[夏小甜Setup]CQHTTP加载完成OWo\033[0m"
	fi
fi
echo -e "\033[32m[夏小甜Setup]QQ茶话会中转组件加载完成OWo\033[0m"
cq_set=$(find /etc/xxt/cq -name 'config.yml')
if [ ! -f "$cq_set" ];then
	echo '[夏小甜管家]CQHTTP初始化完成,即将开始账户设置'
	sleep 3
	cd /home/xxt-QQbot/tools/
	python setting.py -qi $qid -qp $qpwd
	if [ $? -ne 0 ]; then
		echo -e '\033[31m[夏小甜管家]出现了致命错误：关键变量缺失，请确定QID与QPWD变量是否存在！QAQ\033[0m'
		echo '[夏小甜管家]因无法解决的错误而退出了程序。。。。。。。。。。'
		exit 1
	else
		echo -e '[夏小甜管家]CQHTTP配置完毕,即将启动owo\033[0m'
		sleep 3
	fi
else
	echo -e '\033[32m[夏小甜管家]CQHTTP初始化完成,正在启动owo\033[0m'
	cd /etc/xxt/cq && nohup ./cqhttp >/dev/null 2>log &
	sleep 1.5
fi
cp /home/xxt-QQbot/tools/device.json /etc/xxt/cq/device.json
clear
echo '以下是NoneBot的启动日志：'
cd /home/xxt-QQbot/
python start.py