+++
title = "the debut of H.266"
date = "2025-03-24"
template = "page.html"
description = "快来品尝新鲜出炉的 H.266"

[taxonomies]
category = ["media"]
tags = ["vvc"]
+++

## build vvenc on termux

```zsh
pkg install binutils-gold llvmgold

git clone --depth 1 https://github.com/fraunhoferhhi/vvenc
cd vvenc
mkdir build               cd build              cmake ..
cmake --build . --config Release
cd ../bin

en266() {
  ffmpeg -i "$1" -pix_fmt yuv420p10le -strict -1 -f yuv4mpegpipe - | \
  ./vvencapp -i - --y4m --format yuv420_10 --hdr hdr10_2020 -t 4 -o "${1%.*}.266"
}

de266() {
  ./vvdecapp -b "$1" -f 1 --y4m -o - | \
  ffmpeg -f yuv4mpegpipe -i - -c:v libwebp -lossless 1 -y "${1%.*}.webp"
}

en266 test.jpg
de266 test.266
```
## fin

今天简单地测试了一下 `H.266` 的压缩图片效果，直接说结论：低码率下，`H.266` 的压缩率相比 `H.265` 略有提升；高压缩比情况下，画质和 `AV1` 一样差（涂抹严重）；而 `H.266` 的压缩速度已经下降到 `AV1` 和 `JXL` 这样的级别了（笑）。  

`H.265` 作为上一代编码算法，质量依然很强。你们 `AV1` 就别老去碰瓷老前辈了，你们真正的竞争对手是 `H.266` 啊！！！  

目前我这边仍然使用 `H.265` 来压缩高质量图片（？），对于非写实图片，`AV1` 的压缩率还是更好一些，毕竟质量不那么敏感。在我这 `H.266` 可能还要再过几年才能取代 `H.265` 吧？嘛，或许没有 8K 视频的话，也没必要上这种大炮……

