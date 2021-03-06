---
layout: page
date: 20220618137845
title: strace
categories: linux
tags: [cmd, todo]
udc: [0]
---

## strace

> 用于追踪程序的系统调用

[^1]
[^1]:https://colobu.com/2021/04/30/strace-commands-for-troubleshooting-and-debugging-linux/
```bash
strace ls



strace -p <pid>
strace -p 1
    # 启动后可以使用 <ctrl+c> 退出


strace -c ls
    # -c :: 得到追踪的每一种系统调用的耗时和次数和失败次数

strace -i ls
    # -i :: 显示每一次系统调用的时候的指令指针


strace -t ls
    # -t :: 显示时间戳

strace -T ls
    # -T :: 显示系统调用的耗时时间



# 追踪特定的系统调用
strace -e trace=<type> ls
    # type 可以是[signal, abbrev, verbose, raw, read, write, all]

strace -e trace=read ls

strace trace=open,close,read,write ls

strace -e trace=all ls

# 针对特定类型进行追踪

[process, file, memory, network, signal, ...]

strace -q -e trace=process ls
```
