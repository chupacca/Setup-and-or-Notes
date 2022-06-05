### TABLE OF CONTENTS 
1. APPLICATION 

2. BROWSER PLUGINS 

3. BURP TOOLS 
  + Authorization / Authentication 
  + Graph QL
  + Nice to Have / Quality of Life 
  + Race Condition / Timing 
  + SQLi 
  + XSS 
  
4. CLI TOOLS - COMMAND LINE TOOLS 
  + Docker (Pull)
  + Dependency Review 
  + Web App Code Review 
  + Web App Specific Language Review

------------------------------------------------------------------------
------------------------------------------------------------------------

# APPLICATION 

[App Any Run]: https://app.any.run/
+ This helps you `monitor` what else an `application` is _up to_
 - _networking_ done in backgroud
 - _file_ usage/storage
 - etc.

------------------------------------------------------------------------
------------------------------------------------------------------------

# BROWSER PLUGINS 

+ Cookie Editor (Firefox & Chrome)
+ Cookie Editor [Family] (Chrome)
 - Has a picture of a _family of cookies_

+ HackTools (Firefox & Chrome)
 - `useful things` like _payloads_
  * _XSS, Reverse Shells, etc._
  * Has `msfvenom`

+ Wappalyzer (Firefox & Chrome)
 - analyzes `web app` to find _what it's using_
 
------------------------------------------------------------------------
------------------------------------------------------------------------

# BURP TOOLS 

- - - - - - - - - - - - - - - - - - - - -

 **AUTHORIZATION / AUTHENTICATION**
+ Autorize
 - Helps **automate authorization findings**
 - Replaces `cookie values` from an _unprivileged_ user on a _privliged user_
 
+ Authz (_similar to Autorize_)

- - - - - - - - - - - - - - - - - - - - -

  **GRAPH QL**
+ InQL Scanner
+ InQl Timer

- - - - - - - - - - - - - - - - - - - - -

 **NICE TO HAVE / QUALITY OF LIFE**
+ HackVector
 - has a bunch of _useful functionality_
 - one use is `encoding and encoding`
 
+ Param Miner 
 - This extension identifies **hidden, unlinked parameters**
 - Particularly useful for finding _`web cache` poisoning vulnerabilities_

- - - - - - - - - - - - - - - - - - - - -

 **RACE CONDITION / TIMING**
+ Turbo Intruder
 - Complements `Burp Intruder` by handling attacks that requires 
   _extreme speed_ or _complexity_
   
- - - - - - - - - - - - - - - - - - - - -

 **SQLi**
+ SQLiPy "SQLMap Scanner"
 - Uses `sqlmap`

- - - - - - - - - - - - - - - - - - - - -

 **XSS**
+ XSS Validator
 
- - - - - - - - - - - - - - - - - - - - -

------------------------------------------------------------------------
------------------------------------------------------------------------

# CLI TOOLS - COMMAND LINE TOOLS

## Docker (Pull)
  [mpepping/cyberchef]: https://hub.docker.com/r/mpepping/cyberchef
   - Use `cyberchef functionality` _offline_


## Dependency Review
  [AppThreat/dep-scan]: https://github.com/AppThreat/dep-scan

- - - - - - - - - - - - - - - - - - - - -

## Web App Code Review
  [graudit]: https://github.com/wireghoul/graudit
  [semgrep]: https://github.com/returntocorp/semgrep
  [silversearcher-ag]: https://github.com/ggreer/the_silver_searcher

- - - - - - - - - - - - - - - - - - - - -

## Web App Specific Language Review

 **GO**
  [gosec]: https://github.com/securego/gosec
   - `Go` security review
  [gokart]: https://github.com/praetorian-inc/gokart
   -  `Go` security review
   
 **JAVASCRIPT**
  `npm audit`
   - `Javascript` security review

 **PYTHON**
  [bandit]: https://bandit.readthedocs.io/en/latest/start.html
   - `Python` security review
   
 **RUBY**
  [brakeman]: https://github.com/presidentbeef/brakeman
   - `Ruby on Rails` security review

- - - - - - - - - - - - - - - - - - - - -

## Web App Tools 

[sqlmap]: https://github.com/sqlmapproject/sqlmap
[xsshunter]: https://github.com/mandatoryprogrammer/xsshunter-express

- - - - - - - - - - - - - - - - - - - - -

---------------------------------------------------------
---------------------------------------------------------

 