[word]: 16 buts

[dword]:  32 bits

[dword ptr]: _
 + Example: `dword ptr [ebp-4]`
    - "the size of the target operand is 32 bits"

---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------

http://www.cplusplus.com/forum/general/185764/

DWORD is a typedef for, as you mentioned, 'double word' sized integers. It's a way of sizing them, rather than giving bit numbers.

They are useful, because that way you know you have, for example, x bits worth of space to store information in. On the other hand, just using int means that you might have x, but you could just as well only have less than x bits of data (depending on the compiler and target architecture).

EDIT:
Actually, I just did some more reading and it turns out I was kind of wrong :)

See this: https://en.wikipedia.org/wiki/Word_(computer_architecture)

Basically, the gist of it is that a WORD is traditionally the size of a memory pointer, the 'most natural' size of data that can be read. DWORD is twice that size, QWORD is four times, etc.

Now, traditionally that would be 16 bits of data; a legacy to the 16 bit MSDOS days. Nowadays, though, it's generally 32 bit or 64 bit, according to your computer's architecture. So, really, a DWORD on modern computers should be 128 bit!

However, for 'backwards compatibility reasons', the size of each has stayed the same. So, the WORD type is 16 bits, even though it technically should be 64 bits, like a computer word.

TLDR; what I wrote above is technically correct, just not for the reasons I gave.

Also, I should have mentioned that typically you shouldn't use them; they're rather obscure and only really make sense to use if you're interfacing with the WinAPI.
