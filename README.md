# 使用须知
1. 本分支为单个Dice！部署完成的Docker环境，如更新本分支请不要添加闭源项目（人人为我我为人人owo）！！！！
2. 这个分支本质为独立于xxt-QQbot的仓库，只是个人不喜欢杂而乱的感觉，加上为感谢前期Dice的整合包对自己的小管家帮助极大（当时Mirai已经删库跑路啦），如果您对这个脚本还有什么好的建议还可以自行修改，push到这里最好啦（算是我的一个小小请求啦QAQ）
3. 这个容器基本做到了部署即用不过我没什么能量可以预知你的骰娘账号，所以你还需要在一开始进入容器内简单的配置一下，文件夹为Mirai_Dice，内容为Dice论坛的20200807的较新一键包
4. 由于尽量适配AGPL的许可和精简内存的目的这个里面的一键包相较于论坛的有些出入，详细如下
# Dice-moe
  Dice！一键包的Docker化版本
## 运行环境：
### 以下是基于一键包所修改的内容：
修改的运行环境     |推荐版本| 用途
 :-: | :-: | :-:
OPENJDK | 8 | Miari协议的基础环境，使用开源版java相较于闭源版更加开放，减少了内存占用（基于Mirai）
wine| 3.0-stable | MiraiNative的WinAPI兼容层
xiasweet/i386-novnc|任意|创建远程链接，相信pull这个容器的都是云服务器小机吧
### 这里是移除组件的详细说明：
移除组件     |原因
 :-: | :-:
 VC_redist.x86.exe | 新版的一键包已经不需要这个运行库了
 RBTray（窗口最小化工具） | 没有必要且代码不开源，无转载许可
 Mem Reduct | 你都使用Docker容器了,不知道直接restart吗？
## 使用方法：
1. 首先你需要先运行一次容器并等待夏小甜守护管家下载本仓库内容的提示
2. 等待同步完成，使用NOVNC进入容器并修改配置文件用于第一次初始化
3. 修改完配置文件测试完毕，准备再重启一遍容器
  您就可以拥有一个小管家骰娘辅助您啦，去跟转生的骰娘聊聊天试试吧owo
## 注意事项：
  出于最小授权的考虑，请自行修改一键包的所有权限为755,log文件夹需要修改为777，否则会出现报错信息并自己退出
## 友人帐及相应的说明
改进版的小管家本质上只是更换了底层，初步版本并没有考虑整合的问题，由于项目创建时Miari项目原作者已删库跑路。所以非常感谢以下的开源项目，没有这些项目那么小管家夏小甜可能要跟其他QQ机器人一样被动写入历史书的命运了
  
感谢以下仓库给予的灵感：
仓库     | Repository链接 
 :-: | :-:
XiaSweet/i386-novnc| https://hub.docker.com/repository/docker/xiasweet/i386-novnc
XiaSweet/xiaxiaotian-QQbot| https://github.com/XiaSweet/xiaxiaotian-QQbot
yyuueexxiinngg/cqhttp-mirai | https://github.com/yyuueexxiinngg/cqhttp-mirai
nonebot/nonebot| https://github.com/nonebot/nonebot
mamoe/mirai|https://github.com/mamoe/mirai
iTXTech/mirai-native|  https://github.com/iTXTech/mirai-native
  
特别感谢[Dice！论坛](https://forum.kokona.tech)的整合包用以提取Miari本体及启动器
