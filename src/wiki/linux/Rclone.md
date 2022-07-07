---
layout: page
date: 20220412000000
title:
categories:
tags:
- rclone, cmd
udc: 
reference:

1|https://rclone.org/commands/rclone_serve_webdav/

 
---

## Rclone

### mount

```bash
# mount derive
rclone mount 233
  # Downloads \
--umask 0000 \
--default-permissions \
--allow-non-empty \
--allow-other \
--transfers 12 \
--buffer-size 64M \
--low-level-retries 200 --daemon -v --no-modtime




# copy files
rclone copy /bt 233:/w --fast-list --transfers=40 --checkers=40 --tpslimit=10 --drive-chunk-size=1M --max-backlog 200000 --verbose --log-file=/l.log

```


### serve

#### webdav


```bash
rclone serve webdav ./
```


	
