

-------------------------------------------------------------------------------

# Sections
+ `.text`   -> _this section holds executable code_
 - Points to `ROM - read only memory`

+ `.rodata` -> _read only data section (such as strings)__
+ `.data`   -> _Initialized data here (usually)_

    - marked by `PROGBITS`
    - _bits_ of program data in the `ELF` file that the loader needs to
       read out into memory for you
 

+ `.ebss`   -> _Uninitialized Variables (usually)_
+ `.bss`    -> _Uninitialized Variables (usually)_

 - guranteed to be all zeros when the program is loaded into memory
 - data doesn't have to bin the ELF file on disk
 - instead the loader knows from the section headers how much to allocate
     to `.bss` and simply zero it out
 - marked by `NOBITS`


-------------------------------------------------------------------------------


# PLT
 + Writeable array of _function pointers_
  - every _funtion_ call is in _external library_ (like libc)
  - Does lazy linking
   * address is _only resolved when it's first called_
  
 + `fini_array` is another _array of function pointers_
  - each funtion in array is called _as fucntion exits_
  - if program exits this will be triggered


-------------------------------------------------------------------------------

# Decompiler / Disassembler Formatting

1. `[register].q` == `qword[rsp+<some_value>], rax`
  + _pointer / quadword at address in register_
  + Example: `[rdi].q = 0` ---> `*puVar4 = 0` (you're dereferncing a pointer)
  
2. **BINJA MLIL - Middle**
  + `if (rcx != 0) then 15 else 16 @ 0x401241` --> `for(lVar3 = 0x10; lVar != 0; lVar3 = lVar + -1)`
   - essentially a for loop from 0-15 which makes for 16 loops
   
  + `zx.q` --> _Zero-Extend-Quad-Word_

-------------------------------------------------------------------------------

# Register

1. `RCX` - often used as a counter/incrementer **when in loop**

-------------------------------------------------------------------------------

# Things to Look For

1. Look things that **set the RAX / EAX register**
  + Examples
   - `mov eax, 0x0` 
   - `mov eax, 0x1`

  + Often the _return value_ is stored in the `eax` register
   - This can be what:
    * What _THIS function is returning_ (the function currently looking at)
        OR
    * The _return value_ of _another function_ that is called


2. Conditional jump like `je`, `jbe`, `jne`, etc
  + This way you can see what the variables are

  + _Set a breakpoint_ right before so you can
    examine values in _registers or stack_
    
    
3. `**void pointers` - _double void pointer_ often identify **structures**


4. **A bunch of hex f values** like `0xffffffffffffffff --> -1`
  + Remember _2's complement_
  
  
5. **+8 OR -8 on register/pointer in a loop**
  + Probably looping through elements (probalby char cause 8 bit in a byte)
    in a list



 
-------------------------------------------------------------------------------

**div** instruction
```aldeid.com
Assembly

mov edx, 0        ; clear dividend
mov eax, 0x8003   ; dividend
mov ecx, 0x100    ; divisor
div ecx           ; EAX = 0x80, EDX = 0x3

Python

>>> hex(0x8003 / 0x100)
'0x80'
>>> hex(0x8003 % 0x100)
'0x3'

```

**sete / setz**
+ Sets destination to `1` if _zero flag is set_
 - `0` otherwise



-------------------------------------------------------------------------------

# Registers
```
64-bit register | Lower 32 bits | Lower 16 bits | Lower 8 bits
==============================================================
rax             | eax           | ax            | al
rbx             | ebx           | bx            | bl
rcx             | ecx           | cx            | cl
rdx             | edx           | dx            | dl
rsi             | esi           | si            | sil
rdi             | edi           | di            | dil
rbp             | ebp           | bp            | bpl
rsp             | esp           | sp            | spl
--------------------------------------------------------------
r8              | r8d           | r8w           | r8b
r9              | r9d           | r9w           | r9b
r10             | r10d          | r10w          | r10b
r11             | r11d          | r11w          | r11b
r12             | r12d          | r12w          | r12b
r13             | r13d          | r13w          | r13b
r14             | r14d          | r14w          | r14b
r15             | r15d          | r15w          | r15b
```

# Calling Conventions

```x86_64-Linux
1st arg: rdi
2nd arg: rsi
3rd arg: rdx
4th arg: rcx
5th arg: r8
6th arg: r9

Result: rax
```
```Stack_Arguments
<stack arguments>    | ($rbp + 8) + ?
  + If too many arguments, those extra arguments will be referenced as like a 
    stack argument
<return address>     | $rbp + 8
<saved base pointer> | $rbp points here
<local variables>    | ($rbp - 8) - ?
```


--------------------------------------------------------------

**Local Variables**
+ Usually accessed as a _negative offset from_ `rbp`
 - Example: `mov qword [rbp-0x8], rax`

**Initializing Variable**
```uint64_t foo = 0x5151515151515151;
mov     rax, 0x5151515151515151
mov     qword [rbp-0x8], rax
```

**Initializing Buffer**
```char buffer[32] = {};
mov     qword [rbp-0x30], 0x0
mov     qword [rbp-0x28], 0x0
mov     qword [rbp-0x20], 0x0
mov     qword [rbp-0x18], 0x0
```

**After main ends**
+ _returns_ to `libc_start_main`
