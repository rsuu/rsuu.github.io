---
layout: page
date: 20220506000000
title: iconv
categories:
tags:
udc: 
---

## iconv


```bash
mkdir v2; for f in *; do iconv -c -f utf-16 -t utf-8 "$f" > ./v2/"${f%.*}_v2.ass"; done
    # utf-16 to utf-8

```