# WEB PLAYBOOK 
### Table of Contents 
1. Injection Attacks 
  + XSS
  + SQLi / NoSQLi
  + OS Command Injection 
  + XXE - Cross Site Entity Injection 
  + Directory Traversal 
2. Server Side 
  + SSTI - Servier Side Template Injection
  + SSRF - Server Side Request Forger 
3. Credentials Attacks
  + CSRF 
  + JWT Attacks 
  + OAuth 
  + PAM 
  + SSO - Single Sign On
4. Authentication / Authorization 
  + Double Check Auth with Burp's `Autorize`
  + 2FA - 2 Factor Authentication 
  + Password Reset 
5. CORS - Cross Origin Resource Sharing 
  + 
6. HTTP Headers 
  + HTTP Request Smuggling 
  + HTTP Host Header Attacks 
7. Access Control
  + 
8. Web Sockets 
  + 
9. Web Cache
  + 
10. Insecure Deserialization
  + 
11. Information Disclosure 
  + Username Enumeration 
  + 
12. Business Logic 
13. File Attacks
   + File Upload Vulnerabilities 
   + LFI - Local File Inclusion

## (1)  INJECTION ATTACKS
1. Do you have `source code` access?
  + If `yes`, look at methods that _process_ `user input`
   - Ideally you have `wrapper/beautifying functions`
  
2. Look/Assess **what context** `user input` _is inside_

  + If `user input` is something that gets put into the
    **Client's HTML** look for **XSS**
   - Look at the XSS section below: _1a : XSS_
- - - - - - - - - - - - - - - - - - - - - - - - -
###    1 - XSS
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    2 - SQLi / NoSQLi
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    3 - OS Command Injection 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    4 - XXE
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    5 - Directory Traversal
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    6 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (2)  SERVER SIDE 
###   1 - SSRF - Server Side Request Forgery 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   2 - SSTI - Server Side Template Injection 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = 
## (3)  CREDENTIALS ATTACK 
###   1 - CSRF
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   2 - JWT Attacks 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   3 - OAuth 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   4 - PAM 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   5 - SSO - Single Sign On
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   6 - @U
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   7 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   8 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (4)  AUTHENTICATION / AUTHORIZATION 
###   1 - Use Burp Plugin `Autorize` 
###   2 - 2FA - 2 Factor Autentication 
###   3 - Password Reset 
###   4 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (5)  CORS - Cross Origin Resource Sharing 
###   1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (6)  HTTP HEADERS 
###   1 - Http Request Smuggling 
###   2 - Http Host Header Attacks
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (7)  ACCESS CONTROL 
###   1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (8)  WEB SOCKETS 
###   1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (9)  WEB CACHE 
###   1 - Web Cache Poisoning 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (10) INSECURE DESERIALIZATION 
###   1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (11) INFORMATION DISCLOSURE 
###    1 - Username Enumeration 
###    2 - 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (12) BUSINESS LOGIC 
###   1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (13) FILE ATTACKS 
###    1 - File Upload Vulnerabilities 
###    2 - LFI - Local File Inclusion
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (14) 
###    1 - 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
 =
