FROM python:3.8.5-slim
MAINTAINER xiasweet lolosweet@storymail.xiasweet.com
#更新Debian基础的软件源为国内源，提高下载速度
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
	&&sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
#部署夏小甜基础运行库
RUN apt-get update \
        && apt-get upgrade -y \
		&& mkdir -p /usr/share/man/man1\
        && apt-get install -y  nano git screen supervisor openjdk-11-jre locales\
		&& mkdir /etc/xiaxiaotian
# 设置时区为上海
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Shanghai
#部署夏小甜小管家底层程序及本体
RUN pip install nonebot
#添加配置文件
COPY xiaxiaotian/xxt-path/* /etc/xiaxiaotian/

#后台运行配置的文件
CMD ["sh","/etc/xiaxiaotian/xiaxiaotian-safe.sh"]