The tool we will use to assemble the assembly code into machine code is a GNU Assembler from the GNU Binutils project named as which works with source files having the *.s extension.
****
Once you wrote your assembly file with the extension *.s, you need to assemble it with as and link it with ld*:

     $ as program.s -o program.o
     $ ld program.o -o program

*********

---------------------------------------------------------------------


[ASSEMBLY PROGRAM]: The different sectionss

    /* the .data section is dynamically created and its addresses cannot be easily predicted */
    .data

    /* variable 1 in memory */
    var1: .word 3
    /* variable 2 in memory */
    var2: .word 4               

    /* start of the text (code) section */ 
    .text          
    .global _start
    _start:
      ldr r0, adr_var1  @ load the memory address of var1 via label adr_var1 into R0 
      ldr r1, adr_var2  @ load the memory address of var2 via label adr_var2 into R1 
      ldr r2, [r0]      @ load the value (0x03) at memory address found in R0 to register R2  
      str r2, [r1]      @ store the value found in R2 (0x03) to the memory address found in R1 
      bkpt           

    /* address to var1 stored here */ 
    adr_var1: .word var1  
    /* address to var2 stored here */
    adr_var2: .word var2  
*********


---------------------------------------------------------------------

# [ ] -> the value found in the register between these brackets is a memory address we want to load something from
# Think of it like dereferencing a pointer (except when it's lea)
    EX: [fp, #-12]

*********
---------------------------------------------------------------------


[DEBUGGER]: debugging assembly

+ <gef disassemble _start
>

# The labels we specified with the first two LDR operations changed to [pc, #12]. This is called PC-relative addressing
        Current position + #12   (in this example)

        Dump of assembler code for function _start:
        0x00008074 <+0>:      ldr  r0, [pc, #12]   ; 0x8088 <adr_var1>
        0x00008078 <+4>:      ldr  r1, [pc, #12]   ; 0x808c <adr_var2>
        0x0000807c <+8>:      ldr  r2, [r0]
        0x00008080 <+12>:     str  r2, [r1]
        0x00008084 <+16>:     bx   lr
        End of assembler dump.

# Look at arm-relativeAddressing.png to get a ___VISUAL EXAMPLES___
****************


''
------------------------------------------------------------------------------------------------
### CONDITIONAL EXECUTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .global main

    main:
        mov     r0, #2     /* setting up initial variable */
        cmp     r0, #3     /* comparing r0 to number 3. Negative bit 
                              get's set to 1 */
        addlt   r0, r0, #1 /* increasing r0 IF it was determined that 
                              it is smaller (lower than) number 3 */
        cmp     r0, #3     /* comparing r0 to number 3 again. Zero bit 
                              gets set to 1. Negative bit is set to 0 */
        addlt   r0, r0, #1 /* increasing r0 IF it was determined that 
                              it is smaller (lower than) number 3 */
        bx      lr
******



''
------------------------------------------------------------------------------------------------
### CONDITIONAL EXECUTION IN THUMB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[IT]: Some ARM processors support this in THUMB MODE

+ 4 instructions

# Syntax:  IT{x{y{z}}} cond
      - cond specifies the condition for the first instruction in the IT block
      - x specifies the condition switch for the second instruction in the IT block
      - y specifies the condition switch for the third instruction in the IT block
      - z specifies the condition switch for the fourth instruction in the IT block

# The structure of the IT instruction is ___*IF-Then-(Else)*___ and the syntax is a construct of the two letters T and E:
      - IT refers to If-Then (next instruction is conditional)
      - ITT refers to If-Then-Then (next 2 instructions are conditional)
      - ITE refers to If-Then-Else (next 2 instructions are conditional)
      - ITTE refers to If-Then-Then-Else (next 3 instructions are conditional)
      - ITTEE refers to If-Then-Then-Else-Else (next 4 instructions are conditional)

# Each inst in IT block must have SAME CONDITION or LOGICAL INVERSE
      - IF-THEN must have same condition
      - ELSE must have inverse condition

# Examples:
        ITTE   NE           ; Next 3 instructions are conditional
        ANDNE  R0, R0, R1   ; ANDNE does not update condition flags
        ADDSNE R2, R2, #1   ; ADDSNE updates condition flags
        MOVEQ  R2, R3       ; Conditional move

        ITE    GT           ; Next 2 instructions are conditional
        ADDGT  R1, R0, #55  ; Conditional addition in case the GT is true
        ADDLE  R1, R0, #48  ; Conditional addition in case the GT is not true

        ITTEE  EQ           ; Next 4 instructions are conditional
        MOVEQ  R0, R1       ; Conditional MOV
        ADDEQ  R2, R2, #10  ; Conditional ADD
        ANDNE  R3, R3, #1   ; Conditional AND
        BNE.W  dloop        ; Branch instruction can only be used in the last 
                            ; instruction of an IT block


''
------------------------------------------------------------------------------------------------
### BRANCHING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ Also known as jump

[Example]: ex

    .global main
    main:
        mov     r1, #2     /* setting up initial variable a */
        mov     r2, #3     /* setting up initial variable b */
        cmp     r1, r2     /* comparing variables to determine which is bigger */
        blt     r1_lower   /* jump to r1_lower in case r2 is bigger (N==1) */
        mov     r0, r1     /* if branching/jumping did not occur, r1 is bigger 
                              (or the same) so store r1 into r0 */
        b       end        /* proceed to the end */
    r1_lower:
        mov r0, r2         /* We ended up here because r1 was smaller than r2, 
                              so move r2 into r0 */
        b end              /* proceed to the end */
    end:
        bx lr              /* THE END */

[B / BX / BLX]: branching
# B:  Branch
    * Simple jump to function

#  BL: Branch Link
    * Saves (PC+4) in LR and jumps to function

# BX: Branch Exchange
    * Need a register as first operation
    * BX/BLX <register>
    * According to the lsb (least significant bit) of the address to branch to, 
      the processor will treat the next instruction as ARM or as thumb.


[CONDITIONAL BRANCHES]: b
# BEQ is an example (branch is equal)


