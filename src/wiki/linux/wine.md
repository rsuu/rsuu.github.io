---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## wine

```bash
winetricks d3dx9* msxml3 msxml4 vcrun2003 quartz devenum corefonts lucida tahoma d3dcompiler_43

```


```bash
# 关掉 WINEDEBUG

WINEDEBUG=-all game.exe

```



```bash
# 32位

某些游戏只支持 32位
倘若出现打不开游戏的情况
可以尝试下使用 32位 的 wine


win32() {
    WINEARCH=win32 WINEPREFIX=$XDG_DATA_HOME/win32 \
        \wine $1 -force-d3d9
}

```


	
