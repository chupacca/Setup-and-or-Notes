# TABLE OF CONTENTS
1. Variables
2. Stack
3. Info On Something (Info Commands)
4. Registers
5. Other


### ========================================== ###
###                 VARIABLES                  ###
### ========================================== ###

**Arguments of the Current Stack Frame**
   (gdb) info args

**Local Variables**
   (gdb) info locals

**Global & Static Variable Names**
   (gdb) info variables



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

   _PWNDBG / GEF_

**Display Arguments/Variable Names**
[display]: display <expression>

```Examples:
        pwndbg> display argv[i]
        2: argv[i] = 0xbffff204 "/home/bazis/test"
```


**Information at an Address**
[xifno]: xinfo <address>
[xifno]: xinfo <function>
[xifno]: xinfo $<register>


**Reprint the GDB summary**
	pwndbg> context
    gdf> context


-------------------------------------------------------------------------
-------------------------------------------------------------------------


### ================================= ###
###               STACK               ###
### ================================= ###


**Print STRING from a POINTER on the stack**
    x/s <address>
    x/s *($<register>-<offset>)
    x/s *($rbp-0x18)
    x/s $rdi


**Print INTEGER on stack**
  x/wd $rbp-0x4
  x/1wd $rbp-0xc
  x/1wd <address>
  x/1wd $<register>-<offset>


**Print ADDRESS in register**
  p/g $<register>
  p/g $<ebp>
  p/gx $<register>
  p/gx $<ebp>

  pwndbg> dq <address>    ; dump quadword
  (gdb) x/8b <address>    ; dump 8bytes (quadword)


**Print a specific register**
  p $<register>
  p $rsi


**STACK FRAME THAT CALLED THIS ONE**
	`pwndbg> up			;  pwndbg specfific`


**Stack Frame**
```
	(gdb) x/10x $sp  		 ;see top 10 elements of the stack

	gef> dereference $sp     ; GEF SPECFIFIC; get the stack dump from gdb summary !!!!!!!!!!!!!!!
	gef> dereference $sp [#] ; GEF SPECFIFIC; print that many elements from stack !!!!!!!!!!!!!!!

	pwndbg> telescope $sp     ; PWNDBG specific; get the stack dump from gdb summary !!!!!!!!!!!!!
	pwndbg> telescope $sp [#] ; PWNDBG specific; print that many elements from stack !!!!!!!!!!!!!
```

+ Stack frame from frame pointer to stack points
```
	pwndbg> telescope $sp $fp-$sp  	; pwndbg specific 
	pwndbg> stack 						; see stack
```



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


**(gdb) DISPLAY Memory Contents**
[x]: x/<count><format><unit>
 + x <address expression>
 + x /<format> <address expression>
 + x /<length> <format>

	(gdb) x10s  <address>  ; see top 10 strings from that address
	(gdb) x10i  <address>  ; see top 10 instructions from that address
	(gdb) x/10x <address>  ; see top 10 hex from that address
	(gdb) x/10u <address>  ; see top 10 usigned integers from that address
	(gdb) x/10c <address>  ; see top 10 characters from that address

   _FORMAT              |  UNIT_
```___________________________________________________
    x – Hexadecimal     |  b – bytes
    d – decimal         |  h – half words (2 bytes)
    i – instructions    |  w – words (4 bytes)
    t – binary (two)    |  g – giant words (8 bytes)
    o – octal           |
    u – unsigned        |
    s – string          |
    c – character       |
```


**PRINT**
[printing]: use the print command to print values
 + print *argv
 + print argv[i]

```Examples:
    (gdb) print argv[i]
      $2 = 0xbffff204 "/home/bazis/test"
    (gdb) print /a argv[i]
      $3 = 0xbffff204
    (gdb) print /s argv[i]
      $4 = 0xbffff204 "/home/bazis/test"
    (gdb) print /c argv[i]
      $5 = 4 '\004'
    (gdb) print *argv
      $6 = 0xbffff204 "/home/bazis/test"
```


