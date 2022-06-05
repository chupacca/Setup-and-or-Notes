# Quick Start

1. Run radare
  + `r2 <binary>`          run radare on binary
  + `r2 -AAA <binary>`     run radare and analyze binary
  + `r2 -w -AAA <binary>`  run radare with write permission
  + `r2 -zz <binary>`      load strings
  + `r2 -z <binary>`       DO NOT load strings
  + `r2 -q <binary>`       quiet mode (no prompt) and quit after -i (running script file)
  + `r2 -a <architecture> <binary>` load a specific architecture

2. Intial commands to run in radare
```
[]> aaaa    ; analyze binary

[]> s main      ; seek to main function
       OR
[]> s entry0	; this should get to the entry function

       
# Quick reference to other commands I don't really reference this document
[]> clear   ; clears terminal
[]> a?      ; get list of commands

[]> s <function_Or_address>  ; goes to that function/address
                             ; you should see address change b/w brackets

[]> afl     ; see functions
[]> axt     ; cross reference where we are
[]> axt @ @ str.*  ; cross references for all strings

[]> afv         ; see local variables

[]> iI      ; see plugin details
[]> is      ; see symbols
[]> ii      ; see import
[]> iE      ; get export
[]> iz      ; strings in data section

[]> iS entropy   ; Get entropy for each section
                 ; You get high entropy like 7 if this is
                 ;   packed/compressed/encrypted

[]> pd 1@<function_Or_address>   ; print 1 line of disassembly at address
```

