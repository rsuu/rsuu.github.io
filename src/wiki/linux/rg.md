---
layout: page
date: 20220707134605
title: rg
categories:
tags: [cmd]
udc: 
---

## rg

```bash
# Arch
pacman -S ripgrep
```




```bash
rg foo
    # 搜索包含 foo 的文本


rg -l foo
    # 只显示文件的路径
    # Only show the file path


ps -a | rg -o 'rclone'
    # 只显示匹配到的内容


ps -a | rg -v 'rclone'
    # 只显示没有匹配到的内容


rg --files-with-matches
    # 只显示包含匹配的文件路径


rg --files-without-match 'rclone'
    # 只显示不包含匹配的文件路径


for f in $(rg 'test' -l); 
do 
  cat $f
done


# 使用文本里的二级标题作为文件名
for f in *; 
do 
  mv $f "$(rg '^## .*' $f -o -m 1 -I --no-line-number | rg ' .*' -o | tr -d ' ')".md; 
done


-o, --only-matching, print only the matched part of the line (instead of the entire line)
-a, --text, process a binary file as if it were text
-m 1, --max-count, stop reading a file after 1 matching line
-h, --no-filename, suppress the prefixing of file names on output
-r, --recursive, read all files under a directory recursively
```



	