-------------------------------------------------------------------------
-------------------------------------------------------------------------


### ========================================== ###
###     Info On Something (Info Commands)      ###
### ========================================== ###

  _------------------_
   _| Info Commands |_
  _------------------_

**Security configurations**
	gef> checksec	; checks secruity configurations
	gef> aslr		; checks if aslr is enabled
	gef> canary	; checks canary


**Frame Info**
   (gdb) info frame
   (gdb) info frame <#>   ; select a frame on the call stack for inspection


**Function(s) Info**
[info functions]: info functions <optional-regex>
+ If regex is specified, show matching ones


**Gives address/expression that will be searched for a symbol**
[info symbol]: info symbol <address-OR-function>

```Examples:
    pwndbg> info symbol 0x80483f0
    pwndbg> info symbol $pc
```


**Displays the The addresses and sizes of all the program (stac/heap/libraries/etc.)**
     `gdb> info proc map`


**With GEF, you can get enhanced version**
     `gef> vmmap`


-----------------------------


**View mapped pages**
	(gdb) info proc map
	gef> vmmap				; GEF & PWNDBG; includes rwx attributes
	Start      End        Offset     Perm Path

**Sections View (gef)**
	gdb> info files
	gef> xfiles			; GEF SPECIFIC


**Get info on a certain target (such as registers)**
[info]: info <what-you-want-info-on>
 + <pwndbg info <what-i-want-to-see> 

[info breakpoints]: i b
Examples:
```
    pwndbg> info registers
    pwndbg> info registers <specific-register>
    pwndbg> info proc map
    pwndbg> info files
```


-------------------------------------------------------------------------
-------------------------------------------------------------------------


### ================================= ###
###             REGISTERS             ###
### ================================= ###
 
**Register information**
```
	gdb> info registers
	gef> registers			; GEF SPECIFIC (is similar to the summary at every step)
	pwndbg> regs    		; PWNDBG SPECFIFIC
	pwndbg> xpsr			; pwndbg specific; see ARM/xPSR/CPSR register

	pwndbg> regs eflags     ; get a sane version pf the eflags register
```

**See content of register**

	gdb> x/s $r3			; see string in r3 register


```Register_Info
     $rax -- References full 64 bit register
     $eax -- References lower 32 bits of $rax
     $ax  -- References lower 16 bits of $rax
     ----------------------------------------
     $ah  -- References higher 8 bits of $ax
     $al  -- References lower  8 bits of $ax
```
```Register_View
     info registers
```

* `$` symbol before the register if using _out of the box (gdb) commands_

1. See address value: `x/g $<register>`
2. See a single int value in stack example:
  + `x/1wd $rbp-<offset>`
  + Example: `x/1wd $rbp-0xc`


-------------------------------------------------------------------------
-------------------------------------------------------------------------


### ================================= ###
###               OTHER               ###
### ================================= ###

**Info About Part of Memory**
   gef> xinfo <address>  ; GEF & PWNDBG; gives info about that part of memory
   
   
**Hex Values**
	pwndbg/gef> hexdump [register/address]


### Sections View- - - - - - - - - - - - - - - - - - - - - - - - - - -
[gdb]:    info files
[gef]:    xfiles
[pwndbg]: ???



### View Contents - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**gef>    xinfo <addressORregister>   ; gef & pwndbg; gives info about that part of memory**
**pwndbg> xinfo <addressORregister>   ; gef & pwndbg; gives info about that part of memory**

```
* By default just running `xinfo` gets information of the binary
```



### View mapped pages - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**gef>    vmmap			; GEF & PWNDBG; includes rwx attributes**
**pwndbg> vmmap			; GEF & PWNDBG; includes rwx attributes**


``` (gdb)
	(gdb) info proc map
	
	Start      End        Offset     Perm Path
```


-------------------------------------------------------------------------
-------------------------------------------------------------------------

