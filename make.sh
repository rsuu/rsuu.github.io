#!/bin/bash

rm -rf docs
sphinx-build src docs
python3 scripts fix-comments.py
