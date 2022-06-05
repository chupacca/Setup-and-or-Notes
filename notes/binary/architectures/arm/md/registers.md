Look at registers.png & cpsr-status_register.png

------------------------------------------------------------------
#KEYWORDS
  + STACK FRAME --> FUNCTION (ROUTINE)

------------------------------------------------------------------
#REGISTERS

[ R0 ]: Can be used as an ACCUMULATOR for arithmetic operations
[ R0 ]: Can store RESULT of previously called FUNCTION

[ R0-R3 ]: For FUNCTION CALLING first 4 registers are arguments

[ R4-R6 ]:  General Purpose
[ R7 ]:     Syscall Number (store syscall number)
[ R8-R10 ]: General Purpose

[R11]: (FP)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FRAME POINTER - POINTS TO THE FRAME (push & pop DON'T modify this value)

[R12]: (IP)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#INTRA-PROCEDURE REGISTER - 

[R13]: (SP)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#STACK POINTER - POINTS TO TOP OF THE STACK (push & pop modify this value)
  [STACK FRAME]: FUNCTION (ROUTINE)
     A stack frame is comprised of:
        1. Local Variables
        2. Saved copies of registers modified by subprograms 
           that could need restoration
        3. Argument parameters
        4. Return address

[R14]: (LR)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LINK REGISTER - Has the return address if BL/BLX is executed
  ^like EIP REGISTER

[R15]: (PC)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROGRAM COUNTER - Has address of next instruction to be executed
  + A register similar to EIP in x86
  + When fetching from PC, you'll get **2 INSTRUCTIONS AHEAD**
   - Example:
      0x8054 mov, r0, pc    <=== r0 will be 0x85c
      0x8058 add r1, r0, r0      |
      0x805c add r1, r0, r0   <---

[CPSR]: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#BITS that represent a certain state
  + EFLAGS in x86
  + T: bit is set if in thumb mode
  + M: specify current privilege (USR, SVC, etc)
  + J: Allows some ARM processors to execute Java bytecode

#COMMANDS - KEY POINTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[Carry Flag]:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  +  ADDITION result is greater than or equal to 2^32
  +  SUBTRACTION result is poitive or 0
  +  INLINE BARREL SHIFTER OPERATION result or LOGICAL INSTRUCTION

  Example:
      r0 = 0x00000002
      r1 = 0x00000004
      r2 = 0x00000004
      cmp r1, r0   <---- (4-2)  CARRY (C) FLAG IS SET
      cmp r0, r1   <---- (2-4)  NEGATIVE (N) FLAG IS SET
      cmp r1, r2   <---- (4-4)  ZERO (Z) FLAG IS SET

