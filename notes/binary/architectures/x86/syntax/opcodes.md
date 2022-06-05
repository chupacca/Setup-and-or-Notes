# Opcodes ==================================

[CALL – FF Dx]:
   + The `x` in `Dx` could be anything from `D0` to `D7` based on the register referenced
   + You’re just trying to recall what a command does when you see it
   + Therefore, you don’t have to memorize the number for each register

[JMP – EB]: You’re going to be seeing this one alot!

[INC – 4x]:
  + The `x` in `4x` goes from 40 to 47 depending on the register
  + When you fuzz a program, you’re going to use lots of A’s, B’s and C’s (\x41, \x42, \x43)
  + That means that sending A (\x41) to a program, it will be interpreted as a `INC ECX`
  + This is useful to know not just for quickly identifying where your offset lands
  + But, it's also as a reminder that they can be interpreted as commands

[DEC – 4x]:
 + The `x` in `4x` goes from 48 to 4F
 + This carries on where INC stopped and goes from 48 to 4F depending on the register
 + Careful of information overload here
 + Limit your list to seven or eight opcodes at most.

