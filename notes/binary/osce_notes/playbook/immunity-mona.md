# HOW TO mona CORRECTLY!!!!
[Downlaod zip from]: https://github.com/corelan/mona
+ put mona.py in `C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands`

--------------------------------------------------------------

[Go back to CPU window]: Alt+C

[Finding a useful breakpoint]:
 + Just run an overflow until you trigger the EIP overwrite
 + After the crash, right click the ESP register and do `Follow in dump`

 + Do `!mona jmp -r esp`   <or wherever you want eip to point to>
 + Set the breakpoint where the `jmp esp` is from what mona gave you


--------------------------------------------------------------

[A quick note about symbol files…]:
 + it’s especially helpful to load the appropriate symbol files when debugging Windows applications 
 + they provide useful, descriptive information for functions, variables, etc.
 + You can do so within WinDbg by navigating to 
   `File –> Symbol File Path…`
 + Follow the instructions found here:
    http://support.microsoft.com/kb/311503
 + You can also load symbol files in Immunity by navigating to:
   `Debug –> Debugging Symbol Options`

--------------------------------------------------------------

[Useful TIPS]:
 + If you right click and address (top left pane) and go to 
   `Follow in dump`, the bottom left pane will be at that address

 + Typing `cpu` in the command terminal at bottom will return
   to the 4 pane with cpu info (insturction, stack, registers, etc.)

 + In the registers section, if you double click the address
   the top left pane will jump to that address

--------------------------------------------------------------

[DLL]:
 + You can view them in Immunity in the Memory view:
   `(Alt+M)`
 + If you want to only view the DLLs you can select the Executable Module view
   `(Alt+E)`

--------------------------------------------------------------

[Useful OS/System Modules]:
 + ntdll
 + user32

--------------------------------------------------------------

[Shortkeys]:

+ `Ctrl+F2` RESTARTS the program

+ `F3` to Open
+ `F9` to run
 - `F7` step into
 - `F8` step over
+ `F2` for breakpoint

+ `Ctrl+F1` to Attach
+ `Alt+X` to Exit
+ `Ctrl+G` to go to a position
 - (make sure you click the upper left pane you go to insctruction)
  * good for when putting in eip register to set breakpoint
 - double click address to make a break point


---------------------------------------------------------
# Mona --------------------------------------------------
---------------------------------------------------------


## DO AFTER EACH COMMAND - - - - - - - - - - - - -

[Just run moan]: !mona
 * If you don't you won't see the results
 * Alternativey, you can just minimize the sub-window you're on
   - The 2nd highest minimize on the top right


## Then run other commands - - - - - - - - - - - -

[Find jmp to esp]: !mona jmp -r esp
 * Then do `!mona`, scroll up, observe results
 * Look for `jmp esp` that has ascii:
    Ex: `0x62501203 :  jmp esp | ascii`


## Useful commands ---------------------------------------

[ACL / Access Control Lists]:
 * pageacl / pacl :  Show ACL associated with mapped pages


[Bad Charachter Discovery Help]:
 * bytearray / ba : create a byte array, can be used to find
                      bad characters

[Calculate / Convert]:
 * assemble / asm : convert instruction to opcode
                    (separate multiple instructions with #)
 * offset : calculate number of bpytes b/w 2 addresses
 * info : Show info of a given adddress in the context of the app


[EggHunter]:
 * egghunter / egg : Create egghunter code


[Find]:
 * find / f          : Find bytes i memory; Find opcode
 * findmsp / findmsf : Find cyclic pattern in memory
 * findwild / fw     : find instructions in memory, accepts wildcards
 * fwptr / fwp       : find writeable pointers that get called

 * peb : Show location of PEB
 * teb : Show TEB related information


[Find Ptr/Pointer]:
 * ropfunc : Find pointers to pointers (IAT) to interesting
              functions that can be used in ROP chain


[Gadgets]:
 * jseh : Find gadgets that can be used to bypass SafeSEH
 * rop     : Finds gadgets that can be used in a ROP exploit
 * ropfunc : Find pointers to pointers (IAT) to interesting
               functions that can be used in ROP chain

 * jmp / j : Find pointers that will allow you to jump to a register


[Info]:
 * info : Show info of a given adddress in the context of the app


[Modules]:
 * modules / mod : Show all loaded modules and properties
 * noaslr        : Show modules WITHOUT aslr
 * nosafeseh     : Show modules that are NOT safeseh protected
 * nosafesehaslr : Show modules that are NOT safeshe protected and
                     WITHOUT aslr


[SEH]:
 * seh : Find pointers to assist with SEH overwrite exploits
 * sehchain / exchain :  Show the current SEH chain
 * jseh : find gadgets that can be used to bypass safeseh
 * nosafeseh     : Show modules that are NOT safeseh protected
 * nosafesehaslr : Show modules that are NOT safeshe protected and
                     WITHOUT aslr

 * bpseh / sehbp : Set breakpoint on all current SEH Handler
                     function pointers


[Stack]:
 * stacks     : Show all stacks for all threads
 * stackpivot : Find stackpivots (move stackpointer to controlled area)


[Strings]:
 * string / str : Read or write a string from/to memory 





 


