import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]


p = interact.Process()

print(p.readuntil('Choice:'))
p.sendline('1')

print(p.readuntil('data:'))
p.sendline('aaa')

print(p.readuntil('quiz...'))
p.sendline(' ')

print(p.readuntil('Answer:'))
p.sendline('Hello\nWorld!\n\xC0\xDE\xF0\x0D')

print(p.readuntil('-'))

