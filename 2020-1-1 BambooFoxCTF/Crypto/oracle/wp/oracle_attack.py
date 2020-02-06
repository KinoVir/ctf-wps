from pwn import *
from Crypto.Util.number import *
# r = process('./server.py')
r = remote('34.82.101.212',20001)

r.recvuntil('Exit\n')
r.send('1\n')
c = r.recvline()
m = re.search(r"\d", c.decode('utf-8'))
C = int(c[m.start():].strip().decode('utf-8'))
n = r.recvline()
m = re.search(r"\d", n.decode('utf-8'))
N = int(n[m.start():].strip().decode('utf-8'))
r.recvuntil('Exit\n')
print("C=",C)
print("N=",N)

def _decrypt(c):
    r.send('2\n')
    r.send(c)
    r.send('\n')
    message = r.recvuntil('Exit\n')
    #print(message)
    m = re.search(r"\d", message.decode('utf-8'))
    message = int(message[m.start():m.start()+1].decode('utf-8'))
    # if message == 0 or  message == 2:
    #     message = 1
    # else:
    #     message = 0
    # if message != 0: 
    #     message = 1
    return message

e = 65537
upper_limit = N
mid_limit = N // 2
lower_limit = 0

i = 1
# 0 -> 1 -> 0
# for 1024 bit N
# while i <= 1024:
#     chosen_ct = (C*pow(2**i, e, N)) % N
#     # chosen_ct = (C*pow(2, i*e, N)) % N
#     output = _decrypt(str(chosen_ct))
#     if output == 0:
#         upper_limit = lower_limit + (((upper_limit - lower_limit) // 2))#(upper_limit + lower_limit)//2
#     elif output == 1:
#         lower_limit = lower_limit + (((upper_limit - lower_limit) // 2))#(lower_limit + upper_limit)//2
#     i += 1
#     a = long_to_bytes(upper_limit)
#     if b'Bamboo' in a:
#         print(i)
#         break

# Cyclic Groups For 3 -->
# if N%3 == 1; -> 0 -> 2 -> 1 -> 0
# if N%3 == 2; -> 0 -> 1 -> 2 -> 0

if N % 3 == 2:
    x = 2
else:
    x = 1

print("X: ", x)
lower_limit + ((upper_limit - lower_limit) // 3)
while i <= 1024:
    chosen_ct = (C*pow(3**i, e, N)) % N
    # chosen_ct = (C*pow(2, i*e, N)) % N
    output = _decrypt(str(chosen_ct))
    if output == 0:
        # upper_limit = (upper_limit + lower_limit)//2
        upper_limit = lower_limit + (((upper_limit - lower_limit) // 3))
    elif output == x:
        # lower_limit = (lower_limit + upper_limit)//2
        lower_limit = lower_limit + (((upper_limit - lower_limit) // 3) * 2)
    else:
        diff = upper_limit - lower_limit
        upper_limit = lower_limit + ((diff // 3) * 2)
        lower_limit = lower_limit + ((diff // 3))
    assert lower_limit <= upper_limit, output
    i += 1
    a = long_to_bytes(upper_limit)
    # if b'Bamboo' in a:
    #     print(i)
    #     break

# Decrypted ciphertext
print(long_to_bytes(upper_limit))
print(upper_limit)
