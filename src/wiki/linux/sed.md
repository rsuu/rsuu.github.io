---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## sed

```sh
sed -n '/foo/{:start /bar/!{N;b start};/your_regex/p}' your_file
    # 跨行匹配


echo dog dog dos | sed -e 's:dog:log:g'


sed -n 30,40p in.txt
    # 显示 30 至 40 行

# 替换文件中的所有匹配项
sed -i 's/原字符串/替换字符串/g' filename


# 同时执行两个替换规则
sed 's/^/添加的头部&/g；s/$/&添加的尾部/g' 




# 注意这里的 " & " 符号，如果没有 “&”，就会直接将匹配到的字符串替换掉
sed 's/^/添加的头部&/g' 　　　　 #在所有行首添加
sed 's/$/&添加的尾部/g' 　　　　 #在所有行末添加
sed '2s/原字符串/替换字符串/g'　 #替换第2行
sed '$s/原字符串/替换字符串/g'   #替换最后一行
sed '2,5s/原字符串/替换字符串/g' #替换2到5行
sed '2,$s/原字符串/替换字符串/g' #替换2到最后一行
```

