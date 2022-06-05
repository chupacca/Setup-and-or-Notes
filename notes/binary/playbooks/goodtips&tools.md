# When:
    push {r11, lr} ; lr is r14
      + The lower number register will be at a lower address (higher up the stack)
      + The bigger number register will be at a higher address (lower in the stack)
      + 14 > 11
      + $sp will now point at the top of the stack (r11 in this case)

### USEFUL TRICKS ----------------------------------------------------------

[Breaklines to Read Assembly]: nop
	#include <stdio.h>
    int main() {
       asm("nop"); //Puts a nop inst in assembly
                   //Can use this as a breakpoint
       int a = 1;
       asm("nop");
       int b = 2;
       asm("nop");
       return 0;
    }

[Hex Output]: "\xc7\x84\x04\x08"
# Use the 'printf' command to print hex
    $ printf '\x61'
        a

# Use python to provide hex arguments
    ./binary $(python -c "print '\x01' * 10")

    export VAR=$(python -c "print '\x61\x62\x63'")
    echo $VAR
      abc            ; keep in mind '\x61\x62\x63' is 'abcd' in hex


[Little Endian]: ""
 + When given a string the characters will be in order from smaller byte to bigger
 String: abcd
 Bytes:            0    1    2    3   4
 Chars of String:  a    b    c    d   e




### USEFUL TOOLS ------------------------------------------------------------

[Docker]::
# You can use docker to execute a binary if you're on mac and not linux
	+ ex) sudo docker run --rm -v $PWD:/something --security-opt seccomp=unfonfined -d --name <name> -i ctf:ubuntu19.something

--------------------------------------------------

[Hex Dump]: $ hexdump [args] <file>
	Ex) $ hexdump -v -e '"\\""x" 1/1 "%02x" ""' file.bin

--------------------------------------------------

[Hex Editors]::
	+ hexedit - a command line tool hex editor

--------------------------------------------------

[file]: $ file <binary>
	+ What type of binary
	+ What OS
	+ Wherther or not it was stripped
	 - If it says `not stripped` this will
       have symbol names (making things easier)

--------------------------------------------------

[readelf]: $ readelf -a <binary>
	+ 

--------------------------------------------------

[strings]: $ string <binary>
	+ gets strings within the binary

