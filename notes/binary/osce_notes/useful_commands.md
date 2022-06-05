### Base64 Decode
cat encoded_raw | base64 -d

### Hex to Shell
python3 -c 'import sys; sys.stdout.buffer.write(b"\xCC")' > shellcode

### Shell to Asm
ndisasm -b 32 shellcode > shellcode.asm
i
### Remove first two columns of asm so it's just assembly
awk '{$1=$2=""; print $0}' shellcode.asm | sed 's/^  //g' > shellcode_edited.asm

 + Add this to the top of the new asm file
    global _start
    _start:

### Turn assembly into object file
nasm -f elf shellcode.asm
             ^will get shellcode.o

### Turn object file into executable
ld -m elf_i386 -o key_ed shellcode.o
