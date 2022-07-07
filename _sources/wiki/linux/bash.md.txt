---
layout: page
date: 20220412000000
title: bash
categories:
tags: [cmd]
udc: 
---

## bash


```sh
# 
n<&-
    关闭输入文件描述符 n

0<&-, <&-
    关闭 stdin

n>&-
    关闭输出文件描述符 n

1>&-, >&-
    关闭 stdout

echo 1 > a
    # 输出 1 到 a
    # > :: 覆盖 a 的内容

echo 1 >> a
    # 输出 1 到 a
    # >> :: 在 a 的末尾追加内容

lskk 2>> a
    # 输出 lskk 输出的错误信息到 a
    # 2>> :: 在 a 的末尾追加错误信息

ls &> a
    # 把 ls 的输出的信息转移到 a
    # &> :: 重定向标准输出和错误输出

cat < a
    # 显示 a 的内容
    # < :: 用特定输出作为输入内容

cat < a > b
    # 接受 a 的内容后输入到 b

echo 1 | cat -
    # 输出 1 给 cat 命令使用


# 后台运行命令 
sleep 90
C-z
    # 后台运行当前命令

fg
    # 将后台命令切换到前台
    # 由用户接管命令控制权

bg sleep 90
    # 后台运行命令


sleep 90 &!
    # 后台运行命令


sleep 90 & disown
    # 后台运行命令


# 使用 nohup 
nohup
> /dev/null
    # 断开标准输出

2> /dev/null
    # 断开标准错误

2>&1 &> /dev/null &




# 替换 
x=path/to/script.sh 

echo "${x%/*}"
path/to

echo "${x##*/}"
script.sh


x=script.sh
echo ${x%%.*}
script


t="hello.world.txt"
echo ${t%.*}
hello.world

echo ${t%%.*}
hello


$ echo -e '
cat <<EOF
\tblabla
EOF
cat <<-EOF
\t\t\t\t\tblabla
\t\t\t\t\t\t\t\t\t\t\t\t\tEOF
' > file.sh
$ bash ./file.sh
      blabla
blabla


<< EOF
    # 允许使用转义符号

<<- EOF
    # 移除转义符号

```
