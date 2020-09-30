FROM python:3.8.5-slim

#更新Debian基础的软件源为国内源，提高下载速度并安装基础运行库
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
	&& sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list \
    && apt-get update \
    && apt-get upgrade -y \
    && mkdir -p /usr/share/man/man1\
    && apt-get install -y git openjdk-11-jre\
	&& mkdir /etc/xiaxiaotian
# 安装守护程序
RUN apt-get install -y supervisor
#部署夏小甜小管家底层程序及本体
RUN python -m pip install --upgrade pip \
    && pip install nonebot msgpack ujson
 #添加配置文件并进行最后的清理工作
COPY xxt-path/* /etc/xiaxiaotian/
RUN apt-get clean
# 设置时区
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Shanghai
#后台运行配置的文件
CMD ["sh","/etc/xiaxiaotian/xxtsafe.sh"]