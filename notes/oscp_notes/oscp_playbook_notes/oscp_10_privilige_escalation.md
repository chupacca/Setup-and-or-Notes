# Escalating Privliges 🛗

### DOOM EMACS - Inline Images
   1. Set the `config.el` as I have it
   2. `Ctrl-C + Tab` to import an image
   3. `Ctrl-C + Ctrl-X + Tab` to make images viewable

---------------------------------------------------------------
---------------------------------------------------------------

# LINUX 

### Linux: Table of Contents 
   1. DO YOU HAVE SUDO PRIVLIGES?
   2. Get information about the system
   3. Try using Linux Exploit Suggester 
   
- - - - - - - - - - - - - - - - - - - - - - - - - - - -

## 1) DO YOU HAVE SUDO PRIVLIGES?

1. If you have _sudo privliges,_ try making this bash file 
  ```escalate.sh
  #!/bin/bash 
  bash
  ```
 - Your'e essentially calling `sudo bash` to get _root shell_

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

## 2) Get information about he system
  + Observe _Information About the System_ section
    in `oscp_playbook_noates/oscp_3_useful_cmds.md`
    
- - - - - - - - - - - - - - - - - - - - - - - - - - - -

## 3) Try using Linux Exploit Suggester
   [Linux Exploit Suggester]: https://github.com/mzet-/linux-exploit-suggester


  + Clone the repo 
    `git clone https://github.com/mzet-/linux-exploit-suggester.git`
 
 
  + There should be a file names `linux-exploit-suggester.sh`
    - **Transport the file over**
      * See the `Transporting Files 📦` _section_ in the `oscp_playbook.md`
 
 
  + Run the file:
    - `chmod +x linux-exploit-suggester.sh && ./linux-exploit-suggester.sh`
 
 
  + Use one that _your system_ is **vulnerable against**
    - Like the `version number`
    - the _information about the system_ from the 
      **Get information about the system** step above (_STEP 2_)
 
 
  + `Linux Exploit Suggester` will **give you the name of the exploit**
    - Try _searching for the explit_
      * Observe _Searching for Exploit_ section
        in `oscp_playbook_noates/oscp_3_useful_cmds.md`
    
    
  + Once found, **transport the exploit over** and _RUN IT!_
    - See the `Transporting Files 📦` _section_ in the `oscp_playbook.md`
  
- - - - - - - - - - - - - - - - - - - - - - - - - - - -

---------------------------------------------------------------
---------------------------------------------------------------



# ===== BREAKLINE ===== #

# WINDOWS

### Windows: Table of Contents 
   1. 

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

---------------------------------------------------------------
---------------------------------------------------------------
