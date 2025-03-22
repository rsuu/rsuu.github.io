+++
title = "keyword args"
date = "2025-03-20"
template = "page.html"

[taxonomies]
set = ["idea"]
tags = ["rust"]
+++

## kw-struct

```rust
// 语法糖
fn f(
    v1: u8, v2: u8, 
    struct s {
        r: u8,
        g: u8,
        b: u8,
    }: impl Default,
) {
    // ...
}

// 脱糖后 
fn f(
    v1: u8, v2: u8, 
    // 注意: 有无实现 Default 是在编译时判断的
    r: u8, 
    g: u8,
    b: u8,
) {
    let s = (r, g, b);
    // ...
}

f(1, 2, struct s {
    r: 1,
    g: 2,
    b: 3,
});


let opt = StructA {
    r: 1, 
    g: 2, 
    b: 3, 
    a: 4,
};

// 自动收集 fields
f(1, 2, struct s { ..opt });

```

## kw-enum

```rust
// 对 enum 也是有效的
// ? 如何脱糖
// ? Default
fn f(
    v1: u8, v2: u8, 
    enum e {
        #[default]
        Unit,
        Unnamed(u8),
        Named { r: u8 },
    }: impl Default,
) {
    // ...
}


// 太奇怪
f(1, 2, enum e::Unit);
f(1, 2, enum e::Unnamed(1));
f(1, 2, enum e::Named { r: 1 } );
f(1, 2, enum e::Default::default());

```

```rust

// ? 允许 kw-arg 出现在 unnamed arg 之前
f(1, struct s {
    r: 1,
    g: 2,
    b: 3,
}, 2);

// ? 哪个好
match s {
    struct s { ... } => { ... },
    (...) => { ... },
}

```

## fin

或许还是这样最好,只要命名参数而不要可选参数和自动收集,这样就是单纯的允许手动添加参数名注释了

```rust
fn f(r: u8, g: u8, b: u8) {}

f(a = 1, 2, b = 3);

// 脱糖,少即是多(LESS IS MORE) 🤣
f(/* a = */ 1, 2, /* b = */ 3);
```


```rust
fn f(r: u8, g: u8, b: u8) {}

f(7, 6, 5);
f(r = 7, b = 5, g = 6); // stage 1
f(b = 5, g = 6, ..Default::default()); // stage 2
f(..Default::default());
f(..opts); 

// error
f(6, 5, ..Default::default()); // mix unnamed args and `..`
f(r = 7, 6, 5); // mix unnamed and named args.
f() // empty args

```

[^03221733]: https://github.com/rust-lang/rfcs/issues/323
