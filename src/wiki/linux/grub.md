---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc:---

## grub

grub 会自动识别新的内核


```bash
grub-mkconfig -o /boot/grub/grub.cfg

# Generating grub configuration file ...
# Found linux image: /boot/vmlinuz-linux-btf
# Found initrd image: /boot/initramfs-linux-btf.img
# Found fallback initrd image(s) in /boot: initramfs-linux-btf-fallback.img
# Found linux image: /boot/vmlinuz-linux
# Found initrd image: /boot/initramfs-linux.img
# Found fallback initrd image(s) in /boot: initramfs-linux-fallback.img
# done



```



	
