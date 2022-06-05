#  { } is for stack operations

    pop    {r11, pc}    /* End of the epilogue. Restoring Frame pointer from the stack, jumping to previously saved LR via direct load into PC */

    push   {r11, lr}    /* Start of the prologue. Saving Frame Pointer and LR onto the stack */

---------------------------------------------

[Literal Pool]: Memory 
#Memory area in the same section (because the literal pool is part of the code) to store constants, strings, or offsets
    v = n ror 2*r


#Insturctions that don't update status register (may not be all)~~~~~~~~~~~~~~
    + AND
    + ADD
    + SUB


#Adding S at the end of instruction~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + When using instructions such as ADD and SUB, the status register doesn't get updated
    + Adding s at the end (ADDS and SUBS) makes it so the status register updates



#Adding cc at the end of instruction~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + Checks to see if the carry bit is set to 0 (C==0)
     - ADDCC: do the operation if the carry status bit is set to 0
      - ADDCCS: do the operation if the carry status bit is set to 0 and afterwards, update the status flags (if C=1, the status flags are not overwritten).



###INSTRUCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         1b     4b      2b     2b        8b     4b for rotational: 2*r
          ^      ^       ^      ^         ^      ^

[MNEMONIC{S}{condition} {Rd},  Operand1, Operand2]: template
--------------------------------------------------------------
# MNEMONIC    - Short name (mnemonic) of the instruction
--------------------------------------------------------------
# {S} - Optional suffix
      If S is specified, the condition flags are updated 
      on the result of the operation
--------------------------------------------------------------
# {condition}
      Condition that is needed to be met in order for the
      instruction to be executed (checks the CPSR register
      for condition)

  - Example:

        MOVLE R0, #5        - Moves number 5 (Operand2, because the compiler treats it 
                                as MOVLE R0, R0, #5) to R0 (Rd) ONLY if the condition LE 
                                (Less Than or Equal) is satisfied
--------------------------------------------------------------
# {Rd}        - Register (DESTINATION) for storing the result of the instruction
--------------------------------------------------------------
# Operand1    - First operand. Either a register or an immediate value 
--------------------------------------------------------------
# Operand2    - Second (flexible) operand. Can be an immediate value (number)  or a register with an optional shift

  - Can be used as:
  ```
   * Immediate Value:       ADD   R0, R1, #2
   * Register:              ADD   R0, R1, R2
   * Register w/ a shift:   ADD   R0, R1. LSL #1
  ```

        ADD   R0, R1, R2         - Adds contents of R1 (Operand1) and R2 
                                    (Operand2 in a form of register) 
                                    and stores the result into R0 (Rd)
                                    _
        ADD   R0, R1, #2         - Adds contents of R1 (Operand1) and the value 2 
                                    (Operand2 in a form of an immediate value) 
                                    and stores the result into R0 (Rd)
                                    _
        MOV   R0, R1, LSL #1     - Moves the contents of R1 (Operand2 in a form of register 
                                    with logical shift left) shifted left by one bit to R0 (Rd). 
                                    So if R1 had value 2, it gets shifted left by one bit and 
                                    becomes 4. 4 is then moved to R0.

--------------------------------------------------------------

### MEMORY INSTRUCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ **Only LOAD & STORE instructions can ACCESS MEMORY**
+ **ARM data must be moved from memory into registers** before being operated on
  (in x86 you can directly operate on data in memory)

```
+ Load the value at the address found in R0 to the destination register R2
 - LDR R2, [R0]
+ Store the value found in R2 to the memory address found in R1
 - STR R2, [R1]
```

+ [ ] means: the value found in the register between these brackets is a memory address we want to load something from
+ ARM can only load an 8-bit value in one go (cause of the 32 bits available to an instruction which include dest reg, operands, status flag, etc.)

---------------------------------------------------

