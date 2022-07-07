---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## curl

```bash
curl -F "userid=1; filecomment=This is an image file; path=@test.txt" 'http://test.com/uploader.php'
    # miniserver upload file




curl -I https://github.com
    # head


curl -head https://github.com
    # head


echo xxx > xxx.txt && curl -F "c=@-" "http://fars.ee/" < xxx.txt



curl -C - -0 "https://avatars.githubusercontent.com/u/38876461?s=96&v=4" --output 0.jpg
    # 下载文件
    # -C - :: 断点续传
    # -p :: 自动命名文件
    # --output :: 设置保存文件的路径(因为链接中无法获取文件类型  所以需要自定义)


curl --trace-ascii - http://www.google.com/
    # --trace-ascii :: 跟踪访问过程



curl -X POST --data "email=test@example.com&press=%20OK%20"  http://www.example.com/form.php


curl -X POST -F 'file=@./upload.txt' http://www.example.com/upload.php






curl -X GET "http://www.example.com/api/resources"

curl -X GET "http://www.example.com/api/resources/1"

curl -X POST -H "Content-Type: application/json" -d '{"status" : false, "name" : "Jack"}' "http://www.example.com/api/resources"


curl -X PUT -H "Content-Type: application/json" -d '{"status" : false }' "http://www.example.com/api/resources"


curl -X DELETE "http://www.example.com/api/resources/1"



curl --cookie "name=Jack" http://www.example.com
    # 指定 cookie

curl --cookie stored_cookies_file_path http://www.example.com
    # 读取 cookie 文件

curl --user-agent "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)" http://www.example.com
    # 指定 User Agent


curl -i --user secret:vary_secret http://www.example.com/api/resources


```



```bash
-X/--request [GET|POST|PUT|DELETE|PATCH]  使用指定的 http method 來發出 http request
-H/--header                           設定 request 裡所攜帶的 header
-i/--include                          在 output 顯示 response 的 header
-d/--data                             攜帶 HTTP POST Data 
-v/--verbose                          輸出更多的訊息方便 debug
-u/--user                             攜帶使用者帳號、密碼
-b/--cookie                           攜帶 cookie（可以是參數或是檔案位置）



```


	
