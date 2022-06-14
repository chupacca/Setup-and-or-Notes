# OSCP PLAYBOOK

### Files to pair this playbook with

**LOOK AT a_youtube_notes.md**

### Other OSCP Guides

[OSCP Guide Referenced]: https://sushant747.gitbooks.io/total-oscp-guide/content/port_scanning.html

- - - - - - - - - - - - - - - - - - - - - -

### Tools OSCP said I Can Use
BloodHound
SharpHound
PowerShell Empire
Covenant 
Powerview
Rubeus
evil-winrm
Responder (Poisoning and Spoofing is not allowed in the labs or on the exam)
Crackmapexec
Mimikatz
 
### Table of Contents
1.  Enumeration: Network Scanning 🌐
2.  Web Stuff: Enumeration 🕸️
3.  Web Stuff: Exploitation 🕸️
4.  PRIVESC 🛗: Once You Have a Shell 🪜

5.  Reverse Shell - How to GET IT 🐢
6.  You have SHELL🐢😊 ... NOW WHAT ❓ 
7.  I AM ROOT 🌳 What's Next? 🦝
8.  Pivoting 🔄 ↓↳

9. Transporting Files 📦

- - - - - - - - - - - - - - - - - - - - - -

**!!! KEEP NOTES ON EVERYTHING YOU DO !!!**
 = try cherrytree or doom emacs for oscp =

- - - - - - - - - - - - - - - - - - - - - -

### + + + + + + + + + + + + + + + + + + + + + + +
## 1) Enumeration: Network Scanning 🌐
* ALWAYS DO **ENUMERATION IN BACKGROUND** _while working on other things_
* Stuck? **Do More Enumeration**
* Assuming you're already connected to the VPN
* I'm also assuming you're just starting at a VM

- - - - - - - - - - - - - - - - - - - - -

1. Run `ifconfig, ipconfig, or ip addr` to see what IP subnet you're in

  + We're going to target the **last octet** of your IP address
   -  So if `10.11.1.12`, then we're targeting where the `12`

- - - - - - - - - - - - - - - - - - - - -

2. Use `network scanning` / `Subdomain_Scanning` / etc

  + Look at:
    `oscp_playbook_notes/oscp_4_enmeration_network_scan.md`
    
  + When doing _Network Scanning_ hold results in a _separate directory_

- - - - - - - - - - - - - - - - - - - - -

3. Have one scanner doing _fast scan_ and another doing _in depth scan_
Example: https://www.youtube.com/watch?v=M4J0tH5vk_k
  + `Rustscan` for the fast scan 
  + `nmapautomator` for in depth scan

- - - - - - - - - - - - - - - - - - - - -

4. **CONDITION: `Port 80 or 443 Open?`:** Try opening it in a **browser**
  + Go to the **Web Stuff: Enumeration 🕸️** section below

- - - - - - - - - - - - - - - - - - - - -

--------------------------------------------------------------
--------------------------------------------------------------


## 2) Web Stuff: Enumeration 🕸️
* Make sure to have _Burp_ proxying setup 
* You can try Yuki: https://latesthackingnews.com/2018/10/12/yuki-chan-the-auto-web-penetration-testing-tool/

1. When _first visting the site_
  + Have `proxy` _intercept off_ initially, but have it collecting traffic
   - You may want to look through it later 
    * Make sure to have `filters on` **Burp**
    
   - Send `interesting requests` to **Burp Repeater**
    * `KEEP NOTES` about _which request is what_
    
   - **vvv CHECK IF THIS TOOL IS BANNED vvv**
       Use the `Wappalyzer` _plugin_ to analyze the website
     **^^^ CHECK IF THIS TOOL IS BANNED ^^^**

- - - - - - - - - - - - - - - - - - - - - -

2. Things to look for in `response`
  + Look for any _comments/hints_ in the `respone`
  + Check if the _response_ has a `Server header` and see if it 
    tells you about the _what service_ it's using (like apache)
   * You can use that to _figure out what version of linux_ is used 
   * In cause you didn't find this in the nmap scan

- - - - - - - - - - - - - - - - - - - - - -

3. Try using `Burp` or `dirbuster` to find directories in the 
   _webserver_

- - - - - - - - - - - - - - - - - - - - - -

4. See if there's a label like `Power by <product>` or `©`
  + Try to **GOOGLE** the _product or resource_
   - Kind of like `googling Nibbleblog` when seeing `Powerd by Nibbleblog`
    * See if it's **open source** so you can see the **source code**
    * Look at the _Searching_ secion in 
      `oscp_playbook_notes/oscp_3_useful_cmds.md`
    
  + `Source code` can reveal `embedded files, directories, etc`
   - like _/nibbleblog/admin/boot/rules/98-constants.bit_
   
  + **Keywords** to look for in `source code`
    (filenames,dir,contents,etc.):
   - `admin`
   - `user` / `users`
   - `update`
   - version numbers
   
  + See if there's **documentation**
   - It may hold the **default password**

- - - - - - - - - - - - - - - - - - - - - -

5. Try _playing around_ with the **URL**
  + Try adding in the `=users&id=1`
   - like: `https://10.10.10.75/nibbleblog/index.php?controller=users&action=view&id=1`

- - - - - - - - - - - - - - - - - - - - - -

6. If you see _login functionality_ look at the **Login Exploitation**
   in the _Web Stuff: Exploitation 🕸️_ section below
   
- - - - - - - - - - - - - - - - - - - - - -

