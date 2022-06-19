---
layout: page
date: 2022-05-01T00:00:00+08:00
title:
categories:
tags: 
- cmd
udc: 

 
---

## postgresql

```sh
# run sql {
su - postgres -c "initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgres/data'"
    # 初始化

pg_ctl start

psql -d db1 -U userA -f in.sql
    # 之后输入数据库的密码

psql -d db1 -U userA
\i in.sql
# }
```
