---
layout: page
date: 20220618132845
title: ssh
categories:
tags: [cmd]
udc:  
---

## ssh

```bash
pacman -S openssh
```

### ssh

```bash
tar czf - file | ssh user@ip "tar zxf -"
    # 从本地传输到远程

tar czf - file | ssh user@ip "cat > file.tar.gz"
    # 从本地压缩后传输到远程

ssh user@ip "tar zxf -" < file.tar.gz
    # 从本地解压到远程

ssh user@ip "cat file.tar.gz" | tar zxf -
    # 从远程解压到本地

```


### sshd

```bash
ssh-keygen -A


/usr/bin/sshd -p 51234
```