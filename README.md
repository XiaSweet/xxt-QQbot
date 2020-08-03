# 特别声明
1. 本项目为个人实验性质，运行并不稳定且无法保证是否会被封号。
2. 本项目内所使用的其他项目版权归各自开发者所有。
3. 本项目基于现有开源项目组合而成不接受issues，由于无法预测的方面，请勿用于生产环境。
4. 本项目跟随引用项目使用AGPL V3.0协议，Mouster可能随时弃坑。
5. 运行本项目即代表您自愿接受以上条款并放弃追究因错误操作或tx封杀导致机器人封号的全部责任owo
# 夏小甜QQ酱
基于Miari与Nonebot所组合的皇室战争部落：皇家.部落的专属QQ小管家（机器人）
## 前言
看过EVA结局的也许知道，虽然人类看似被终结了，但却换了另一种方式重生。小管家也一样。ಥ‿ಥ

本版本基于原先的[夏小甜小管家](https://github.com/XiaSweet/xiaxiaotian-QQbot)和nonebot为本体，借助开源项目Miari以及cqhttp-mirai组件合并而成。原先的版本虽然跟随着酷Q的关闭而远去，虽然大部分QQ机器人都被迫关闭，但是上帝总会为你在关门的时候打开一扇窗。虽然某公司继续作恶，但请坚信，光明的到来只是时间的问题owo。
  
## 推荐运行环境：
### 需要自己安装的环境：
运行环境     | 推荐版本 | 用途
 :-: | :-: | :-:
OPENJDK| 11 | Miari协议及服务端的基础环境
Python| 3.7 | 运行Nonebot协议所需要的组件
Screen|任意| 可选，用于后台运行Miari 及Nonebot
Nonebot |1.6.0| 独立于Miari的一套原用于CoolQ机器人的快捷SDK
### 以下环境项目已自带：
运行环境 | 用途
 :-: | :-:
Miari|QQ协议的基础运行包
cqhttp-mirai|CQHTTP协议的Miari实现
xiaxiaotian-QQbot| 游戏皇室战争及皇室战争部落“皇家.部落”的管理辅助
### 可选自己安装的组件：
运行环境 | 用途
 :-: | :-:
 Dice！| 用于QQ跑团的骰子娘 
 mirai-native |强大的 Mirai 原生插件加载器
 wine | 用于兼容Dice！的Windows兼容层（Windows系统不需要）
## 使用方法：
1. 使用Git Clone本仓库,参照页面底部仓库逐一修改相应配置
2. 使用Screen单独开启一个后台终端并打开项目的xiaxiaotian文件夹
3. 使用Python运行start.py并挂后台运行
4. 回到项目根目录并执行以下代码开始运行
>
    java -jar mirai-console-wrapper-1.3.0.jar --update KEEP
5. 在Miari加载完成后运行
>
    login 您的机器人QQ账户 账户密码
  
  您就可以拥有一个小管家辅助您啦，稍等一会去跟小管家聊聊天试试吧owo
## 友人帐及相应的说明
改进版的小管家本质上只是更换了底层，初步版本并没有考虑整合的问题，由于项目创建时Miari项目原作者已删库跑路。所以非常感谢以下的开源项目，没有这些项目那么小管家夏小甜可能要跟其他QQ机器人一样被动写入历史书的命运了
  
如何配置请参考以下仓库：
仓库     | Repository链接 
 :-: | :-:
XiaSweet/xiaxiaotian-QQbot| https://github.com/XiaSweet/xiaxiaotian-QQbot
yyuueexxiinngg/cqhttp-mirai | https://github.com/yyuueexxiinngg/cqhttp-mirai
nonebot/nonebot| https://github.com/nonebot/nonebot
mamoe/mirai|https://github.com/mamoe/mirai
iTXTech/mirai-native|  https://github.com/iTXTech/mirai-native
  
特别感谢[Dice！论坛](https://forum.kokona.tech)的整合包用以提取Miari本体及启动器
