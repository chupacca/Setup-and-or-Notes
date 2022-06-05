

#seh is 8bytes

# This structure ( also called a SEH record) is 8 bytes and has 2 (4 byte) elements :
> a pointer to the next exception_registration structure
  (in essence, to the next SEH record, in case the current handler
  is unable the handle the exception)

> a pointer,  the address of the actual code of the exception handler
  (SE Handler)


# Intel machines
> When looking at the disassembled SEH code, you will see an
  instruction to move `DWORD ptr` from `FS:[0]`

> Ensures that the exception handler is set up for the thread and will be able to catch errors when they occur

> Opcode for this instruction: `64A100000000`
> Bottom of SEH Chain: `FFFFFFFF`

> If you CAN'T FIND this opcode, the application/thread may
  NOT have exception handling at all


# Changes in Windows XP SP1 with regards to SEH, and the impact of GS/DEP/SafeSEH and other protection mechanisms on exploit writing.

## XOR
> In order to be able to build an exploit based on SEH overwrite, we will need to make a distinction between Windows XP pre-SP1 and SP1 and up
> Since Windows XP SP1, before the exception handler is called, all registers are XORed with each other
 + Thus making them all contain 0x00000000

 + This means you WON'T find a reference to your payload in one of the registers
  - `jmp esp` : This means having EIP point to an insturctin that executes `jmp esp` WON'T work
  - !!!!!!!!!!!!!!!!!!!!!!

 + In other words, maybe you’ll see that one or more registers point at your payload at the first chance exception
  - BUT when the EH kicks in, these registers are cleared again 
    (so you cannot jump to them directly in order to execute your shellcode)

 + There is a way around the XOR 0x00000000 protection and the SafeSEH protections
  - Since you cannot simply jump to a register (because registers are xored), a call to a series of instructions in a dll will be needed
     ^ look at `osce/seh/'SEH Based Exploits.pdf'`


## DEP & Stack Cookies

> On top of that, Stack Cookies (via C++ compiler options) and DEP (Data Execution Prevention) were introduced (Windows XP SP2 and Windows 2003)
 + I will write an entire post on Stack cookies and DEP
   ^osce/'Bypass Stack Cookies, SafeSeh, SEHOP, HW DEP and ASLR.pdf'
 + In sort, you only need to remember that these two techniques can make it significantly harder to build exploits.


## SafeSEH
> Some additional protection was added to compilers, helping to stop the abuse of SEH overwrites
> This protection mechanism is active for all modules that are compiled with /safeSEH


## Windows 2003
> Under Windows 2003 server, more protection was added
> I’m not going to discuss these protections in this post (check tutorial series part 6 for more info)
> because things would start to get too complex at this point
> As soon as you mastered this tutorial, you will be ready to look at tutorial part 6 :-)
   ^osce/'Bypass Stack Cookies, SafeSeh, SEHOP, HW DEP and ASLR.pdf'


