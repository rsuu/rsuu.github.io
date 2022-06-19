---
layout: page
date: 2022-04-12T00:00:00+08:00
title: Rust-Async
categories: rust
tags: [async,rust,parallel
udc: [0]
---

## Rust-Async

https://blog.logrocket.com/a-practical-guide-to-async-in-rust/
https://github.com/rust-lang/rust/issues/15641

 

```rust
fn get_two_sites() {
    // 生成两个线程来下载网页.
    let thread_one = thread::spawn(|| download("https:://www.foo.com"));
    let thread_two = thread::spawn(|| download("https:://www.bar.com"));

    // 等待两个线程运行下载完成.
    thread_one.join().expect("thread one panicked");
    thread_two.join().expect("thread two panicked");
}


```


```rust
async fn get_two_sites_async() {
    // 创建两个不同的 "futures", 当创建完成之后将异步下载网页.
    let future_one = download_async("https:://www.foo.com");
    let future_two = download_async("https:://www.bar.com");

    // 同时运行两个 "futures" 直到完成.
    join!(future_one, future_two);
}

```


### async vec

use futures::future::join_all;


 async fn start_consumers(&self) {
    let mut v = Vec::new();
    for consumer in &self.consumers {
        v.push(consumer.consume());
    }
    join_all(v).await;
 }

### daemonize a process
[#1]

