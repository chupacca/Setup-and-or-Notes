### TABLE OF CONTENTS
1. Run With Arguments
2. Breaking
3. Starting Execution
4. Step Through Execution
5. Till Breakpoint / Finish Up Execution


### ================================== ###
###         Run With Arguments         ###
### ================================== ###

-----------------------------

**Run with arguments**
	(gdb) run arg1 arg2 agr3

**Run with piped arguments**
	python 
	gdb ./vuln_prog
	run < filename_with_input

**Running Code from VIM:** `:!./% GDB NOASLR`

-----------------------------


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


### ================================== ###
###              Breaking              ###
### ================================== ###

**Breaking w/ GDB**
	(gdb) break *0x1046c         ; breaking at address
	(gdb) b <function>           ; breaking at function
	(gdb) b <class>::<function>  ; break at function in a class

**List and delete breakoints**
```
	(gdb) i b     ; list breakpoints
	(gdb) d 1	  ; delete breakpoint 1
	(gdb) d 1 2   ; delete breakpoints 1 and 2
```

   _-----------------------------_
   _| Breaking w/ PWNDBG or GEF |_
   _-----------------------------_
   
**Break at next return**
	pwndbg> stepret			; pwndbg specific

**Break at next syscall**
	pwndbg> stepsyscall         ; pwndbg specific

**Break at Main**
	gef> 	entry-break		; gef specific
	pwndbg> entry    	    	; pwndbg specific



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



### ================================== ###
###         Starting Execution         ###
### ================================== ###


**Start program execution from beginning of program**
[run / r]: r


**Debug a NEW INSTANCE of the program**
[start]: start


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



### ============================== ###
###     STEP THROUGH EXECUTION     ###
### ============================== ###

-----------------------------


**Continue running until `just after the function` (in stack frame)**
[finish / fin]: fin


-----------------------------


**Backtraces (what was been executed)**
[backtrace]: bt
[where]: where
          ^seems to do the same thing

-----------------------------

**Step to the NEXT LINE of code**
     _(WILL ENTER FUNCTION)_

[stepi / s]: s <optional-number-of-steps>
 + si  -> steps through everything (goes into functions)
 + s

Examples:
```
    pwndbg> s
    pwndbg> s 5
```

-----------------------------

**Execute NEXT LINE of code**
_(WILL `NOT` ENTER FUNCTION)_

[nexti / n]: n <optional-number-of-steps>
 + ni  -> this lets you step without going into functions
 + n   -> 

Examples:
```
    pwndbg> n
    pwndbg> n 6
```

-----------------------------

**Break on the instruction after this one**
	pwndbg> stepover	    ; pwndbg specific

-----------------------------

**Next call (pwndbg specific)**
	pwndbg> nextcall

-----------------------------


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


### ============================================= ###
###     Till Breakpoint / Finish Up Execution     ###
### ============================================= ###

-----------------------------

**Continue Until ...**
 [until]: until <optional-break-point>
 + specific line-number
 + fucntion name, address
 + filename:function
 + filename:line-number

Examples:
```
    pwndbg> until main
    pwndbg> until 17
```

-----------------------------

**Continue to the end of the function**
[finish]: finish

-----------------------------

**Continues program execution after breakpoint**
[continue / c]: c <optional-repeat-count>

Examples:
```
    pwndbg> c
    pwndbg> c 7
```

-----------------------------

