FROM xiasweet/i386-novnc:latest
MAINTAINER xiasweet lolosweet@storymail.xiasweet.com
#更新Ubuntu基础的软件源为国内源，提高下载速度
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated \
	xvfb x11vnc xdotool wget tar gnupg2 \
        language-pack-zh-hans tzdata wget software-properties-common apt-transport-https && \
    add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
# 安装 wine
RUN dpkg --add-architecture i386 && \
	wget -O - https://dl.winehq.org/wine-builds/winehq.key | apt-key add - && \
	echo 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' |tee /etc/apt/sources.list.d/winehq.list && \
	apt-get update && apt-get -y install winehq-stable
RUN mkdir /opt/wine-stable/share/wine/mono && wget -O - https://dl.winehq.org/wine/wine-mono/4.9.4/wine-mono-bin-4.9.4.tar.gz |tar -xzv -C /opt/wine-stable/share/wine/mono && \
	mkdir /opt/wine-stable/share/wine/gecko && wget -O /opt/wine-stable/share/wine/gecko/wine-gecko-2.47.1-x86.msi https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86.msi && wget -O /opt/wine-stable/share/wine/gecko/wine-gecko-2.47.1-x86_64.msi https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86_64.msi  && \
	apt-get -y full-upgrade && apt-get clean
# copy 文件
COPY ./docker-root /
# 各种环境变量
ENV LANG=zh_CN.UTF-8 \
    LC_ALL=zh_CN.UTF-8 \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    S6_CMD_ARG0=/sbin/entrypoint.sh \
    VNC_GEOMETRY=1000x600 \
    VNC_PASSWD=66666666 \
    USER_PASSWD='' \
    DEBIAN_FRONTEND=noninteractive