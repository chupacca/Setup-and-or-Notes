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


