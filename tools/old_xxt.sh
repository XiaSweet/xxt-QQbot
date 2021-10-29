#!/bin/bash
echo '[夏小甜管家]正在检测程序完整性'
if [ ! -d "/home/xxt-QQbot" ]; then
  echo '[夏小甜管家]小管家主程序需要初始化，请稍后'
  cd /home
  git clone --depth=1 -b master https://github.com/XiaSweet/xxt-QQbot
  if [ $? -ne 0 ]; then
   echo "[夏小甜管家]小管家程序初始化完成owo"
   else
   echo -e "\033[31m[夏小甜管家]小管家主程序下载失败，请在网络通畅的时候再试试吧QAQ\033[0m"
   echo "[夏小甜管家]请注意目前有20分钟的时间用来手动进入容器排查，请注意！"
   sleep 1200
   echo "[夏小甜管家]默认为问题已解决，正在自动重启"
   exit 1
   fi
fi
cd /home/xxt-QQbot
if [ ! -d "/etc/xxt/cq" ]; then
  echo '[夏小甜管家]文件初始化。。。。。。'
  mkdir /etc/xiaxiaotian/cq
fi
cqstat=$(find /etc/xiaxiaotian/cq -name 'cqhttp')
if [ ! -f "$cqstat" ];then
	echo "[夏小甜管家]CQHTTP正在初始化，请稍候"
	os=$(uname)
	osc=$(uname -m)
	if [ $os = "Linux" ] ; then
		os="linux"
	elif [ $os = "FreeBSD" ] ; then
		os="FreeBSD"
	elif [ $os = "Solaris" ] ; then
		os="Solaris"
	else
		os="What?"
	fi
	if [ $osc = "x86_64" ];then
		os_type=amd64
	elif [ $osc = "armv7l" ];then
		os_type=arm
	else
		os_type=$(uname -m)
	fi
	echo -e '\033[33m[夏小甜管家]推荐的CQHTTP版本：'${cq_ver}''
	echo 'os：'$os
	echo 'OS架构：'$os_type
	echo '测试时间：'$(date)
	echo -e '正在加载CQHTTP\033[32m'
	wget "https://github.com/Mrs4s/go-cqhttp/releases/download/v${cq_ver}/go-cqhttp-v$cq_ver-$os-$os_type" -O /etc/xiaxiaotian/cq/cqhttp
	if [ $? -ne 0 ]; then
		echo -e "\033[31m[夏小甜管家]很抱歉CQHTTP下载失败，请在网络通畅的时候再试试吧QAQ\033[0m"
		exit 1
	chmod -R 744 /etc/xiaxiaotian/cq/cqhttp
	else
		chmod -R 744 /etc/xiaxiaotian/cq/cqhttp
		echo -e "\033[32m[夏小甜管家]CQHTTP加载完成OWo\033[0m"
	fi
fi
cq_set=$(find /etc/xiaxiaotian/cq -name 'config.yml')
if [ ! -f "$cq_set" ];then
	echo '[夏小甜管家]CQHTTP初始化完成,现在开始账户设置'
	sleep 3
	python tools/setting.py -qi $qid -qp $qpwd
	if [ $? -ne 0 ]; then
	echo -e '\033[31m[夏小甜管家]出现了致命错误：关键变量缺失，请确定QID与QPWD变量是否存在！QAQ\033[0m'
	echo '[夏小甜管家]因无法解决的错误而退出了程序。。。。。。。。。。'
	exit 1
	else
	echo -e '[夏小甜管家]CQHTTP配置完毕,即将启动owo\033[0m'
	sleep 3
	fi
else
	echo -e '\033[32m[夏小甜管家]CQHTTP初始化完成,马上启动owo\033[0m'
	cd /etc/xiaxiaotian/cq && nohup ./cqhttp >/dev/null 2>log &
	sleep 1.5
fi
cp device.json /etc/xiaxiaotian/cq
clear
echo '以下是NoneBot的启动日志：'
python /home/xxt-QQbot/start.py