# Enumeration: Network Scanning 🌐
* Try to hold scan results in a _separate directory_

### Table of Contents 
1. Network Enumeration 
  + Rustscan 
  + NMAPAUTOMATOR 
  + autorecon 

3. Nmap
4. Wireshark / tcpdump
5. DNS Enumeration 
6. SMB Enumeration 
7. Subdomain Enumeration

8. Network Sniff for Password/Hashes 
9. Active Directory Enumeration 

- - - - - - - - - - - - - - - - - - - - - -

* To look at: 
redhawk (enumeration): https://latesthackingnews.com/2018/11/21/red-hawk-open-source-information-gathering-and-vulnerability-scanning-tool/

* Deprecated:
 + Sparta (use nmapAutomator instead)
 + Masscan (use rustscan instead)

----------------------------------------------------------------------
----------------------------------------------------------------------

### + + + + + + + + + + + + + + + + + + + + + +
## (1) Network Enumeration 

###   1 - RUSTSCAN
#### Installation & Setup 
  + Docker
    ```Debian_Installation
    sudo apt install -y docker.io
    sudo systemctl enable docker --now
    sudo usermod -aG docker $(whoami)
    sudo chmod 666 /var/run/docker.sock
    docker pull rustscan/rustscan:2.0.0
      + Don't use sudo 
    ```
   - Docker Status: `sudo systemctl status docker`
   - Execution
     ```Docker_Execution_Options 
     docker run -it --rm --name rustscan rustscan/rustscan:2.0.0 \
        <rustscan arguments here> <ip address to scan>
        
     alias rustscan='docker run -it --rm --name rustscan \ 
                    rustscan/rustscan:2.0.0'
     ```
   
  + Source: From Source Code 
    ```DebianLinux_Installations 
    curl https://sh.rustup.rs -sSf | sh
        + Use _1_ for default installation 
        + cargo will be install with it 
    git clone https://github.com/RustScan/RustScan.git
    cd RustScan 
    cargo build --release
    ./resease/rustscan 
    ```
   - Execution: `cd RustScan/release/rustscan`
   
  + MacOS Installation: `brew install rustscan`
   
   
#### USAGE
Reference: https://github.com/RustScan/RustScan/wiki/Things-you-may-want-to-do-with-RustScan-but-don't-understand-how
   
   + One IP Address: `rustscan -a <IP>`
   + Multiple IP Addresses: `rustscan -a <IP>/24`
#### - - - - - - - - - - - - - - - - -
###   2 - NMAPAUTOMATOR
#### Installation & Setup 
Installation Guide: https://linuxhint.com/nmapautomator/
   
```Install_Dependencies_Involving_GO:
    # Download go tar from https://go.dev/doc/install
    cd ~/Downloads 
    sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.#.#.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    
    # Since `go get` is depreceated, USE THIS: 
    go install github.com/OJ/gobuster@latest
```
```Install_DebianLinux_Dependencies
    sudo apt install -y smtp-user-enum nmap libwhisker2-perl nikto
    reboot 
    cd /tmp
    git clone https://github.com/vulnersCom/nmap-vulners.git
    cd nmap-vulners
    cp *.nse /usr/share/nmap/scripts
```
```Install_nmapAutomator 
    cd $tools 
    git clone https://github.com/21y4d/nmapAutomator.git
    sudo ln -s $(pwd)/nmapAutomator/nmapAutomator.sh /usr/local/bin/
    cd nmapAutomator
    chmod +x nmapAutomator.sh
    ln -s nmapAutomator.sh /usr/local/bin
```
   
----------------------------------------------------------------------
#### Usage 
Usage Guide: https://linuxhint.com/nmapautomator/
```Usage_Examples:
   sudo ./nmapAutomator <IP> all
   sudo ./nmapAutomator.sh 64.91.238.144 Full
   sudo ./nmapAutomator.sh 64.91.238.144 Recon
   sudo ./nmapAutomator.sh 64.91.238.144 Quick
   sudo ./nmapAutomator.sh 64.91.238.144 Basic
   sudo ./nmapAutomator.sh 64.91.238.144 UDP
   sudo ./nmapAutomator.sh <Target> Vulns
```
   
#### - - - - - - - - - - - - - - - - -
###   3 - AUTORECON 
autorecon: https://latesthackingnews.com/2019/08/04/autorecon-an-open-source-enumeration-tool/
#### - - - - - - - - - - - - - - - - -
###   4 - NMAP

#### Nmap Table of Contents
   1. Basic NMAP Scans 
   2. Subdomain NMAP Scans 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#### 1: Basic NMAP Scans

```Basic_Nmap_Scan_From_ITSecurityLabs
nmap -sV -sC -T4 -p- -oA nmap
```
```Basic_Nmap_Scan_From_Ippsec
nmap -sV -sC -vvv -oA nmap/initial $IP
```
* -sC : --script=default
* -sV : probe open ports to determine * service
* -oA <basename> : output in 3 major formats at once
* -T <#> : set timing (0-5); higher is faster
* -vvv: for verbose output

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#### 2: Subdomain NMAP Scans

```Subdomain_Scanning
# Stealthy
nmap -sS 10.11.1.X
-sS : will send first syn and wait for syn-ack

# Scan all ports, might take a while.
nmap 10.11.1.X -p-

# Scan for UDP
nmap 10.11.1.X -sU
unicornscan -mU -v -I 10.11.1.X

# Scan for version, with NSE-scripts and trying to identify OS
nmap 10.11.1.X -sV -sC -O

# All out monsterscan
nmap -vvv -Pn -A -iL listOfIP.txt

# Fast scan
nmap 10.11.1.X -F

# Only scan the 100 most common ports
nmap 10.11.1.X --top-ports 100

```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

----------------------------------------------------------------------
----------------------------------------------------------------------

#### - - - - - - - - - - - - - - - - -
### + + + + + + + + + + + + + + + + + + + + + +
## (2) WIRESHARK / TCPDUMP 
+ If **Wireshark is available**, open it and see what `IP`s are
  communicating with your machine
 - Or try **install it**

----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
## (3) DNS ENUMERATION 

**nslookup**
**dig**
**dnsenum**

----------------------------------------------------------------------
----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
## (4) SMB ENUMERATION 

  **WINDOWS**

  **LINUX**

----------------------------------------------------------------------
----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
## (5) SUBDOMAIN ENUMERATION 

subfinder: https://latesthackingnews.com/2021/01/23/subfinder-a-subdomain-discovery-tool/

turbolist3r: https://latesthackingnews.com/2019/12/04/turbolist3r-an-automated-subdomain-scanning-tool/

knock: https://latesthackingnews.com/2018/11/30/knock-open-source-subdomain-scanner-tool/

+ Look at `NMAP` section above (_2: Subdomain NMAP Scans_)

----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
## (6) Network Sniff for Password/Hashes 

net-creds: https://latesthackingnews.com/2018/08/24/net-creds-open-source-tool-to-sniff-network-passwords-and-hashes/

----------------------------------------------------------------------
----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
## (7) ACTIVE DIRECTORY ENUMERATION 

**Bloodhound**
bloodhound: https://latesthackingnews.com/2018/09/25/bloodhound-a-tool-for-exploring-active-directory-domain-security/

----------------------------------------------------------------------
### + + + + + + + + + + + + + + + + + + + + + +
 =
