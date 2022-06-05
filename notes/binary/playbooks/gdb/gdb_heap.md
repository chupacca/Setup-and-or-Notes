### TABLE OF CONTENTS
1.  context
2.  print
3.  ptype
4.  vmmap
5.  top_chunk
6.  bins
    + large bins
    + small bins
    + unsorted bin
    + fastbins
7.  dq mp_.sbrk_base
8.  vis
9.  dq
10. db
11. xinfo
12. arena/arenas
13. find_fake_fast

14. GEF


### ================================= ###
###              PWNDBG               ###
### ================================= ###


**===== context - only portion =====**
* Only show source code or context section: `pwndbg> set context-sections code`



**===== print value =====**
+ In `pwndbg`: `p <variable>`
 - Example: `p a` <--- variable name is a
 - Example: `p __malloc_hook` <-- print value of a function pointer

 - Print a `malloc_chunk struct`
   `pwndbg> p *((struct malloc_chunk*)<address>).fd`
   `pwndbg> p *((struct malloc_chunk*)0x60310).fd`
  
 

**===== ptype =====**
+ Print a structure or print the type it is
+ Use: `ptype <variable/address>`
Example:
```
pwndbg> ptype user
type = struct user {
    char username[16];
    char target[16];
}
```
+ can also use `dq &<variable>`

 
 
**===== vmmap =====**
+ Use `pwndbg`'s `vmmap` to see if _heap_ has been _allocated_

+ Takes an argument to filter results
 - Example: `vmmap libc`



**===== top_chunk =====**
+ See info related to the _top chunk_
```Example
pwndbg> top_chunk
Top chunk
Addr: 0x602000
Size: 0x1019       ; it's really big cause i overwrote it
```



**===== bins =====**
+ Get all the `bins` that are associated with this heap

  * [ ] **largebins**
  
    ----------------------------------------
    
  * [ ] **smallbins**
  
    ----------------------------------------
    
  * [ ] **unsortedbin**
       + OTHER CMD: `dq &main_arena 16` and look at _last 2 quadwords_
       
       + Only _one per arena_
        - `head of chunk` is in heap's _arena_
        
       + Has a `forward pointer` & a `backward pointer` to make _doubly linked circular list_
        - The `last chunk's` fd pointer _should point back to the_ `Unsortedbin Head`
      
       + _Newly freed chunks_ added to the **HEAD of unsortedbin**
        - adjacent free chunks are consolidated
       + _Allocated chunks_ are allocated **from the TAIL of the unsortedbin** 
      
       + holds chunks of _any size_
      
    ----------------------------------------
    
  * [ ] **fastbins**
       + Gets the `fastbins` with size between _0x20~0x80_
       + Null (_0x0_) means the bin is empty
       
       + Note that if I want something in the _0x70_ `fastbin`
        - I have to `malloc` _0x68_ bytes because _8_ bytes are reserved for the chunk size
         * It's hex so: _0x68 0x69 0x6a 0x6b 0x6c 0x6d 0x6e 0x6f_

       + _Newly freed chunks_ added to the **HEAD of fastbin**
       + _Allocated chunks_ are allocated **from the HEAD of the fastbin** (what's in the fastbin)




**===== dq mp_.sbrk_base # =====**
+ A `vis` alternative if _I corrupted the heap_



**===== vis =====**
+ Use `pwndbg`'s `vis_heap_chunks` or `vis` to see _heap chunks_

+ Usually the first link will have a **size**
 - Each chunk has a `size field`
```                                                     v--size_here
0x602000        0x0000000000000000      0x0000000000000021      ........!.......
  [...]
0x602060        0x0000000000000000      0x0000000000000021      ........!.......
  [...]
0x602080        0x0000000000000000      0x0000000000000031      ........1....... 
  [...]
0x602060        0x0000000000000000      0x0000000000020fa1      ................    <-- Top chunk
```

+ After the _size_, you should see the **userdata**
```                  userdata_is_YYYY_or_595959
0x603000        0x0000000000000000      0x0000000000000021      ........!.......
0x603010        0x0000000a59595959      0x0000000000000000      YYYY............
0x603020        0x0000000000000000      0x0000000000020fe1      ................    <-- Top chunk
```



**===== dq =====**
+ Dumps _quadwords_

+ Use with _variable names_: `dq <variable-name>`  OR  `dq &<variable-name>`
+ Address use: `dq 0x<address>`
+ Can do math operations in argument: `dq target-16`

+ Gdb does pointer math depending what you pass it:
 - example: `dq &__malloc_hook-2`

+ See _arenas_ :
 - `dq &main_arena 14` -> see fastbins in qwords (1 means beginning of fastbins)

**===== db =====**
+ Dumps _bytes_

+ example `db &_malloc_hook-4`
 - pwndbg usually shows bytes in reverse order, but keep in mind things are in little endian
  * this means dq is good for seeing things as they are in memory
  


**===== xinfo =====**
+ Get information about target
+ Confirm which section it resides in (_like the .data section_)

+ Use: `xinfo <variable/address>`



**===== arena/arenas =====**
+ print things related to arenat
+ can also do `dq &main_arena #` like `dq &main_arena 20`



**===== find_fake_fast &<variable/address> =====**
+ prints locations of fake chunks that overlap the target address


-------------------------------------------------------------------------


### ================================= ###
###                GEF                ###
### ================================= ###

### Arenas (when multithreading)
	gef> heap arenas


### Chunk
	gef> heap chunks <location>
