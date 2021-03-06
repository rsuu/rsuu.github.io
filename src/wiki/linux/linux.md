---
layout: page
date: 2022-04-12T00:00:00+08:00
title: Linux
categories: linux
tags: [ing,linux,os]
udc: [004.42
---

## Linux

https://zh.m.wikipedia.org/wiki/%E5%86%85%E6%A0%B8

+ 内核
    + 宏内核(大众使用的基本都是这个)
        + Unix
            + BSD
        + Unix-like
            + Linux
            + FreeBSD
        + DOS
            + Windows
        + Mac OS
    + 微内核
    + 外内核

[](../Assets/Image/Svg/cs/Kernel_Layout.svg)

### Kernel

一个内核所做的事

+ Kernel
    + 内存管理[Memory Management]
        += 记录内存都用来干什么了
    + 进程调度[SCHED]
        += 确定哪些进程可以与使用 CPU
    + 设备驱动
        += 调度硬件与进程之间的互动
        + 虚拟文件系统[Virtual File System]
    + 系统调用
        + 处理程序的请求
    + 网络接口[Network Interface]
    + 进程通信[Interprocess Communication]


可以把 kernel 当成一个翻译官
他把我们说的话翻译给机器听
又把机器说的话翻译给我们听
以便让我们可以和机器沟通

#### 内存管理
#### 进程调度
#### 虚拟文件系统
#### 网络接口
#### 进程通信



### 硬件

+ 主要的几部分
    + 电源
    + 主板
        + CPU[中央处理器]
        + RAM[内存]
            + SRAM[静态随机存取记忆体]
            + DRAM[动态随机存取记忆体]
        + HDD[硬盘] / SSD[闪存]
        + 显卡 / 集成显卡
        + 声卡
        + 网卡
    + 输出设备
        + 显示器
        + 扬声器
    + 输入设备
        + 鼠标
        + 键盘


