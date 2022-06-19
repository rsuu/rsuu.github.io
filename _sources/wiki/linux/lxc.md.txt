---
layout: post
date: 20220618132845
title: lxc
categories: 
tags: [cmd]
udc: [0]
---

## lxc


```bash
lxc-create -t download -n arch
    # 创建容器


lxc-start -n arch
    # 启动容器
    

lxc-attach -n arch
    # 登入容器


lxc-info -n arch
    # 查看容器的状态


lxc-ls -f arch
    # 显示已安装的容器


lxc-stop -n arch
    # 关闭容器


lxc-destroy -n arch
    # 删除容器


echo 'lxc.start.auto = 1' >> /var/lib/lxc/arch/config
    # 开机时启动容器


echo 'lxc.mount.entry = /mnt mnt none bind 0 0' >> /var/lib/lxc/arch/config
    # 共享主机的某个目录给容器

```