#1. Offset form: Immediate value as the offset
      STR    Ra, [Rb, immediate-value]
      LDR    Ra, [Rc, immediate-value]

 [Addressing mode: Offset]: str r2, [r1, #2]
  
  + Store the value found in R2 (0x03) to the memory address found 
   in R1 plus 2
  + Base register (R1) UNMODIFIED
 
 [Addressing mode: Pre-indexed]: str r2, [r1, #4]!  

  + Store the value found in R2 (0x03) to the memory address found 
   in R1 plus 4
  + Base register (R1) MODIFIED: R1 = R1+4
 
 [Addressing mode: Post-indexed]: ldr r3, [r1], #4  

  + *Load the value at memory address found in R1 to register R3*
  + Base register (R1) MODIFIED: R1 = R1+4

---------------------------------------------------------------

#2. Offset form: Register as the offset
      STR    Ra, [Rb, Rc]
      LDR    Ra, [Rb, Rc]

 [Addressing mode: Offset]: str r2, [r1, r2]

  + *Store the value found in R2 (0x03) to the memory address found 
     in R1 with the offset R2 (0x03)*
  + Base Register Unmodified

 [Addressing mode: Pre-indexed]: str r2, [r1, r2]!

  + *Store value found in R2 (0x03) to the memory address found 
     in R1 with the offset R2 (0x03)*
  + Base register modified: R1 = R1+R2
 
 [Addressing mode: Post-indexed]: ldr r3, [r1], r2

  + *Load value at memory address found in R1 to register R3*
  + Then modify base register: R1 = R1+R2

---------------------------------------------------------------

#3. Offset form: Scaled register as the offset
 
 [Addressing mode: Offset]: str r2, [r1, r2, LSL#2]

  + *Store the value found in R2 (0x03) to the memory address found 
     in R1 with the offset R2 left-shifted by 2*
  + Base register (R1) unmodified

 [Addressing mode: Pre-indexed]: str r2, [r1, r2, LSL#2]!
  + *Store the value found in R2 (0x03) to the memory address found 
     in R1 with the offset R2 left-shifted by 2*
  + Base register modified: R1 = R1 + R2<<2
 
 [Addressing mode: Post-indexed]: ldr r3, [r1], r2, LSL#2
  + *Load value at memory address found in R1 to the register R3*
  + Then modifiy base register: R1 = R1 + R2<<2

==============================================================

#LDR FOR PC-RELATIVE ADDRESSING (PSEUDO-INSTRUCTIONS)
 + LDR is not only used to load data from memory into a register. Sometimes you will see syntax like this:
```
   .section .text
   .global _start
   
   _start:
      ldr r0, =jump        /* load the address of the function label 
                              jump into R0 */
      ldr r1, =0x68DB00AD  /* load the value 0x68DB00AD into R1 */
   jump:
      ldr r2, =511         /* load the value 511 into R2 */ 
      bkpt
```
 + The reason why we sometimes need to use this syntax to move a 32-bit constant into a register in one instruction is because ARM can only load a 8-bit value in one go

===============================================================

[LOAD & STORE MULTIPLE / INCREMENT & DECREMENT]:

ldm   - load  multiple
stm   - store multiple

ldmia - load  multiple increment after
stmia - store multiple increment after

ldmib - load  multiple increment before
stmib - store multiple increment before

ldmda - load  multiple decrement after
stmda - store multiple decrement after

ldmdb - load  multiple decrement before
stmdb - store multiple decrement before

--------------------------------------------------------------

! denotes writeback of the base register. Base register is the register used to address the memory to be read or written - in your case it's R4. Writeback means that the base register will be updated with the delta equal to the size of transferred data.

So, the instruction

ldm r4!, {r0, r1, r2, r3}
can be represented by the following pseudocode:

r0 = *(int)(r4) 
r1 = *(int)(r4+4) 
r2 = *(int)(r4+8) 
r3 = *(int)(r4+12) 
r4 = r4 + 16 // writeback (16 bytes transferred)
-

#asdfasdf