7. **Look up vulnerabilities**
  + `searchsploit` can be used
   - Look at _Searching for Exploit_ seciont in
     `oscp_playbook_notes/oscp_3_useful_cmds.md`

- - - - - - - - - - - - - - - - - - - - - -

--------------------------------------------------------------
--------------------------------------------------------------

## 3) Web Stuff: Exploitation 🕸️

**Login Exploitation**

1. Guessing password 
  + `admin`
  + the name on the website (or some variation)
  
2. SQLi 
  + look at my _sqli notes_ in the `web/howto_notes`

2. Brute Force
  + **BEWARE YOU MAY END UP LOCKING YOURSELF OUT**
   - service may ban your IP 
   - Look at _Getting Around IP Bans_ section in
     `oscp_playbook_notes/oscp_8_tips_N_tricks.md`
   
  + `hydra` can be used to _brute force_
   - Look at _Brute Force_ section in
     `oscp_playbook_notes/oscp_5_exploit_web.md`

- - - - - - - - - - - - - - - - - - - - - - - - - - -

**File Upload**

1. First try _uploading a test file_ that'll execute code 
  + Maybe try this out:
    ```Mabye_Try_This:cmd.php
    GIF8;
    <?php echo system($_REQUEST['mycmd']); ?>
    ```
   - Putting something like **GIF8;** at the top of the file
     can help **evade** _file checking service_


  + If I can access this file from a _broswer/url_ I can hit it with
    `?mycmd=whoami`
   - You can inject a different cmd _like on to get reverse shell_
    * See the **Reverse Shell - Getting IT 🐢** section below
   [Example Url]: 10.10.10.73/nibbleblog/private/plugins/my_image/cmd.php?mycmd=whoami

--------------------------------------------------------------
--------------------------------------------------------------

## 4) PrivEsc 🛗: Once You Have a Shell 🪜
  
1. Visit `oscp_playbook_notes/oscp_10_privilige_escalation.md`
   for _details_
  + You may need to **transport files**
   - See the `Transporting Files 📦` _section below_

2. Try to get a reverse shell 🐢

-----------------------------------------------------------------
-----------------------------------------------------------------

## 5) Reverse Shell - How to GET IT 🐢
 + You may need to **transport files**
  - See the `Transporting Files 📦` _section below_
   
   
[Reverse Shell Cheat Sheet]: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

1. Try the different reverse shells in:
  + the above cheat sheet
  + or, the _Reverse Shell_ section in **1_youtube_notes.md**

2. Try _copying and pasting_ a `reverse shell source code` you have:
  + Like `php-reverse-shell.php`
  + Can copy the files over like in _STEP 2_ in the **2) Privesc** section above
  
3. Try _overwriting_ a **local executable** (like `python`) to be a _reverse shell_
  + Look at the _Reverse Shell_ section in **1_youtube_notes.md**
   - `Python` has a _command line_ & _code_ versions

4. If _none work_, try looking at configurations
  + If I _used a `script`_ to get a `shell`, **double check the script**


-----------------------------------------------------------------
-----------------------------------------------------------------


## 6) You have SHELL🐢😊 ... NOW WHAT ❓

1. See what's **available to you**:
  + Observe _See What's Available to Young's_ section
    in `oscp_playbook_noates/oscp_3_useful_cmds.md`
 
2. Get **information about he system**
  + Observe _Information About the System_ section
    in `oscp_playbook_noates/oscp_3_useful_cmds.md`
 
2. Check **privliges**
  + `$ sudo ls` - do i have sudo permissions?
 
3. See if you can **escalate privliges**
  + See the `PrivEsc 🛗: Once You Have a Shell 🪜` _section above_
   - You may need to _transport files_
    * See the `Transporting Files 📦` _section below_
 
4. Do some **network scanning**
  + See the `Enumeration: Network Scanning 🌐`
    section above
 
5. Try _pivoting_
  + See the `Pivoting 🔄 ↓↳` section below
  
6. See if you can **transport file in**
  + Is there a `file` that _can be helpful?_
  + See the `Transporting Files 📦` _section below_
 
--------------------------------------------------------------
--------------------------------------------------------------
 
## 7) I AM ROOT 🌳 What's Next? 🦝

* Do some _network scanning_
 + See the `Enumeration: Network Scanning 🌐` section above

**Linux**

1. Try _appending to_ `/etc/hosts` with something you control
  + `echo $IP $USERNAME >> /etc/hosts`

--------------------------------------------------------------
--------------------------------------------------------------

## 8) Pivoting 🔄 ↓↳ 

**POTENTIAL OPTIONS (MAY NOT BE UP TO DATE)**
   * Double check w/ `oscp_9_pivoting.md`
     ```OPTIONS
         1. Port Forwarding With SSH
     ```   

- - - - - - - - - - - - - - - - - - - - - - - - -

 + Observe `oscp_playbook_notes/oscp_9_pivoting.md` 
   for **more details**
   
--------------------------------------------------------------
--------------------------------------------------------------

## 9) Transporting Files 📦

**POTENTIAL OPTIONS (MAY NOT BE UP TO DATE)**
   * Double check w/ `oscp_11_transport_files.md`
     ```OPTIONS
         1. Copy & Paste 
         2. Python WebServer 
         3. SCP (through SSH)
     ```

- - - - - - - - - - - - - - - - - - - - - - - - -

 * For **more details,** visit the _Transport Files 📦_ 
   section in:
   `oscp_playbook_notes/oscp_11_transport_files.md`


--------------------------------------------------------------
--------------------------------------------------------------

