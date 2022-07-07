---
layout: page
date: 20220422000000
title: cat
categories:
tags: 
udc: 
---

## cat

```bash
cat << done
    # 输入文本  遇到 done 后退出


cat << done >> ou.txt
    # 在 done 之后追加内容


cat << EOF >> ou.txt > a > b > c
    # 往 ou.txt 中追加文本  并覆盖 a b c 中的内容


cat << EOF > q.rs && rustc q.rs && ./q
    # 写一些代码

cat a
    # 显示 文件a 的内容

cat > a
    # 把键盘输入内容输出到 文件a 里
    # 按 <C-c> 退出 
    # <C-c> 是 Ctrl-c

cat << EOF > a

cat a b > c
    # 把 a 和 b 的内容一起输出到 c 里


```
