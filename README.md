# 夏小甜QQ酱
  基于Miari/OneBot标准的皇室战争部落：皇家.部落的专属QQ小管家（机器人)
  
 本版本基于原先的[夏小甜小管家](https://github.com/XiaSweet/xiaxiaotian-QQbot)和nonebot为本体，遵守OneBot标准而制作的机器人，以游戏"皇室战争"内的茶话会QQ群机器人“夏小甜”为运行主体。
 
 这个版本着重再于合并以前自己所写的CR辅助插件，本版本开始采用的效率更高的go-cqhttp机器人，因而相对上一版本占用的275MB左右内存甚至不及其的一个零头。同时也将基于机器人安排一键同步组件，简化机械一般的流程，当然这个版本开始目标似乎有点虚无了，不过这又如何呢？
 #### 小管家的目标毕竟是星辰大海( ⊙ o ⊙ )a！
  
## 推荐运行环境：
### 需要自己安装的环境：
运行环境     | 推荐版本 | 用途
 :-: | :-: | :-:
Python| 3.9+ | 运行Nonebot协议所需要的组件
Screen|任意|用于后台运行Miari 及Nonebot
Nonebot |2.0.2| 基于OneBot标准的Python开发SDK
### 以下环境项目已自带：
运行环境 | 用途
 :-: | :-:
go-cqhttp|CQHTTP协议的Miari实现
xiaxiaotian-QQbot| 游戏皇室战争及皇室战争部落“皇家.部落”的管理辅助
## 使用方法：
### （1）使用Docker快速部署
部署Docker后使用如下指令配置并运行即可
>
    docker run -d --name=xxt -v /home/www/xxt:/home --restart=always -e qid=机器人QQ号 -e qpwd=机器人QQ密码
请注意：部署容器后机器人不会有任何的运行提示，在初次登录时可能视机器人添加的群，好友等消息全部回复造成封号问题，请为GO-cqhttp配置令牌桶
### （2）自行安装
1. 使用Git Clone本仓库,参照页面底部仓库逐一修改相应配置
2. 打开项目的Tools文件夹，在你的系统配置qid和qpwd变量
3. 运行xxt.sh安全卫士会自动为你的机器人配置账户和密码并自动登录，其中一些开启账户锁的账号需要二次验证

### 您就可以拥有一个小管家辅助您啦，稍等一会去跟小管家聊聊天试试吧owo
# 特别提示：
为了保证安全，3.x版本机器人自行安装时请不要在安装目录内留存你的机器人账户和密码。请使用Docker部署！
# 特别声明
1. 本项目为个人实验性质，运行并不稳定且无法保证是否会被封号。
2. 本项目内所使用的其他项目版权归各自开发者所有。
3. 本项目基于现有开源项目组合而成不接受issues，由于无法预测的方面，请勿用于生产环境。
4. 本项目跟随引用项目使用AGPL V3.0协议，Mouster可能随时弃坑。
5. 运行本项目即代表您自愿接受以上条款并放弃追究因错误操作或tx封杀导致机器人封号的全部责任owo
## 友人帐及相应的说明
非常感谢以下的开源项目，没有这些项目那么小管家夏小甜的路途可能务必曲折
如何配置请参考以下仓库：
仓库     | Repository链接 
 :-: | :-:
XiaSweet/xiaxiaotian-QQbot| https://github.com/XiaSweet/xiaxiaotian-QQbot
yyuueexxiinngg/cqhttp-mirai | https://github.com/yyuueexxiinngg/cqhttp-mirai
nonebot/nonebot| https://github.com/nonebot/nonebot
mamoe/mirai|https://github.com/mamoe/mirai
iTXTech/mirai-native|  https://github.com/iTXTech/mirai-native
Mrs4s/go-cqhttp |https://github.com/Mrs4s/go-cqhttp
