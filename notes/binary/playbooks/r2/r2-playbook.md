[BEST R2 Use Playlist]: https://www.youtube.com/watch?v=RbIxKM2QW8s&list=PLCwnLq3tOElpDyvObqsAI5crEO9DdBMNA

[Ghidra/Dec]: https://www.youtube.com/watch?v=hufgzz8nwNw
^short sweet video

-----------------------------------------------------------

# TABLE OF CONTENTS 
1. INSTALL FOR GITHUB AND NOT PACKAGE MANAGER (don't use APT)!!!!!!!!!!!!!!!!!
2. Colors

3. USEFUL COMMANDS
  + Finding entrypoint
  + Finding a string
  + Cross Refernce String (2 ways)

4. Convert HEX to ASCII - rax2
5. Write Values

6. PATCHING
7. Good to Know

-----------------------------------------------------------


# 1. INSTALL FOR GITHUB AND NOT PACKAGE MANAGER (don't use APT)!!!!!!!!!!!!!!!!!
```
git clone https://github.com/radareorg/radare2
radare2/sys/install.sh
sudo pip install r2env
r2env init
r2env add radare2@git
```

[Install plugins]: r2pm - radare2 package manager
```
r2pm init
r2pm -ci <pkg> # install

r2pm -ci r2ghidra
r2pm -ci r2dec
```


-----------------------------------------------------------


# 2. COLORS
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


# 3. USEFUL COMMANDS

**i : for INFO ---------------------------------------------**

* Type `i?` to get a list of i commands

 1. `ia` : get info on binary _(imports/exports/sections/etc.)_
   + `iE` : Exports
   + `ii` : Imports
 2. `iz` : Strings
 3. `iz~<search_string>` : Search a string 

**Find Entrypoint / Exit**
1. `ie`  : Entrypoint
2. `iee` : Show Entry and Exit (preinit, init and fini)

**Find a String**
  ```
  iz~<search_string>
  ```
  + Example: `iz~token`

**Cross Reference a Function**
  1. Seek to the function
    + Example: `[]> s main`
  2. Cross reference with the command `axt`
  
**Cross Reference All String**
  ```
  []>axt @ @ str.*
  ```

**Cross Reference String (2 ways)**

  1. Search the string
    + Example
  ```[]> iz~token
  2    0x000838d8 0x004838d8 21   22   .rodata ascii   %d tokens remaining.\n
  ```
  
  2. Cross refernce the string: `pd 1@<address_of_string>`
    + Example
  ```[]> pd 1@0x004838d8
  ;-- str._d_tokens_remaining._n:
  ; DATA XREF from fcn.004005d4 @ 0x400659
  0x004838d8     .string "%d tokens remaining.\n" ; len=22
  ``` 

- - - - - - - - - - - - - - - - - - - - - - -

**a : analyze the binary -----------------------------------**

 + aaa : analyze
 + afl : print functions found
  - Ex:
   > aaa
   > afl
 + axt : Find out where this method I seeked to _is called from_
   ```Example_where_printf_is_called
   s main
   []> axt
   ```
   ```Cross_References_For_All_Strings
   []> axt @ @ str.*
   ```

[rename variable]: renames a variable to what you want
 + afvn <original> <new>
  - Ex: `afvn local_24 new_name`
    Renames to `new_name`

- - - - - - - - - - - - - - - - - - - - - - -

[s commands]: seeks to a certain location (such as fucntion)
 + `s sym.`    <--- this will pull up any symbols that start with 'sym.'
 + s sym.main  :  seeks to the main function
   To move around the file
      ex)
         > s         ; prints current address
         > s 0x10    ; print offset from current address
         > 3s +1024  ; seeks three time 1024 from current seek
         > s pc      ; seek to register

```Go_to_the_entry_function
s entry0	; this should get to the main function
```

- - - - - - - - - - - - - - - - - - - - - - -

-----------------------------------------------------------


# 4. Convert HEX to ASCII - rax2

