---
layout: page
date: 20220501000000
title: mpv
categories:
tags: 
udc: 
---

## mpv


### ipc


```sh
mpv --input-ipc-server=/tmp/mpv.lock --shuffle ~/Music


echo 'show-text ${playback-time}' | socat - /tmp/mpvsocket


show-text "${filename}"
```


