# WEB PLAYBOOK 
### Table of Contents 
1.  Injection Attacks 
   + XSS
   + SQLi / NoSQLi
   + OS Command Injection 
   + XXE - Cross Site Entity Injection 
   + Directory Traversal 
2.  Server Side 
   + SSTI - Servier Side Template Injection
   + SSRF - Server Side Request Forger 
3.  Credentials Attacks
   + CSRF 
   + JWT Attacks 
   + OAuth 
   + PAM 
   + SSO - Single Sign On
4.  Authentication / Authorization 
   + Double Check Auth with Burp's `Autorize`
   + 2FA - 2 Factor Authentication 
   + Password Reset 
5.  CORS - Cross Origin Resource Sharing 
6.  HTTP Headers 
   + HTTP Request Smuggling 
   + HTTP Host Header Attacks
   + MIME Types / Media Types 
7.  Access Control
8.  Web Sockets 
9.  Web Cache
10. Insecure Deserialization
11. Disclosure Attacks
   + Information Disclosure 
   + Username Enumeration 
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
 **TOOLS**
 + Observe `useful_tools.md` _(3) BURP TOOLS -> XSS_
 + Observe `useful_tools.md` _(4) CLI - TOOLS -> 5 - Web App Testing Tools_
 
 **NOTES**
 + Observe _files inside_`xss/` directory
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    2 - SQLi / NoSQLi / GraphQL
#### + + + + + + + + + + + + + + + + + + + + + + + +
 + Observe `useful_tools.md` _(3) BURP TOOLS -> SQLi_
 + Observe `useful_tools.md` _(3) BURP TOOLS -> GRAPH QL_
 + Observe `useful_tools.md` _(4) CLI - TOOLS -> 5 - Web App Testing Tools_
###    3 - OS Command Injection 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
 **NOTES**
 + Observe _files inside_`cmd_inject/` directory
###    4 - XXE
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###    5 - Directory Traversal
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (2)  SERVER SIDE 
###   1 - SSRF - Server Side Request Forgery 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
 **TOOLS**
 + Observe `useful_tools.md` _(4) CLI - TOOLS -> 6 - Remote Server that I Control_
 **NOTES**
 + Observe _files inside_`ssrf/` directory
###   2 - SSTI - Server Side Template Injection 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = 
## (3)  CREDENTIALS ATTACK 
###   1 - CSRF
#### + + + + + + + + + + + + + + + + + + + + + + + + 
 **TOOLS**
 + Use Burp's `CSRF PoC`
 
 **NOTES**
 + Observe _files inside_`csrf/` directory
###   2 - JWT Attacks 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   3 - OAuth 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   4 - PAM 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   5 - SSO - Single Sign On
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (4)  AUTHENTICATION / AUTHORIZATION 
###   1 - Use Burp Plugin `Autorize` 
 **TOOLS**
 + Observe `useful_tools.md` _(3) BURP TOOLS -> AUTHORIZATION / AUTHENTICATION_
###   2 - 2FA - 2 Factor Autentication 
###   3 - Password Reset 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (5)  CORS - Cross Origin Resource Sharing 
 **NOTES**
 + Observe _files inside_`cmd_inject/` directory
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (6)  HTTP HEADERS 
###   1 - Http Request Smuggling 
###   2 - Http Host Header Attacks
#### + + + + + + + + + + + + + + + + + + + + + + + + 
###   3 - MIME TYPES / MEDIA TYPES
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (7)  ACCESS CONTROL 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (8)  WEB SOCKETS 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (9)  WEB CACHE 
###   1 - Web Cache Poisoning 
#### + + + + + + + + + + + + + + + + + + + + + + + + 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (10) INSECURE DESERIALIZATION 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (11) DISCLOSURE ATTACKS 
###    1 - INFORMATION DISCLOSURE 
###    2 - Username Enumeration 
### = = = = = = = = = = = = = = = = = = = = = = = = = = =
## (12) BUSINESS LOGIC 
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
