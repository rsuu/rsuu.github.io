---
date: 2022-05-01T00:00:00+08:00
title: gstreamer
categories:
tags: [cmd]
udc: 
---

## gstreamer

```sh
# install
pacman -S --needed gst-plugins-{bad,base,good,ugly} gst-libav
```

### usage

```sh
gst-launch-1.0 audiotestsrc ! audioconvert ! audioresample ! alsasink
    # audio test
  # [directsoundsink, esdsink, alsasink, osxaudiosink, artsdsink, osssink]


gst-launch-1.0 videotestsrc ! ximagesink
    # video test
  # [xvimagesink, d3dvideosink, ximagesink, sdlvideosink, osxvideosink, aasink]


gst-launch-1.0 playbin uri=file:///dev/shm/music.opus
    # auto play audio/video

```

