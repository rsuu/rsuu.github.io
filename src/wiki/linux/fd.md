---
layout: page
layout: page
date: 20220412000000
title: fd
categories:
tags: [cmd]
udc: [] 
---

## fd

### Install

```bash
# Arch
pacman -S fd

```




```bash
fd foo
    # 查找文件名中包含 foo 的文件


fd . | head -10 | xargs mv -t ../2
    # 移动前10个文件到 ../2


fd -t f md -x sd '\+ ' -- '- ' {}


fd . --exclude=*.cbz --max-depth=1 -x cp -rl '{}' ../1
    # 合并当前目录到../1


fd --type f --glob '*.rs' -x rustfmt {}


fd -x mv '{}' '{}'.jpg
    # 重命名文件


fd -x sed -i ':a;N;s/layout: page
date: .*\n//g' {}
    # 替换换行符(替换一次)


fd -x sed -i ':a;N;$!ba;s/layout: page
date: .*\n//g' {}
    # 替换换行符(替换多次)


fd . --type d --max-depth=1 -x \rm -rf -v
    # 查找当前路径下的所有目录并删除
        # --type d :  只搜索目录
        # --max-depth=1 :  最大搜索深度为1
        # -x :  --exec 传递参数
        # -v :  显示详细信息
```



	
