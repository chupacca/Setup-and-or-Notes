[x86 Overview]: https://www.youtube.com/watch?v=75gBFiFtAb8&list=PLkf235f24oOnzkiAQPFsQF1hkwbycDxCC
 * is also a playlist


# Instructions ===================================================


## CALL
Call <func>  =   push eip
                  jmp func

* Pushes where eip is pointing (the next instruction to be executed)
  onto the stack
* This wasy, when the function returns, EIP repoints to the instruction
  where it left off

## LEAVE/RET

* leave is followed by ret

[leave]:
 + ESP = EBP
 + POP (pops EBP off of the stack)
  - stores result in EBP register
  - now the return address should be at the top of the stack
    so ESP should be pointing at the return address

[ret]:
 + POP the return instruction (where we're executing code next)
 + store the address in the EIP register

-----------------------------------------------------------------------
-----------------------------------------------------------------------



# Parameter Order ==========================
 + Destination before source: <inst> <dest>, <src>

 [Example]: mov eax, 5


# Sigils ===================================
   
-----------------------------------------------------------------------
-----------------------------------------------------------------------

[Symbols]:

 [] - if brackets, then defrefernce, EXCEPT when it's LEA instruction
  + mov eax, [ebp - 4]
   - Value of ebp is subtracted by 4 and the brackets indicate
     we are grabbing from memory at the resulting vaue of ebp-4
   - That value is then stores in the eax register

  + lea eax, [ebp - 4]
   - Value of ebp is subtracted by 4 and the ADDRESS is stored in eax


