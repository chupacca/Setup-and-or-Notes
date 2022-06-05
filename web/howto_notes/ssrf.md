
# Exploitng Regular / In-Band SSRF
  * [ ] Does the application allow **arbitrary user-supplied URLS**
   + If so, can you **specify a port number**
    - Try using `Burp Intruder` to port scan internal network
   + Attempt to connect to other services on the loopback address 
 + [ ] If you can't supply arbitrary URLS, can you bypass defenses
   
--------------------------------------------------------------------

# Black Box Testing
 + **Map** the application
  - Identify any request parameters that contain:
  ```
   * hostnames
   * IP
   * addresses for full URLs
  ```

 + For each request parameter, _modify its value_ to specify an `alternative resource` and observe how the appication responds
 + For each request parameter, _modify value to a server_ that **you control** and monitor the server for incoming requests
  - If **no incoming connections**, recieved, _monitor the time_ taken for app to respond
  
# White Box Testing
 + Review source code and identify _all request parameters_ that accept **URLS**
 + What **URL Parsers** are being _used_ and it can be _bypassed_
  - `New Era of SSRF by Orange Tsai`
 + Check if blacklist vs whitelist

--------------------------------------------------------------------

