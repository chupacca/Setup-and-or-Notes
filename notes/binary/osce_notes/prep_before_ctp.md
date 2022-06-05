# Preparing for CTP (before starting)


[WATCH THIS]: https://www.youtube.com/watch?v=gHISpAZiAm0
[Vulnserver Buffer Overflows]: https://github.com/stephenbradshaw/vulnserver
[x86 Refernce & Opcodes]: https://c9x.me/x86/
[ASCII Shellcode]: https://nets.ec/Ascii_shellcode

[Web1 - File Inclusion]: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion
[Web2 - XSS]: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection

[Fuzzer]: boofuzz



##1 Windows Exploitation Basics: 
    ```
    http://www.securitysift.com/windows-exploit-development-part-1-basics/
     OR
    go to ~/Documents/osce/resources/WindowsExploitDevelopment-Part1.pdf

```

Go over vulnserver: https://resources.infosecinstitute.com/topic/restricted-character-set-vulnserver/
vulnserver.exe is in the resources folder!
http://thegreycorner.com/tags.html#vulnserver


##2 GDB (did this with protostar)


##3 Basic Assembly Opcodes - Useful Opcodes

It’s a good idea to memorize the op codes for one or two commands.

This will make reading assembly so much easier down the line.

The ones that I recommend:

[CALL – FF Dx]: 
   + The `x` in `Dx` could be anything from `D0` to `D7` based on the register referenced
   + You’re just trying to recall what a command does when you see it
   + Therefore, you don’t have to memorize the number for each register

[SHORT JMP – EB]: You’re going to be seeing this one alot! Also, useful opcode

[INC – 4x]: 
  + The `x` in `4x` goes from 40 to 47 depending on the register
  + When you fuzz a program, you’re going to use lots of A’s, B’s and C’s (\x41, \x42, \x43)
  + That means that sending A (\x41) to a program, it will be interpreted as a `INC ECX`
  + This is useful to know not just for quickly identifying where your offset lands
  + But, it's also as a reminder that they can be interpreted as commands

  
  * 43 -> INC EBX
  
[DEC – 4x]:
 + The `x` in `4x` goes from 48 to 4F
 + This carries on where INC stopped and goes from 48 to 4F depending on the register
 + Careful of information overload here
 + Limit your list to seven or eight opcodes at most.

[POPAD - 61]:

[Opcode instruction to move `DWORD ptr` from `FS:[0]`]: 64A100000000
[Bottom of SEH chain]: FFFFFFFF




##4 Stack Based Overflows (Windows Specific):
https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/



##5 Useful Info
 + DON'T TRUST WINDOWS CALC FOR HEX


##6 Offsets and JMPs

When exploit isn't working, you're offset is probably wrong


##7 Fuzzing
 + John Hammond video says to use `BooFuzz`


##9 SEH (Structured Exception Handlers)
https://www.corelan.be/index.php/2009/07/25/writing-buffer-overflow-exploits-a-quick-and-basic-tutorial-part-3-seh/
https://www.corelan.be/index.php/2009/07/28/seh-based-exploit-writing-tutorial-continued-just-another-example-part-3b/
https://resources.infosecinstitute.com/topic/buffer-overflow-vulnserver/



##10 Egghunters
 + PDF in resources folder (egghunt-shellcode.pdf)
   may not need to read this since it doesn't help in practice

 + https://www.corelan.be/index.php/2010/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/

 + url below also had pdf in resources

 [What is Egg hunter?]: https://www.secpod.com/blog/hunting-the-egg-egg-hunter/#:~:text=Egg%20hunter%20is%20a%20small,combining%20of%20two%20%E2%80%9CTAG%E2%80%9D.

  + 8 byte unique string made up of 2 TAGS
  + Unique so it won't come across itself while searching in memory
  + Placed just before the shellcode
  + Is placed in the small available buffer space while exploiting the overflows

  + Egg hunter is a small piece of shellcode which searches for an actual bigger shellcode
    which the attacker was not able to fit-in the available buffer space and redirect
    execution flow to it

  + The egg hunter code searches for an “EGG”


 [What is a TAG?]: https://www.secpod.com/blog/hunting-the-egg-egg-hunter/#:~:text=Egg%20hunter%20is%20a%20small,combining%20of%20two%20%E2%80%9CTAG%E2%80%9D.
  + Unique string of 4 bytes
  + Common TAGs: 'w00t' & 'lxxl'
 


##11 ASLR
 +  CTP covers ASLR
 +  Another resource:
    https://www.corelan.be/index.php/2009/09/21/exploit-writing-tutorial-part-6-bypassing-stack-cookies-safeseh-hw-dep-and-aslr/



##12 Restricted Characters
 + CTP has chapter on bad chars
 + https://www.youtube.com/watch?v=gHISpAZiAm0


##13 Mona
 + Learn how to use it
 https://www.corelan.be/index.php/2011/07/14/mona-py-the-manual/



##14 Shellcoding
 + Not EXPLICITLY covered in CTP, but good to know
 https://www.corelan.be/index.php/2010/02/25/exploit-writing-tutorial-part-9-introduction-to-win32-shellcoding/


Next up check out these guides in the order that they are listed.

https://www.fuzzysecurity.com/tutorials/expDev/6.html
http://sh3llc0d3r.com/windows-reverse-shell-shellcode-i/
http://www.vividmachines.com/shellcode/shellcode.html#ws



##15 Anti-Virus Evasion

 + Focus of CTP is EXPLOIT DEVELOPMENT
 + Anti-virus evasion is only a piece of that
 + CTP trick is a bit outdated, but still foundational



##16 Web Apps
 + LFI
 + XSS

Here are a couple of resources that I found useful in my research of the topic:

https://www.exploit-db.com/docs/40992.pdf
https://excess-xss.com/
https://www.veracode.com/security/xss
