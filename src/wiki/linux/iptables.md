---
layout: page
date: 20220412000000
title: iptables
categories:
tags: [cmd, ip]
udc: 
---

## iptables

```bash
iptables -S
iptables --list
iptables -L
iptables -S TABLE_NAME
iptables --table NameHere --list
iptables -t NameHere -L -n -v --line-numbers


iptables -t nat -L
iptables -t filter -L
iptables -t raw -L
iptables -t security -L
iptables -t mangle -L
iptables -t nat -L 
iptables -t nat -L --line-numbers -n
iptables -t nat -L -n -v



ip6tables -L -n -v

    # target – Tell what to down when a packet matches the rule.
    # prot – The protocol for rule.
    # opt – Additional options for rule.
    # source – The source IP address/subnet/domain name.
    # destination – The destination IP address/subnet/domain name.

```
