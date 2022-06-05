# REGISTERS

+ Retun Value: EAX

+ Arguments Order
 - EAX
 - EBX
 - ECX
 - EDX

## How Registers get denoted (using EBX as example)

EBX
 + Gets the literal value within the EBX register

[EBX]
 + Brackets around register means you're getting the value stored at the
   address in the EBX register


 [] - if brackets, then defrefernce, EXCEPT when it's LEA instruction
  + mov eax, [ebp - 4]
   - Value of ebp is subtracted by 4 and the brackets indicate
     we are grabbing from memory at the resulting vaue of ebp-4
   - That value is then stores in the eax register

  + lea eax, [ebp - 4]
   - Value of ebp is subtracted by 4 and the ADDRESS is stored in eax


--------------------------------------------------------------------


## General Registers
 + EAX
 + EBX
 + ECX
 + EDX
 + ESI
 + EDI

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[EAX]: Accumulator Register

 + Primary register used for common calculations
  - ADD
  - SUB

 + EAX has been given preferential status by assigning it more efficient,
   one-byte opcodes

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[EBX]: No special purpose

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[ECX]: Counter Register

 + Frequently used as a loop/function repitition counter

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[EDX]: Data Register

 + Can be partnered with EAX
   - Often used with division/multiplication operations
     to deal witch overflow

 + Also commonly used for storing function variables

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[ESI]: Source Index

 + Counterpart to EDI
 + Often used to store the pointer to a read location

 + Example: If a function is designed to read a string,
            ESI would hold the pointer to the location of
            the string

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[EDI]: Destination Index

+ Designed to store the storage pointers of functions
 - SUch as write address of a string operation

- - - - - - - - - - - - - - - - - - - - - - - - - - -

[Whole Partial Registers]:

 + EAX as examples
  - EAX -> whole register 32 bits
   * AX  -> last 16 bits
    1. AH the first  half of AX (8 bits)
    2. AL the second half of AX (8 bits)

 + This pattern applies to EBX, ECX, & EDX


--------------------------------------------------------------------


## Reserved
 + EBP
 + ESP
 + EIP

- - - - - - - - - - - - - - - - - - - - - - - - - - -

* Area between EBP and ESP is a stack frame
  (where stack resources for a specific function begins)

[EBP]: Base Pointer
 + Bottom of stack frame

[ESP]: Stack Pointer
 + Points to the top of the stack

[EIP]: Instruction Pointer
 + Points to memory address of the next instruction to be executed


--------------------------------------------------------------------


## Special Registers

[EFLAGS]: Flag register
 + Denotes the result of a calculation
    (usually to denote when to execute conditional jmp instruction)

 + Possible Identifiers
   zero
   carry
   parity
   adjust
   sign
   trap
   interrupt
   direction
   overflow
   resume
   virtualx86
   identification


[Segment]:
 + Most applications on most modern operating systems
   (like FreeBSD, Linux or Microsoft Windows)
   use a memory model that points nearly all segment registers to the same place
   (and uses paging instead)
 + This  effectivly disables their use
 + Typically the use of FS or GS is an exception to this rule
   instead being used to point at thread-specific data

 + Stack Segment (SS). Pointer to the stack.
 + Code Segment (CS). Pointer to the code.
 + Data Segment (DS). Pointer to the data.
 + Extra Segment (ES). Pointer to extra data ('E' stands for 'Extra').
 + F Segment (FS). Pointer to more extra data ('F' comes after 'E').
 + G Segment (GS). Pointer to still more extra data ('G' comes after 'F').


