首先运行note发现主要有5个功能。创建、编辑、展示、复制、删除
查看文件类型发现是64-bit程序
note: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=8d6f7b0e5171f98c844cdbc14b17e0dac2205fcc, not stripped

检查文件保护类型是
$ checksec note
[*] '/home/ubuntu/Desktop/note'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
