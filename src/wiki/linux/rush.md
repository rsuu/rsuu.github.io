---
layout: page
date: 20220618132845
title: rush
categories:
tags: [cmd]
udc:  
---

## rush

```bash
rush -j 3 -i in.txt 'rg a'
echo 'I;P;B' | rush -D ';' 'mediainfo --Details kz8Ee8AHMuEA.mp4 | rg "slice_type {}" | wc -l'
echo foo | rush -v v={} 'echo {v}'

```
