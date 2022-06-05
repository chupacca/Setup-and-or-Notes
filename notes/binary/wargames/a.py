#a = [0x73, 0x73]
#b = 0x15bd3a99
#for h in a:
#    print(chr(h), end = "")
#
#print("\n")
#print(str(0x15bd3a99))


#pw = "s4òðvõôk;¹¿S=º¼c&¢¡pU"
#ds = ""
#for i in range(0, len(pw)):
#    c = pw[i]
#    sv = i<<6
#    sv += i
#    dv = ord(c) ^ sv
#    ds = ds + chr(dv)
#print(ds)

hex_pw = [0x73, 0x34, 0xf2, 0xf0, 0x76, 0x1a, 0xf5, 0xf4, 0x6b, 0x3b, 0xb9, 0xbf, 0x53, 0x3d, 0xba, 0xbc, 0x63, 0x26, 0xa2, 0xa1, 0x70, 0x55]
hexify = lambda s: [hex(ord(i)) for i in list(str(s))]

ds = ""

# works until 4 (4 is where it gets weird)
for i in range(0, len(hex_pw)):

    hex_value = hex_pw[i]
    char_value = chr(hex_value)
    #print("encrypted_char: " + char_value)

    shifted_value = i<<6
    shifted_value += i

    dv = ord(char_value) ^ shifted_value
    dv = dv & 0xFF
    #print(hex(hex_pw[i]))
    print("Encrypted Value: " + str(hex(hex_pw[i])))
    print("Decrypted Value: " + str(hex(dv)))
    #print("Decrypted Value: " + chr(dv))
    #print("Decrypted Value: " + str(hex(dv)))

    re_encrypted_value = dv ^ shifted_value
    re_encrypted_value = re_encrypted_value & 0xFF
    print("Re-encrypted: " + str(hex(re_encrypted_value)))

    ds = ds + chr(dv)
    print("===")

print ("----------")
for c in ds:
    print(str(hex(ord(c))), end=" ")
print("")
print(ds)


#for h in hex_pw:
#    c = chr(h)
#    print(c, end="")
#print("")
