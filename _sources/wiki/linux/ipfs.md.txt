---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## ipfs

```bash

ipfs add --nocopy --wrap-with-directory file
    # add a new file


ipfs dht findprovs <cid>
    # which show what peers in the DHT are still providing the file, if it can find any.


ipfs repo gc
    # clear all repo


ipfs object get QmPnsQoYZbTS5uednnqWbwwvQohZZw7HS4MpjHnNTABKNR | jq
    # show file name


ipfs filestore ls
    # show all files of local


ipfs pin ls -q --type recursive | xargs ipfs pin rm
    # unpin files

```


	
