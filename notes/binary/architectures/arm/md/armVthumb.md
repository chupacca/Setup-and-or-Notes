#ARM vs THUMB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ ARM: always 32 bit
+ Thmb: 16 bit (but can be 32 bit)

+ When writing ARM shellcode, we need to get rid of NULL bytes and using 16-bit Thumb instructions instead of 32-bit ARM instructions reduces the chance of having them

+ *NOT* all ARM *VERSIONS* support the *SAME THUMB INSTRUCTION* SET

+ Both are in .w files
+ To switch betweein ARM and Thumb:
 - Use BX(branch & exchange) or BLX(branch, link, exchange) instruction and set the destination register's least significant bit to 1
   * This can be done by adding 1 to an offset (like 0x5530 + 1)

+ Processor ignores least significant bit
+ If T bit is set, in thumb node

-----------------------------------------------------------------

[THUMB]:
  + Different naming is just for the sake of differentiating them from each other (the processor itself will always refer to it as Thumb)

  + Thumb-1 (16-bit instructions): was used in ARMv6 and earlier architectures.
  + Thumb-2 (16-bit and 32-bit instructions): extents Thumb-1 by adding more instructions and allowing them to be either 16-bit or 32-bit wide (ARMv6T2, ARMv7).
  + ThumbEE: includes some changes and additions aimed for dynamically generated code (code compiled on the device either shortly before or during execution).
------------------------------------------------------------------
[ARM]:
  + Barrel Shifter
   -  You can include the multiply inside a MOV instruction by using shift left by 1:
        Mov  R1, R0, LSL #1  ; R1 = R0 * 2


-----------------------------------------------------------------

#CONDITIONAL EXECUTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

#CONDITIONAL EXECUTION IN THUMB~~~~~~~~~~~~~~~~~~~~~~~~

[IT]: Some ARM processors support this in THUMB MODE

+ 4 instructions

+ Syntax:  IT{x{y{z}}} cond
  - cond specifies the condition for the first instruction in the IT block
  - x specifies the condition switch for the second instruction in the IT block
  - y specifies the condition switch for the third instruction in the IT block
  - z specifies the condition switch for the fourth instruction in the IT block

+ The structure of the IT instruction is ___*IF-Then-(Else)*___ and the syntax is a construct of the two letters T and E:
  - IT refers to If-Then (next instruction is conditional)
  - ITT refers to If-Then-Then (next 2 instructions are conditional)
  - ITE refers to If-Then-Else (next 2 instructions are conditional)
  - ITTE refers to If-Then-Then-Else (next 3 instructions are conditional)
  - ITTEE refers to If-Then-Then-Else-Else (next 4 instructions are conditional)

+ Each inst in IT block must have SAME CONDITION or LOGICAL INVERSE
 - IF-THEN must have same condition
 - ELSE must have inverse condition

+ Examples:

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


-----------------------------------------------------------------

#BRANCHING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ Also known as jump

[Example]:
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

[B / BX / BLX]:
 - B:  Branch
   * Simple jump to function
 - BL: Branch Link
   * Saves (PC+4) in LR and jumps to function
 - BX: Branch Exchange
   * Need a register as first operation
   * BX/BLX <register>
   * According to the lsb (least significant bit) of the address to branch to, the processor will treat the next instruction as ARM or as thumb.


[CONDITIONAL BRANCHES]:
 - BEQ is an example (branch is equal)

--------------------------------------------

#
