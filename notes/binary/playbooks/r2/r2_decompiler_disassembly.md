
# DECOMPILERS (GHIDRA & DEC) & Disassembly
* From `r2ghidra` & `r2dec`

[Useful Link]: https://www.youtube.com/watch?v=hufgzz8nwNw

**===== Decompiler =====**

[Radare]: pdf
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdf     ; get radare's default decompilation
```

[Dec]: pdd
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdd     ; dec's decompilation
            ;  useful to SEE REGISTERS; like in BINJA
```

[Ghidra]: pdg
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> pdg     ; this will give you main method in ghidra
            ;   PSEUDO-CODE should appear too!!!
```
+ `pdg` : ghidra decompiler
 - Must run `r2pm -i r2ghidra-dec` on command line before using this
  * `pdg`  : Decompile current function with the Ghidra decompiler
  * `pdgd` : Dump the debug XML Dump
  * `pdgx` : Dump the XML of the current decompiled function
  * `pdgj` : Dump the current decompiled function as JSON
  * `pdgo` : Decompile current function side by side with offsets
  * `pdgs` : Display loaded Sleigh Languages
  * `pdg*` : Decompiled code is returned to r2 as comment


+ `pdo[N]` : convert esil expressions of N instructions to C (bytes for pdO)



**===== Disassembly =====**

  + `pD` --> print the disassembly
      ex) [0x00000000]> pD 0xdff ~0xc6
  + `pDf` --> print the disassembly of the function
      ex) [0x00000000]> pdf @0x000000ea

  + `pde[q|qq|j] [N]` -->  disassemble N instructions following execution flow from current PC
