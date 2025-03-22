+++
title = "The Little MIDI"
template = "page.html"
date="2024-07-01"

[taxonomies]
set = ["media"]
tags = ["midi","lilypond","staff","audio"]
+++

## Staff

制谱这块我们用[LilyPond],虽然用的是`LaTeX`那样的语法(还混入了`LISP`),但除此之外也没什么好的选择了,能在终端里使用还兼顾着这么完美的质量...


```lilypond
% test.ly
\version "2.24.3"
\language "english"

\score {
    \midi   {} 

    \relative {
        c d e f g a b
    }
}
```

然后轻轻地编译一下: `lilypond test.ly`

## Player

[FluidSynth]在[Termux]上不知道为啥没声音,所以只能用[MPV]来播放,绕了个小圈子.

虽然[TiMidity++]也可以播放[MIDI],但他本身指定字体的方式过于繁琐(只能通过配置文件来指定),所以这里就选择了FluidSynth.

```zsh
midi-play() {
    # https://archive.org/details/500-soundfonts-full-gm-sets
    _NAME="Arachno.sf2"
    _FONT="$HOME/soundfonts/$_NAME"
    _FORMAT=s16le
    _RATIO=44100

    fluidsynth -nli -o synth.cpu-cores=8 \
        -r $_RATIO -g 2 -T raw -F - \
        -i $_FONT $1 \
        | mpv \
        --demuxer=rawaudio \
        --demuxer-rawaudio-format=$_FORMAT \
        --demuxer-rawaudio-rate=$_RATIO \
        -
}
```

DONE: `midi-play test.midi`

[MIDI]: https://en.wikipedia.org/wiki/MIDI
[FluidSynth]: https://github.com/FluidSynth/fluidsynth
[MPV]: https://github.com/mpv-player/mpv
[Termux]: https://termux.dev
[TiMidity++]: https://wiki.archlinux.org/title/Timidity++
[LilyPond]: https://lilypond.org
