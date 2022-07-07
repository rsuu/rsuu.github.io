---
layout: page
date: 20220412000000
title:
categories:
tags: [cargo, rustup]
udc: [004.42]
---

## cargo

[^1]
[^1]:https://blog.csdn.net/mutourend/article/details/100104378

```bash
cargo search <name>
    # 搜索包

cargo install <name>
    # 下载包

cargo remove <name>
    # 移除包

cargo build
    # 编译代码

cargo test
    # 运行测试代码

cargo run
    # 编译并运行程序

cargo run -- -h
    # 编译并运行程序  然后传递参数给程序

cargo build --release
    # 以 release 方式编译代码



```



### rustup

```bash
rustup toolchain install nightly-2021-11-01
    # 安装指定的 nightly 版本



# 卸载指定版本
rustup help toolchain
rustup toolchain uninstall <xxx>


rustup default nightly-2019-05-22-x86_64-unknown-linux-gnu
    # 切换回过去的某个指定版本


```


### kernel

```bash
# 编译内核
rustup default nightly
rustup component add llvm-tools-preview
RUSTFLAGS='-C linker=lld' cargo bootimage
qemu-system-x86_64 -drive format=raw,file=/tmp/cargo/target/x86_64-blog_os/debug/bootimage-blog_os.bin

```

### other

```bash
strip a
    # 给程序瘦身


```

