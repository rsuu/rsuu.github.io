---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## espeak-ng


```bash
pacman -S espeak-ng




# 整点报时 {
echo 'espeak-ng -v zh "现在时间是 `\date +"%H时%t%M分%t%S秒"`"' > xxx.sh
chmod 777 xxx.sh
fcrontab -e
0 * * * * xxx.sh
}




espeak-ng -v en-us+f4 'today is a good day'
    # 使用美式英语+女声


espeak-ng --voices=zh
    # 查看所有可用的中文语音


```


	
