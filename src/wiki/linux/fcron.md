---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## fcron

```bash
systemctl enable fcron.service
    # 自动启动 fcron


fcrontab -u <user> -e
    # 编辑指定用户的 fcron 文件



# Example of job definition:
 # .---------------- minute (0 - 59)
 # |  .------------- hour (0 - 23)
 # |  |  .---------- day of month (1 - 31)
 # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
 # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
 # |  |  |  |  |
 # *  *  *  *  *   echo 1

```



	
