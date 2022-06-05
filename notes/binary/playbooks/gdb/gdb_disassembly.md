**Reprint the GDB summary**
	`gdb> context !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!`
-------------------------------------------------------------------------

### ============================= ###
###          Disassembly          ###
### ============================= ###

### 1. (gdb)
**See the assembly instrucntions**
	(gdb) disassemble <function>
	(gdb) disassemble *<address>

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

   _============_
   _PWNDBG & GEF_
   _============_

### 2. pwndbg
**PWNDBG SPECIFIC COLOR DISASSEMBLY (COLOR INSTRUCTIONS OF FUNCTION)**
	https://gef.readthedocs.io/en/master/commands/capstone-disassemble/
    https://browserpwndbg.readthedocs.io/en/docs/
```
	pwndbg>	nearpc		; PWNDBG SPECIFIC; reprint color dissasembly from summary !!!
	pwndbg> u                 ; does the same as nearpc
	pwndbg> u <address>       ; prints color disassembly at a specific address
	pwndbg> u <function>      ; prints color disassembly at a specific function
	pwndbg> u <function> [#]  ; prints # lines of color disassembly of function!!!

    = = = = = = = = = = = = = = = =

	gef> cs main
	gef> cs main length=20
	gef> cs main nb_prev=3
```


### 3. GEF
	The functions command will list all of the convenience functions provided by GEF.
		$_bss([offset])   -- Return the current bss base address plus the given offset.
		$_got([offset])   -- Return the current bss base address plus the given offset.
		$_heap([offset])  -- Return the current heap base address plus an optional offset.
		$_pie([offset])   -- Return the current pie base address plus an optional offset.
		$_stack([offset]) -- Return the current stack base address plus an optional offset.

-------------------------------------------------------------------------
