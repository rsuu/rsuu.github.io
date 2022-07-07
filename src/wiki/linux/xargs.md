---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## xargs


```bash
# 从文本创建文件
<files.txt xargs -d'\n' touch
xargs -a files.txt -d'\n' touch


# 批量移动
for f in *; do cd $f && fd . | head -1 | xargs mv -t ~/t/1/t$f && cd ../; done
    

```



	