* radare2 come with `rax2` on command terminal
 + Convert hex to ascii
  - `rax2 -s rax2 -s 0x68736f6a`
  - Output: `hsoj` <-- josh backwards cause litte endian architecture
 + In python
  - `bytes.fromhex('68736f6a').decode('utf-8')`

* misc (execute app: !app; calc eq: ?eq; filter output: ~)


-----------------------------------------------------------


# 5. Write Values

[write trap in entrypoint]: 	  *entry0=cc
[wirte value in delta address]:   *entry0+10=0x804800




-----------------------------------------------------------



# 6. PATACHING
 * assumes you're in visual mode with debugging with write enabled


## Setting Up Visual Mode

1. **Run radare with write and analyze flags**
  + `r2 -w -AAA`
  
2. **Setup Visual Mode**
```
[]> s main    ; Seek to main function
[]> db main   ; Set breakpoint at main
[]> ood       ; Repoens the file in a way we can read write in
[]> dc        ; Run till breakpoint
[]> V!        ; Should automatically open to visual mode w/ panels
```


## Hit `:` to enter command while in Visual Mode:
```
:> s <address>   ; seek to address where you want to patch
:> pd 1          ; see line to verify
:> wx <bytes>    ; write bytes
:> pd 1          ; verify you wrote the right bytes
```


## Example of changing `jump` instruction
```
:> pd 1
    0xf7f7f7f7   750c    jne <some address>

:> wx 74         ; if in WRITE MODE this will permanently patch binary

:> pd 1
    0xf7f7f7f7   740c    je <some address>
```


* patch (print: p; write: w; chg Asm: wa, A)


-----------------------------------------------------------


# 7. Good to Know

  `~` --> is used as grep
    ex) [0x00000000]> pD oxdff ~0xc6

  `q` --> quit what you're currently doing (may need to click multiple times)

  `!<bash-cmd>` --> to do cmds from r2
    ex) > ~!ls  
            ^ runs the `ls` command

  `@` --> specify a temporary offset location or
        seek position at which the command is executed.
        ex)
           p8 10 @ 0x4010     ; show 10 bytes at offset 0x4010
           f  patata @ 0x10   ; set 'patata' flag at offset 0x10

  `@@` --> execute a single command on a list of flags matching the glob 
         (think of as foreach loop)

  `>`  --> Redirect the output of command to a file
       ex)
          pr > dump.bin    ; dump 'raw' bytes of current block to a file
          f > flags.txt    ; dump flag list to file

  `;`  --> Pass several commands ina single line
       ex)
          px ; dr

  `/`   --> search plain string
       ex) / foo

  `/x` --> look for hex pairs
       ex) /x 90 90



-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------

[Block Size]: b


---------------------------------------------------------------


[Useful Keys]:
 + Shift+r -> randomizes color
 + Esc  to  exit certain views
 + ? tells me commands i can use


---------------------------------------------------------------


[Set Values]: set certain values
`dr rip=0x<address>`


---------------------------------------------------------------


[break point]: Stop at a certain point
`db`
 + Ex:
   > aaa
   > s sym.main
   > pdf
   > db <at an adress at the start of main>


---------------------------------------------------------------

[Sections]: The different parts of the binary
  
  iS --> displaying info about sections
  om --> view info about mapped sections

# Archive

----------------------------------------------------
### See debug commands
	:> d


### Exit debug commands
	keep pressing q 
	   OR
	:> q


### Display Memory Maps
	:> dm


### Read value at given address
	:> *<address>
	:> *entry0





### Use menu (file,settings,edit,etc)
	press Enter
	use left,right,up,down


[s]: step
# Keep pressing s to setp through the program

# Windows
	s entry0	; this should get to the main function


[q]: reprints the summary

[Debug Program]: How to run a binary as well as look through it
# Use the colon command ':'
# Then enter 'dc'
 + You sill see 'rip:' in the selected visual box to mark where
   in the program you are
# 's' to step through instructions
# 'S' to to step without following functions
  - Ex:
   $ r2 -d     -A      <binary>
        ^debug ^do aaa
   > s sym.main
   > pdf
   > db <at an adress at the start of main>
   > :
   > dc
   > [Enter]
