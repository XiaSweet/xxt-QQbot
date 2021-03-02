FROM python:3.9.2-alpine3.12

#更新Debian基础的软件源为国内源，提高下载速度并安装Bash
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories &&\
	apk update &&\
	apk upgrade &&\
	apk add --no-cache bash\
	bash-doc \
	bash-completion
# 安装守护程序
RUN apk update && \
	apk add git nano wget musl-dev build-base
#部署夏小甜小管家底层程序及本体
RUN python -m pip install --upgrade pip \
    && pip install nonebot2 
 #添加配置文件并进行最后的清理工作
RUN rm -rf /var/cache/apk/* &&\
	apk del build-base
COPY tools/* /etc/xiaxiaotian/
# 设置时区
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Shanghai
#后台运行配置的文件
CMD ["bash","/etc/xiaxiaotian/xxt.sh"]