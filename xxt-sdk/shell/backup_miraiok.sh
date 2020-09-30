#!/bin/bash
clear
mkdir /tmp/xxt_backup
ls_dir=$(pwd)
xxt_dir=$(expr $ls_dir : '\(\/.*/xxt-QQbot/\)')
mv $xxt_dir/xxt-bin/config.txt /tmp/xxt_backup/config.txt
echo '[同步助手]MiraiOK设置文件移动完成'
echo '[同步助手]正在添加所有git更改'
cd $xxt_dir
git add . -A
echo '[同步助手]开始添加Commit日志'
read -s -n1 -p "按任意键继续，编辑完正常退出即可 ... "
git commit
echo '[同步助手]开始上传源码到Github,仓库为默认仓库'
git push origin
echo '[同步助手]代码同步完毕，正在还原登陆信息文件及最后的操作'
mv /tmp/xxt_backup/config.txt $xxt_dir/xxt-bin/config.txt
rm -r -f /tmp/xxt_backup
echo '[同步助手]操作成功完成'