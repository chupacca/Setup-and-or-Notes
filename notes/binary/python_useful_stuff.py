#!/bin/python3
import sys

print("==========================================")
print(" Calc wraparound` distance b/w 2 addresses")
print("==========================================")
def delta(start, end):
    return (0xffffffffffffffff - start) + end

print("==================================")
print(" Ways to `print` bytes in Python3")
print("==================================")
# This will print binary output in a similar way to `print` in Python2
sys.stdout.buffer.write(b"\x61\x62")
print("")
# Regular `print` in Python3
print(b"\x61\x62")
print("")



print("============================")
print("      Hex <--> Decimal")
print("============================")
# Hex to decimal
hex_to_dec = int("0x100", 16)
print(hex_to_dec)
print(hex(16))



print("============================")
print("            XOR")
print("============================")
be = b"\xBE"
x  = b"\xFF"
print(hex( ord(be) ^ ord(x) ))
print(chr( ord(be) ^ ord(x) ))
print("")



print("============================")
print("           SHIFT")
print("============================")
def shift_left(num, count):
    return num << count

def shift_right(num, count):
    return num >> count

print("Original:")
print(41)
print(bin(41))
print("")
print("Shift Left by 3 (add bits and keep existing bits):")
print(shift_left(41, 3))
print(bin(shift_left(41, 3)))
print("")
print("Shift Right by 3 (get rid of rightmost bits):")
print(shift_right(41, 3))
print(bin(shift_right(41, 3)))
print("")



print("=============================")
print(" ROTATE (based on # of bits)")
print("=============================")
def rol32(num, count):
    num1 = (num << count) & 0xFFFFFFFF
    num2 = (num >> (0x20 - count)) & 0xFFFFFFFF
    return num1 | num2

def ror32(num, count):
    num1 = (num >> count) & 0xFFFFFFFF
    num2 = (num << (0x20 - count)) & 0xFFFFFFFF
    return num1 | num2

def rol8(num, count):
    num1 = (num << count) & 0xFFFFFFFF
    num2 = (num >> (0x08 - count)) & 0xFFFFFFFF
    return num1 | num2

def ror8(num, count):
    num1 = (num >> count) & 0xFFFFFFFF
    num2 = (num << (0x08 - count)) & 0xFFFFFFFF
    return num1 | num2

def rol13(num, count):
    num1 = (num << count) & 0xFFFFFFFF
    num2 = (num >> (0x0d - count)) & 0xFFFFFFFF
    return num1 | num2

def ror13(num, count):
    num1 = (num >> count) & 0xFFFFFFFF
    num2 = (num << (0x0d - count)) & 0xFFFFFFFF
    return num1 | num2

print("int is 4 bytes -> 8 bits in a bytes -> 32 bits in an int")
print("Original:")
num = 'a'
print(num)
print(ord(num))
print(bin(ord(num)))
print("")

count = 1

print("Rotate Left by 1 (32 bits; may not see all 32 bits):")
i = rol32(ord(num), count)
print(i)
print(bin(i))
print("")

print("Rotate Right by 1 (32 bits):")
i = ror32(ord(num), count)
print(i)
print(bin(i))
print("")


print("=============================")
print(" ROTATE (based on # of bits)")
print("=============================")

# Size of English Alphabet
ALPH_SIZE = 26

# In an increasing fashing, shift
def ascii_rot13(c):

    # Int representation of the char c
    i = ord(c)

    # Add 13 to the Character
    i_rot13 = i + 13

    # Lower Case Characters
    if i >= 97 and i <= 122:
        if i_rot13 > 122:
            i_rot13 = i_rot13 - ALPH_SIZE
        elif i_rot13 < 97:
            i_rot13 = i_rot13 + ALPH_SIZE

    # Upper Case Characters
    elif i >= 65 and i <= 90:
        if i_rot13 > 90:
            i_rot13 = i_rot13 - ALPH_SIZE
        elif i_rot13 < 65:
            i_rot13 = i_rot13 + ALPH_SIZE

    # Invalid Characters
    else:
        print("Not a valid ASCII character")
        return None

    # print("Original char:   " + c)
    # print("Int representation of char: %d" % i)
    # print("Rot13 char: " + chr(i_rot13))
    # print("")
    return chr(i_rot13)

print("z -> rot13 -> " + ascii_rot13("z"))
print("Z -> rot13 -> " + ascii_rot13("Z"))
print("")
