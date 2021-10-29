#FROM --platform=$TARGETPLATFORM python:3.9.2-alpine3.12
FROM python:3.9.2-alpine3.12
#更新Debian基础的软件源为国内源，提高下载速度并同步部署守护程序
RUN #sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories &&\
	apk update &&\
	apk upgrade &&\
	apk add --no-cache bash\
	bash-doc \
	bash-completion
#部署并运行基础文件
RUN apk update && \
	apk add git nano wget musl-dev build-base
#部署夏小甜小管家底层程序及本体
RUN python -m pip install --upgrade pip && \
	pip install nonebot2 nonebot-adapter-cqhttp pyyaml pymysql requests
 #添加配置文件并进行最后的清理工作
COPY tools/* /etc/xxt/
RUN apk add bash bash-completion &&\
	apk del build-base &&\
	rm -rf /var/cache/apk/* 
# 设置时区
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Shanghai
#后台运行配置的文件
CMD ["/bin/sh"," /etc/xxt/xxt-setup.sh"]