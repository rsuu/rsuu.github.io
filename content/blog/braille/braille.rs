fn main() {
    let braille = vec![
        Braille {
            ch: Ch::A,
            dots: #[rustfmt::skip]
            [1, 0,
             0, 0,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::B,
            dots: #[rustfmt::skip]
            [1, 0,
             1, 0,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::C,
            dots: #[rustfmt::skip]
            [1, 1,
             0, 0,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::D,
            dots: #[rustfmt::skip]
            [1, 1,
             0, 1,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::E,
            dots: #[rustfmt::skip]
            [1, 0,
             0, 1,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::F,
            dots: #[rustfmt::skip]
            [1, 1,
             1, 0,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::G,
            dots: #[rustfmt::skip]
            [1, 1,
             1, 1,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::H,
            dots: #[rustfmt::skip]
            [1, 0,
             1, 1,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::I,
            dots: #[rustfmt::skip]
            [0, 1,
             1, 0,
             0, 0,],
            category: Category::Letter,
        },
        Braille {
            ch: Ch::J,
            dots: #[rustfmt::skip]
            [0, 1,
             1, 1,
             0, 0,],
            category: Category::Letter,
        },
    ];
}

struct Braille {
    ch: Ch,
    dots: [u8; 6],
    ty: Ty,
}

enum Ty {
    Letter,
    Number,
    Punctuation,
}

enum Ch {
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I,
    J,
}
