---
layout: page
date: 20220412000000
title:
categories:
tags:
udc:---

## pacman



```bash
yes | LC_ALL=en_US.UTF-8 pacman -Syu
    # 自动回答 yes


pacman -Syu
    # 更新所有包


pacman -Qlq  neovim | grep /usr/bin
    # 查看某个包所包含的命令


pacman -Ss xxx
    # 搜索 xxx


pacman -Qqe
    # 创建已安装的包的列表


pacman -Qqen
    # 创建已安装的包的列表  但排除外部包


pacman -Qqem
    # 创建已显式安装的外部包的列表


```


## pactree

```bash
pactree linux
    # 显示包的依赖树

```


## pacman-contrib

```bash
pacman -S pacman-contrib


paccache -rk1
    # 仅保留一个过去的版本的包缓存

```


## Error
```bash
# unable to lock database
rm /var/lib/pacman/db.lck


# pacman: /usr/share/zsh/site-functions/_pacman exists in filesystem
# Errors occurred, no packages were upgraded.

pacman -S --dbonly pacman
pacman -S --overwrite glob pacman

```

## makepkg
```bash
pacman -S kernel26-headers file base-devel abs
makepkg -Acs
pacman -U xxx.pkg.tar.zst

```




	
