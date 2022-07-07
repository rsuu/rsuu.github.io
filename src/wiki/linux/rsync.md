---
layout: page
date: 20220501000000
title: rsync
categories:
tags: [cmd]
udc: [] 
---

## rsync

```sh
mkdir x; rsync --delete x/ y/
    # 同步一个空文件夹

rsync -rlptDAPv -g -o -X --delete -h --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/lost+found"} / /mnt/xxx
    # 备份系统
```
