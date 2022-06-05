
# Set variable
	gdb> set {int}0x83040 = 4
	gdb> set var idx = 1

# Set register
	gdb> set $r3=0xa3b4c5

# Set memory
	gdb> set *0x7efff4b4=0x01044c

# Tested:
	gdb> p $r3 = 1


[info proc map]: i



-----------------------------------------------------------------
# MODIFYING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------------------

[set]: Set a values/settings in the binary
 + `(gdb) set $eax=0`

-----------------------------

 + `(gdb) set disassembly flavor intel`
 > This sets the disassembly to look like intels



-----------------------------------------------------------------
# PROCESS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------------------

### Attaches GDB to a running process
[attach]: attach <pid>

Examples:
    `pwndbg> attach 1257`

-----------------------------

### After attaching to the process, this detaches it from that process
[detach]: detach

-----------------------------

### Forcibly terminate a debugging process
[kill]: kill

-----------------------------

# Shell
	pwndbg is in shell mode, so you can just use it as a shell
	`gef> shell <cmd>`

   **Clear screen**
	`gef> shell clear`
	`pwndbg> shell clear`


# Instruction List
	`pwndbg> pwndbg`
	https://browserpwndbg.readthedocs.io/en/docs/


# objdump one function
	$ objdump -d filename | sed '/<functionName>:/,/^$/!d'


# GEF AND PWNDBG (HAS GEF's VIEW)
	Set gdbinit to look for pwndbg
	The run: $ gdb <binary> --command /location/.gdbinit-gef.py
 

-------------------------------------------------------------------------

# Search based on keyword
	`gdb> apropos <search term>`

-------------------------------------------------------------------------

# Code flow (alter code flow)
```
	inst: [fp, #-8]
	(gdb) x $fp-8    		   ; let's say the address is 0x7efff49c
	(gdb) u <target-function>  ; let's say the address for target-function is 0x01047c
	(gdb) set *0x7efff49c=0x01047c
```


-------------------------------------------------------------------------





