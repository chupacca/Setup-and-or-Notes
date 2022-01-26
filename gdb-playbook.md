**Reprint Pwndbg/GEF Output from every step**
```
[pwndbg]: context
[gef]:    context
```

**Search `COMMANDS` and `CMD DESCRIPTIONS`**
```
(gdb) apropos <search_term>
```

**Clear the Screen**
```
[pwndbg]: shell clear  
[gef]:    shell clear  
```

**GDB OUT OF THE BOX**
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


-------------------------------------------------------------------------


### PRINT `STACK VALUES` - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
gef>    dereference <addressORregister>   ; GEF SPECFIFIC; get the stack dump from gdb summary     
pwndbg> telescope   <addressORregister>   ; PWNDBG specific; get the stack dump from gdb summary     
```

**Dump `HEX VALUES` from `STACK`**
```
[pwndbg]: hexdump
[pwndbg]: hexdump <addressORregister>
[gef]:    hexdump
[gef]:    hexdump <addressORregister>
```


```
  (gdb) =============================
	(gdb) x/10x $sp             ; see first 10 HEX INTEGER from the STACK
	(gdb) x/u   $esp+<offset>   ; see UNSIGNED INTEGERS from the STACK at an offset
	(gdb) x/4b  $esp+<offset    ; see first 4 BYTES from the STACK at an offset
	(gdb) x/4c  $esp+0x5c       ; see firtt 3 CHARS from the STACK at an offset of `0x5c`
	
	(gdb) x10s  <address>  ; see top 10 strings from that address
	(gdb) x10i  <address>  ; see top 10 instructions from that address

  GEF ================================
	gef> dereference $sp             ; GEF SPECFIFIC; get the stack dump from gdb summary !!!!!!!!!!!!!!!
	gef> dereference $sp [#]         ; GEF SPECFIFIC; print that many elements from stack !!!!!!!!!!!!!!!
	gef> dereference $sp $fp-$sp  	 ; [ARM] trick to print stack frame
	gef> dereference $esp $ebp-$esp  ; [x86] trick to print stack frame

  PWNDBG =============================
	pwndbg> telescope $sp            ; PWNDBG specific; get the stack dump from gdb summary !!!!!!!!!!!!!
	pwndbg> telescope $sp [#]        ; PWNDBG specific; print that many elements from stack !!!!!!!!!!!!!
	pwndbg> telescope $sp $fp-$sp  	 ; [ARM] trick to print stack frame
	pwndbg> telescope $esp $ebp-$esp ; [x86] trick to print stack frame
```



### DISASSEMBLY / INSTRUCTION VIEW - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
gef>    cs <target>	 ; GEF & PWNDBG; includes rwx attributes
pwndbg> u <target> 	 ; GEF & PWNDBG; includes rwx attributes
```

``` (gdb)
    (gdb) disassemble <function>

	https://gef.readthedocs.io/en/master/commands/capstone-disassemble/
	gef> cs main !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	gef> cs main length=20 !!!!!!!!!!!!!!!!!!!!!!!!!
	gef> cs main nb_prev=3 !!!!!!!!!!!!!!!!!!!!!!!!!

	pwndbg>	nearpc		; PWNDBG SPECIFIC; reprint color dissasembly from summary !!!!!!!!!!!!!!!!!
	pwndbg> u                 ; does the same as nearpc
	pwndbg> u <address>       ; prints color disassembly at a specific address
	pwndbg> u <function>      ; prints color disassembly at a specific function
	pwndbg> u <function> [#]  ; prints # lines of color disassembly of function!!!!!!!!!!!!!!!!!!!
```


### REGISTERS- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
pwndbg> regs
gef> registers
```

``` (gdb)
    (gdb) info registers
```


-------------------------------------------------------------------------

### Register information
```
	(gdb) info registers		; see registers
	(gdb) x/s $r3			; see string in R3 register [that's an ARM arch register]
	
	gef> registers			;GEF SPECIFIC (is similar to the summary at every step) 
	
	pwndbg> reg    			;PWNDBG SPECFIFIC                                       
	pwndbg> xpsr			;pwndbg specific; see ARM/xPSR/CPSR register
```
	
**See content of register**
	


### VARIABLES- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```(gdb)
   (gdb) info args       ; arguments in current fucntion
   (gdb) info locals     ; local variables
   (gdb) info variables  ; all variables
```


### STACK FRAME THAT CALLED THIS ONE - - - - - - - - - - - - - - - - -
```
   pwndbg> up
```

### Sections View- - - - - - - - - - - - - - - - - - - - - - - - - - -
```
[gdb]:    info files
[gef]:    xfiles
[pwndbg]: ???
```



### View Contents - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
gef>    xinfo <addressORregister>   ; gef & pwndbg; gives info about that part of memory
pwndbg> xinfo <addressORregister>   ; gef & pwndbg; gives info about that part of memory
```

```
* By default just running `xinfo` gets information of the binary
```


### View mapped pages - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
gef>    vmmap			; GEF & PWNDBG; includes rwx attributes
pwndbg> vmmap			; GEF & PWNDBG; includes rwx attributes
```

``` (gdb)
	(gdb) info proc map
	
	Start      End        Offset     Perm Path
```



-------------------------------------------------------------------------

### USEFUL PWNDBG / GEF CMNDS

[split screens]: pwndbg [must use tmux for terminal]     
git clone https://github.com/jerdna-regeiz/splitmind     

### instruction list
	pwndbg> pwndbg      
	https://browserpwndbg.readthedocs.io/en/docs/    

**objdump one function**
`$ objdump -d filename | sed '/<functionName>:/,/^$/!d'`

**GEF AND PWNDBG (HAS GEF's VIEW)**
```
	Set gdbinit to look for pwndbg    
	The run: $ gdb <binary> --command /location/.gdbinit-gef.py    
```

-------------------------------------------------------------------------


### Quick tips other useful gdb commands


[Use as shell]:    
* _pwndbg_ is in `shell mode`, so you can just _use it as a shell_    
 - You can _call_ `shell` and run `exit` on that _shell_    
 
`gef> shell <cmd>`    


[Jump to Address/Function]:    
```
j LINENUM
j *Address

OR

set $pc = 0xffffff
```

-------------------------------------------------------------------------

### Breaking

### GEF/PWNDBG Break at Main
	gef> 	entry-break		;gef specific
	pwndbg> entry    		;pwndbg specific

### Breaking at address
	gdb> break *0x1046c

### Break at function
	gdb> b <function>

### Break at a function in a class
	gdb> b <class>::<function>

### Break at multiple points and continue
```
	gdb> break main
	gdb> start
	gdb> run
	gdb> break *0x10468
	gdb> break *0x10470
	gdb> c
	gdb> c
```
	
### Break on the instruction after this one
	pwndbg> stepover	    ; pwndbg specific

### Break at next return 
	pwndbg> stepret			; pwndbg specific

### Break at next syscall
	pwndbg> stepsyscall     ; pwndbg specific




### List and delete breakoints
```
	gdb> i b     ;list breakpoints
	gdb> d 1	 ;delete breakpoint 1
	gdb> d 1 2	 ;delete breakpoints 1 and 2
```
	
-------------------------------------------------------------------------

### Code flow (alter code flow)
```
	inst: [fp, #-8]
	gdb> x $fp-8    		  ; let's say the address is 0x7efff49c
	gdb> u <target-function>  ; let's say the address for target-function is 0x01047c
	gdb> set *0x7efff49c=0x01047c
```

-------------------------------------------------------------------------

### Execution

**Run with arguments**
`gdb> run arg1 arg2 agr3`


**Run with piped arguments (when code uses gets)**
```
	python 
	gdb ./vuln_prog
	run < filename_with_input
```
				 
**Run with arguments (code accepts command line arguments)**
     `gdb --args <binary> arg1 arg2 arg3`    

  [Example]: gdb --args format0 $(python -c 'print "%64d\xef\xbe\xad\xde"')    
   
**Running multiple breakpoints**
```
	gdb> break main
	gdb> run [args]
	gdb> b <somewhere>
	gdb> c
```
	
-------------------------------------------------------------------------

### Function
	
**List functions**
```
	The functions command will list all of the convenience functions provided by GEF.
		$_bss([offset]) -- Return the current bss base address plus the given offset.
		$_got([offset]) -- Return the current bss base address plus the given offset.
		$_heap([offset]) -- Return the current heap base address plus an optional offset.
		$_pie([offset]) -- Return the current pie base address plus an optional offset.
		$_stack([offset]) -- Return the current stack base address plus an optional offset.
```

-------------------------------------------------------------------------

### HEAP

**Arenas (when multithreading)**
	gef> heap arenas

**Chunk**
	gef> heap chunks <location>

-------------------------------------------------------------------------

### Secrity configurations
```
	gef> checksec	; checks secruity configurations
	gef> aslr		; checks if aslr is enabled
	gef> canary		; checks canary
```
	
-------------------------------------------------------------------------

### Set variable
```
	gdb> set {int}0x83040 = 4
	gdb> set var idx = 1
```
	
**Set register**
```
	gdb> set $r3=0xa3b4c5
```
	
**Set memory**
```
	gdb> set *0x7efff4b4=0x01044c
```

**Tested:**
```
	gdb> p $r3 = 1
```
	
-------------------------------------------------------------------------

### Shell Commands
```
	gef/pwndbg> shell <command>
```
	
-------------------------------------------------------------------------

### Stepping quickly
```
	gdb> n        ;**(WON'T ENTER FUNCTION)**
	gdb> s        ;**(WILL ENTER FUNCTION)**
```
	
### Next call (pwndbg specific)
```
	pwndbg> nextcall
```


