# Useful Commands 💻

### Table of Contents 
1. Searching
2. Searching for Exploit 
3. Proving/Confirming I Have a Reverse Shell
4. Seeing What's Available to You 
5. Information About the System

-----------------------------------------------------------------
-----------------------------------------------------------------

## 1) Searching

**TOOLS**

+ `find`
+ `grep`
+ `silversearcher-ag`

+ `uniq` - pipe into uniq to get unique values

+ `awk`  - pipe into awk for pattern scanning
 - `-F valne`: sets the field seporator (like `-F:`)
  * `'{print $1}'` - prints the `first element` _after separating_
  * the _number_ after the `$` is the `index`


**EXAMPLES**

+ Example find directory/filename: `find /some/dir | grep <search>`
 -  like: `find . /grep controller`
 
+ Example Pipe Cmd: `grep [version_num] | awk -F: '{print $1}' | uniq`
  1. greps for a version number
  2. Pipe to `awk` to separate by `:` and only print index 1 
  3. Pipe to `uniq` for unique values

-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 2) Searching for Exploit
+ `searchsploit`
 - look at the _Exploit: Searching & Crafting 🪡_ section below

+ Check exploit-db.com
[Exploit-DB]: https://www.exploit-db.com


-----------------------------------------------------------------
-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 3) Proving/Confirming I Have a Reverse Shell
+ `whoami`
+ `id`
+ `crontab -l`

-----------------------------------------------------------------
-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 4) Seeing What's Available to You 
  + `$ which python` / `which python3`
  
-----------------------------------------------------------------
-----------------------------------------------------------------

## 5) Information About the System 

+ `whoami`
+ `pwd`
+ `cat /etc/lsb-release`

**Version of Tools**
+ `ldd --version`

-----------------------------------------------------------------
-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
