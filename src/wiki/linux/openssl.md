---
layout: page
date: 20220412000000
title:
categories:
tags:
udc:---

## openssl

```bash
# ssl
openssl req -newkey rsa:4096 \
           -x509 \
           -sha256 \
           -days 3650 \
           -nodes \
           -out example.crt \
           -keyout example.key \
           -subj "/C=CN/ST=GD/L=GZ/O=no/OU=no Department/CN=127.0.0.1"
```



	
