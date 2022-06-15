#!/bin/zsh

pwd=$PWD

rm -rf "$pwd"/docs
sphinx-build "$pwd"/src "$pwd"/docs
