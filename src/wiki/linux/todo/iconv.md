---
layout: page
date: 2022-04-22T00:00:00+08:00
title:
categories:
tags:
- cmd
udc: 

 
---

## iconv


```bash
mkdir v2; for f in *; do iconv -c -f utf-16 -t utf-8 "$f" > ./v2/"${f%.*}_v2.ass"; done
    # utf-16 to utf-8


```



	
