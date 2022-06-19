---
layout: page
date: 2022-05-01T00:00:00+08:00
title: Rust
categories: [pl]
tags: [rust]
udc: [4]
---

## rust

https://t.me/c/1264662201/227665


### KeyWord

#### fn

函数是一段代码，什么叫在一个另一个线程。闭包是一个实现了 Fn 系列 trait 的 struct ，它有一个成员函数而已


用 move 捕捉的闭包所有访问的数据都在闭包 struct 内部，不会访问外部数据，编译器自动给它实现 Send ，表示它可以被安全转移给另一个线程

线程创建函数签名上要求必须实现 Send ，所以能编译通过就保证了这点

### Trait

Send 保证了可以挪到另一个线程