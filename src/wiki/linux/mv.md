---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## mv

```bash
mv -- *([1,100]) /other/
    # 在 zsh 中移动100个文件


mv -- (^/[1,100]) /other/
    # 在 zsh 中移动100个文件  包括隐藏文件


for f in *; do cd $f && mv */* $f && cd .. ; done
    # 将文件向上移动一层
```


	
