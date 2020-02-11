from pwn import *
import base64

host = 'misc.ctf.nullcon.net'
port = 8000

context.log_level = 'debug'

def getPic(i):
    p = remote(host, port)
    p.recvuntil('4 for lower right\n')
    c = p.recvline()
    print ('[%d]content: '%i, c)
    io = open(str(i) + '.png', 'wb')
    io.write(base64.b64decode(c[:-1]))
    io.close()
    print('current: ', i)

for i in range(10, 50):
    getPic(i)
