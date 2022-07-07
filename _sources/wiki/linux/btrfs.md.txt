---
layout: page
date: 20220418164621
title: btrfs
categories:
tags: [btrfs]
udc: [004.42]
---

## Btrfs

```bash
btrfs device stats /


btrfs device stats /dev/sda1


btrfs filesystem usage /


btrfs filesystem defragment -r /
    # 碎片整理


btrfs property set /root/Downloads compression none
    # 为目录关闭压缩选项

```
