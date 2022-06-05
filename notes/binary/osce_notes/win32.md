* Every Windows process has an executive process (EPROCESS)

[EPROCESS]: Structure that has process attributes/pointers to related data structures
  - Mostly in kernel
  - Some in PEB (process environment block)


[PEB]: Process-Environment-Block
 + Has varioius user-mode paramters about a running process
 + Some paramters are:
  - base address of image (executable)
  - location of heap
  - DLLs (loaded modules kind of like `.so` in Linux)
  - Environmental variables (OS, relevatn patchs, etc)

 + Process has primary thread and can have additional threads
 + Each thread has it's own TEB (thread environment block)

[TEB]: Thread-Environment-Block
 + Stores context info for:
  - image loader
  - various Windows DLLS
  - location of the exception handler list

[DLL]:
 + Like `.so` files in Linux
  - modules
 + Allow for efficient code reuse and memory allocation
