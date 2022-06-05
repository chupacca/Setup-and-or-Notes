import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]



hex_pw = [0x73, 0x34, 0xf2, 0xf0, 0x76, 0x1a, 0xf5, 0xf4, 0x6b, 0x3b, 0xb9, 0xbf, 0x53, 0x3d, 0xba, 0xbc, 0x63, 0x26, 0xa2, 0xa1, 0x70, 0x55]

ds = ""

for i in range(0, len(hex_pw)):

    hex_value = hex_pw[i]
    char_value = chr(hex_value)
    #print("encrypted_char: " + char_value)

    shifted_value = i<<6
    shifted_value += i

    dv = ord(char_value) ^ shifted_value
    dv = dv & 0xFF
    ds = ds + chr(dv)
print(ds)


p = interact.Process()
print(p.readuntil('password:'))
p.sendline(ds)

print(p.readuntil('password'))

p.interactive()
