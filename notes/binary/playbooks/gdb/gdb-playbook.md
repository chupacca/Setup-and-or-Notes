**Search COMMANDS & COMMAND DESCRIPTIONS**
`pwndbg> pwndbg <search_term>`
`(gdb) apropos <search_term>`


**Instruction List**
	`pwndbg> pwndbg`
	https://browserpwndbg.readthedocs.io/en/docs/
    

**Use as a Shell**
+ _pwndbg_ is in `shell mode`, so you can just _use it as a shell_
 - You can _call_ `shell` and run `exit` on that _shell_
 - `gef> shell <cmd>`
+ CLEAR SCREEN
  [pwndbg]: shell clear
  [gef]:    shell clear


**Split Screen**
[split screens]: pwndbg [must use tmux for terminal]
git clone https://github.com/jerdna-regeiz/splitmind


-------------------------------------------------------------------------


# TABLE CONTENTS
1. CONTEXT - command (pwndbg)
2. objdump one function
3. Calculate Bytes Between 2 Addresses
4. Use PRINT to convert HEX to Decimal
5. Stack Trace when SIG Happens
6. Jump to Address/Function
7. Set Values
8. GDB OUT OF THE BOX


-------------------------------------------------------------------------


# 1. CONTEXT - command (pwndbg)

**Reprint Pwndbg/GEF Output from every step**
[pwndbg]: context
[gef]:    context

**Only Print a Subset of Context**
+ `pwndbg> set context-sections code` ; only prints the source code (if it's available)


-------------------------------------------------------------------------


# 2. objdump one function
	$ objdump -d filename | sed '/<functionName>:/,/^$/!d'


-------------------------------------------------------------------------


# 3. Calculate Bytes Between 2 Addresses

**Example Output**
```
wdb> x/16wb g_posts
0x602180: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
0x602188: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
```

**Words**
+ `address1 - address2 + 8`
+ _8 cause gdb usually puts_ **8 bytes per row**

+ Examples:
 - Example: `0x602188 - 0x602180 = 0x08`     ---> **8 bytes NOT INCLUDING 0x602188's byte**
 - Example: `0x602188 - 0x602181 + 8 = 0x0f` ---> **7 bytes NOT INCLUDING 0x602188's byte**


--------------------------------------------------------------------------


# 4. Use PRINT to convert HEX to Decimal

```(gdb) p/d 0x15bd3a99
$1 = 364722841
```
```python
print(str(0x15bd3a99))

Output:
364722841
```


--------------------------------------------------------------------------


# 5. Stack Trace when SIG Happens

+ I can use the `frame` command or `f` for short to example the stack
```Example
Program received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
51      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
────────────────────────────────────────────────[ BACKTRACE ]────────────
 ► f 0   0x7ffff7a5204a raise+202
   f 1   0x7ffff7a530f5 abort+3570
   f 2   0x7ffff7a93f07 __libc_message+599
   f 3   0x7ffff7a9b2aa
   f 4   0x7ffff7a9ccb4 _int_free+948
   f 5         0x400a22 main+603
   f 6   0x7ffff7a3e037 __libc_start_main+231                                                                 │
───────────────────────────────────────────────────────────────────────────
```
```pwndbg> f 4   ; I'm getting the 4th frame from the stack trace
#4  0x00007ffff7a9ccb4 in _int_free (av=0x7ffff7dd0b60 <main_arena>, p=0x603000, have_lock=0) at malloc.c:4266
4266              malloc_printerr ("double free or corruption (fasttop)");    
```
```pwndbg> context code  ; do this if you can because it shows last line printed in code
                         ;   i.e. the last call made to it
──────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────
In file: /home/test/heap/heaplab/.glibc/glibc_2.30_no-tcache/malloc/malloc.c
   4261     if (SINGLE_THREAD_P)                                  
   4262       {
   4263         /* Check that the top of the bin is not the record we are going to
   4264            add (i.e., double free).  */
   4265         if (__builtin_expect (old == p, 0))
 ► 4266           malloc_printerr ("double free or corruption (fasttop)");
   4267         p->fd = old;
   4268         *fb = p;
   4269       } 
   4270     else
   4271       do
```


-------------------------------------------------------------------------

# 6. Jump to Address/Function
```
j LINENUM
j *Address

OR

set $pc = 0xffffff
```


-------------------------------------------------------------------------


# 7. Set Values

### Set variable
	gdb> set {int}0x83040 = 4
	gdb> set var idx = 1

### Set register
	gdb> set $r3=0xa3b4c5

### Set memory
	gdb> set *0x7efff4b4=0x01044c

### Tested
	gdb> p $r3 = 1



-------------------------------------------------------------------------


# 8. GDB OUT OF THE BOX

``` (gdb)
    b *(main+33)  ; allows method names w/ offsets

    # To see registers and assembly
    $ gdb -tui <binary>
    (gdb) layout asm
    (gdb) layout regs
    
    # Set Assembly to Intel View
    (gdb) set disassembly-flavor intel
    (gdb) layout asm

    # Make gdb do things after each step
     (gdb) define hook-stop
     > python print '---------------'
     > info registers  # prints registers
     > python print '---------------'
     > x/24wx $esp     # prints stack
     > python print '---------------'
     > x/5i $eip       # prints instructions
     > python print '---------------'
     > end
```

