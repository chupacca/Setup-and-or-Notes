### Assembly -> Binary
    $ as program.s -o program.o
    $ ld program.o -o program


### C ->  Binary
    $ gcc progarm.c -o program


### C -> Assymbly
    $ gcc progarm.c -o program
    Then use cutter/binja/ghidra


-------------------------------------------


1. Make assembly file

2. Name the assembly file -> file.s

3. Use an assembler (as)
    $ as file.s -o file.o
    $ as --help

4. Use objdump:
    $ objdump -d file.o

5. Use linker
    $ ld file.o -o file
    $ ld --help
    $ ld -N file.o -o file
          ^Do not page align data
          ^Do not make text readonly
 
 6. Turning to hex
    $ objcopy -O binary file file.bin

 7. Viewing hex
   $ hexdump -v -e '"\\""x" 1/1 "%02x" ""' file.bin

 8. Reverse shell
   + Create a new TCP socket
   + Bind socket to a local port
   + Listen for incoming connections
   + Accept incoming connection
   + Redirect STDIN, STDOUT and STDERR to a newly created 
     socket from a client
   + Spawn the shell
 
