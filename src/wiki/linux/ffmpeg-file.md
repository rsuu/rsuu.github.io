---
layout: page
date: 20220412000000
title: ffmpeg-file
categories: linux
tags:
udc:
---

## ffmpeg-file

```bash
ffmpeg -i 1.jpg -q:v 16 -fs 10M output
    # 输出前 10M 的数据


ffmpeg -i 1.jpg -f mjpeg pipe:1 | sponge 2.jpg
    # output to pipe
    # e.g. 0 for stdin, 1 for stdout, 2 for stderr
    # install sponage with `pacman -S moreutils`

ffmpeg -i 1.jpg -f mjpeg pipe:1 | cat > 2.jpg

ffmpeg -i 1.jpg -f mjpeg pipe: | cat > 2.jpg


cat test.wav | ffmpeg -i pipe:0
    # read from bytes

ffmpeg -i "1.mp4" -c:v mpe4 -acodec aac -strict experimental "1.mp4" < /dev/null

```




