# TABLE OF CONTENTS
1. Hot Keys In Visual Mode
2. Setting Up Debugging Mode
3. Things to do in Visual Mode while Debugging
4. Quick Useful Commands while in Visual Mode
5. Use menu (file,settings,edit,etc)
6. Commands while in Visual Mode


#  DEBUGGING


**===== 1. Hot Keys In Visual Mode =====**

```
   step:        s / ds / F7;
   
   breakpoint:  db
   
   continue:    dc / F9
   
   chg regs:    dr
```



**===== 2. Setting Up Debugging Mode =====**

```
[]> aaaa      ; Analyze
[]> s main    ; Seek to main function
[]> db main   ; Set breakpoint at main
[]> ood       ; Repoens the file in a way we can read write in
[]> dc        ; Run till breakpoint


[]> V         ; Should automatically open to visual mode 
              ;   for the debugger (if not use `p` to go to it)
    OR

[]> V!        ; for panel mode!
```



**===== 3. Things to do in Visual Mode while Debugging =====**

1. Use arrow keys or `jk` to go up and down
2. Hit `.` to go back to the original breakpoint

* Note that this uses same hotkeys as `Ollydbg`
3. Hit `F2` to make a breakpoint
4. Hit `F9` to run the program
5. Hit `F7` to `step into a function`
6. Hit `F8` to `step over a function`

* You can click the colon `:` to enter commands (more detail in section below)



**===== 4. Quick Useful Commands while in Visual Mode =====**

```
:> afvd                    ; see all VARIABLES
:> .afvd <variable_name>   ; see specific variable
:> dr 1                    ; see flags
```



**===== 5. Use menu (file,settings,edit,etc) =====**
	Press _Enter_
	Use _left, right, up, down_



**===== 6. Commands while in Visual Mode =====**

* You can click the colon _:_ to enter commands while in visual mode

 + Hit `Enter` on empty command to return to the debugger
 + While in debugger hit `q` to go back to terminal mode
 + If the program expects user input, you will see an empty line with cursor where you can type

```Examples_Commands
:> db main   ; Set breakpoint at main
:> ood       ; Repoens the file in a way we can read write in
:> dc        ; Run till breakpoint

:> dr eax    ; shows what's in EAX register
:> dr rdi    ; show what's in the RDI register

:> pf z @<address>      ; gets the value at an address
:> pf z @<register>     ; gets the value at an address

:> pdf   ; see disasembly
:> pdd   ; see decompiler disassembly
:> pdg   ; see pseudo code in C
         ;  hit enter at the empty command `:>` to go back to debugger

:> afvd  ; see all the VARIABLES
```

```
: dc   ;

[]> s  ; this is to step

# Note that if I hit `:` I can trigger a command i can run
:> dc   ; continue running (if user input is needed it will wait
```

