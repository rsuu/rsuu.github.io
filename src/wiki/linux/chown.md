---
layout: page
date: 20220412000000
title:
categories:
tags:
udc:---

## chown

```bash
chown user:group f
    # 改变文件的所有者和所有组

chown :group f           
    # 改变文件的所有组

chown user: f               
    # 改变文件的所有者

chown --reference=f1 f
    # 复制 f1 的信息给 f

```

