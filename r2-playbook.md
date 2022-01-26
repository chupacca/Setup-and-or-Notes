
BEST R2 Use Playlist: https://www.youtube.com/watch?v=RbIxKM2QW8s&list=PLCwnLq3tOElpDyvObqsAI5crEO9DdBMNA

Ghidra/Dec https://www.youtube.com/watch?v=hufgzz8nwNw
^short sweet video

-----------------------------------------------------------

# INSTALL FOR GITHUB AND NOT PACKAGE MANAGER (like APT)!!!!!!!!!!!!!!!!!
```
git clone https://github.com/radareorg/radare2
radare2/sys/install.sh
sudo pip install r2env
r2env init
r2env add radare2@git
```

[Install plugins]: r2pm
```
r2pm -ci <pkg> # install

r2pm -ci r2ghidra
r2pm -ci r2dec
```

-----------------------------------------------------------

# COLORS
```
[]> eco         ;  this shows the color schemes
[]> eco <name>  ;  will change to that color scheme from eco
```
[Examples]:
```
[]> eco bobcrawl
[]> eco bright
[]> eco cutter

[]> eco rasta
[]> eco cga
```

-----------------------------------------------------------

# Quick start
1. Run radare
  + `r2 <binary>`          run radare on binary
  + `r2 -AAA <binary>`     run radare and analyze binary
  + `r2 -w -AAA <binary>`  run radare with write permission

2. Intial commands to run in radare
```
[]> aaaa    ; analyze binary
[]> s main  ; seek to main function

# Quick reference to other commands I don't really reference this document
[]> clear   ; clears terminal
[]> a?      ; get list of commands

[]> s <function_Or_address>  ; goes to that function/address
                             ; you should see address change b/w brackets

[]> afl     ; see functions
[]> axt     ; cross reference where we are
[]> axt @ @ str.*  ; cross references for all strings

[]> iI      ; get basic info about binary
[]> is      ; see symbols
[]> ii      ; see import
[]> iE      ; get export
[]> iz      ; strings in data section

[]> iS entropy   ; Get entropy for each section
                 ; You get high entropy like 7 if this is
                 ;   packed/compressed/encrypted

[]> pd 1@<function_Or_address>   ; print 1 line of disassembly at address
```

-----------------------------------------------------------

# VISUAL MODE

[Visual Mode]: V
```    
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> V

* Hit `q` twice to go back to terminal mode
* Hit `Space` to toggle to graph mode
```

[Graph Mode]: VV
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> VV

* Hit `q` TWICE to go back to terminal mode
* Hit `Space` to toggle to visual mode
```

[Panel Mode]: V!
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> V!

* you can  use `TAB` to switch among panels
* when in another panel, hit `"` to choose what that panel shows
* you can hit `-` to split a panel
* you can hit `X` to close a panel
* hit `z` to make the current window to the top left panel
* There's a tollbar on the top you can use your mouse on
   (then use arrow keys and Enter)
```

[Notes]:

1. When in VISUAL mode, hit `q` to go BACK TO TERMINAL MODE!!!!!
   [Quit]: q -> to go back to command window
   * may need to hit `q` twice if VV is used!!!!!!!!!!!!!!!!!!!!


2. Note that you can click the colon `:` to enter  
    commands while in visual mode


3. In Visual Mode you can:  
  + Regular move: `mouse` or `arrow keys`
   - For faster movement, hold `Shift` while doing this

  + Move like VIM:
   - `j` for down
   - `k` for up
   - `h`for left
   - `l` for right

   - For faster movement, hold `Shift` while doing this

4. You can change what type of visual mode by hitting `p`  
[Change mode]: p
   - p  ; changes go one way
   - P  ; changes go the other way

5. Go from vertical view to horizontal view:   
   `Shift+V`

6. I can use h and l to shift what address I'm looking at `one byte at a time`
  + This way I can look at different types of instructions (google geometry of instructions)

```Other
 ascii flow graph (analyse: df, af, move: hjkl, resize: +-0, chg mode: pP, highlight: /)
```

- - - - - - - - - - - - - - - - - - - - - - -

# GHIDRA & DEC
* From `r2ghidra` & `r2dec`

[Useful Link]: https://www.youtube.com/watch?v=hufgzz8nwNw

[Ghidra]: pdg
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdg     ; this will give you main method in ghidra
            ;   PSEUDO-CODE should appear too!!!
```
[Dec]: pdd
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdd     ; dec's decompilation
            ;  useful to SEE REGISTERS; like in BINJA
```

[Radare]: pdf
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdf     ; get radare's default decompilation
```

-----------------------------------------------------------

# DEBUGGING
```
debugging (step: s, ds, F7;
           breakpoint: db;
           continue: dc, F9;
           chg regs: dr)
```
[Setting up debugging mode]:
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

[Things to do in Visual Mode while debugging]:  

1. Use arrow keys or `jk` to go up and down
2. Hit `.` to go back to the original breakpoint

* Note that this uses same hotkeys as `Ollydbg`
3. Hit `F2` to make a breakpoint
4. Hit `F9` to run the program
5. Hit `F7` to `step into a function`
6. Hit `F8` to `step over a function`

* You can click the colon `:` to enter commands (more detail in section below)  
[Quick useful commands while in Visual Mode]:  
```
:> afvd                    ; see all VARIABLES
:> .afvd <variable_name>   ; see specific variable
:> dr 1                    ; see flags
```


[Commands while in Visual Mode]:
* You can click the colon `:` to enter commands while in visual mode

 + Hit `Enter` on empty command to return to the debugger
 + While in debugger hit `q` to go back to terminal mode
 + If the program expects user input, you will see an empty line with cursor where you can type

```Examples commands
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

-----------------------------------------------------------


# PATACHING
* assumes you're in visual mode with debugging with write enabled

[Setting Up Visual Mode]:
1. Run radare with write and analyze flags
  + `r2 -w -AAA`
2. Setup Visual Mode
```
[]> s main    ; Seek to main function
[]> db main   ; Set breakpoint at main
[]> ood       ; Repoens the file in a way we can read write in
[]> dc        ; Run till breakpoint
[]> V!        ; Should automatically open to visual mode w/ panels
```


[Hit `:` to enter command while in Visual Mode]:
```
:> s <address>   ; seek to address where you want to patch
:> pd 1          ; see line to verify
:> wx <bytes>    ; write bytes
:> pd 1          ; verify you wrote the right bytes
```

[Example of changing `jump` instruction]:
```
:> pd 1
    0xf7f7f7f7   750c    jne <some address>

:> wx 74         ; if in WRITE MODE this will permanently patch binary

:> pd 1
    0xf7f7f7f7   740c    je <some address>
```


* patch (print: p; write: w; chg Asm: wa, A)


-----------------------------------------------------------

* radare2 come with `rax2` on command terminal
 + Convert hex to ascii
  - `rax2 -s rax2 -s 0x68736f6a`
  - Output: `hsoj` <-- josh backwards cause litte endian architecture
 + In python
  - `bytes.fromhex('68736f6a').decode('utf-8')`

* misc (execute app: !app; calc eq: ?eq; filter output: ~)
