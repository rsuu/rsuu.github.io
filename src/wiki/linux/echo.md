---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## echo

```bash
# 
FILE="example.tar.gz"

echo "${FILE%%.*}"
example

echo "${FILE%.*}"
example.tar

echo "${FILE#*.}"
tar.gz

echo "${FILE##*.}"
gz






echo -e "\e[?1049h"
    # 进入 备用终端[alternate screen]


echo -e "\e[?1049l"
    # 退出 备用终端[alternate screen]


tput smcup
    # 进入 备用终端[alternate screen]


tput rmcup
    # 退出 备用终端[alternate screen]


echo -e "lines\ncols"|tput -S
    # 获取终端的宽度和高度

```


	
