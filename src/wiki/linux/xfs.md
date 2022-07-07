---
layout: page
date: 20220412000000
title:
categories:
tags:
- xfs, cmd
udc:---

## xfs


```bash
# 启用 bigtime 支持  解决千年虫问题

## 1. 格式化分区时使用
mkfs.xfs -m bigtime=1 /dev/sdX1

## 2. 对已格式化但未挂载的分区使用
xfs_repair -c bigtime=1 /dev/sdX1



# 修复文件系统

## 1. 尝试 mount 和 umount 分区  以便重放日志

## 2. 检查文件系统是否损坏
xfs_repair -n /dev/sdX1
    # 如果没有问题  可以跳过后续步骤

## 3. 安全的修复系统(在这之前你也可以先用 xfs_metadump 备份一下元数据)
xfs_repair /dev/sdX1

## 4. 如果修复失败  可以强制修复系统(会丢失文件)
xfs_repair -L /dev/sdX1
    # 清空日志
xfs_repair /dev/sdX1
    # 修复
```


	
