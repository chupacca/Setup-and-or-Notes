# Enumeration: Network Scanning 🌐
* Try to hold scan results in a _separate directory_

### Table of Contents 
1. Rustscan 
2. NMAPAUTOMATOR 
3. Nmap
4. Masscan (use rustscan instead)
5. Wireshark
6. DNS Scanning

----------------------------------------------------------------------
----------------------------------------------------------------------

## 1) RUSTSCAN

  + Docker Installation
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

  + Linux
    ```Debian_Installations 
    curl https://sh.rustup.rs -sSf | sh
        + Use _1_ for default installation 
        + cargo will be install with it 
    git clone https://github.com/RustScan/RustScan.git
    cd RustScan 
    cargo build --release
    ./resease/rustscan 
    ```
   - Execution: `cd RustScan/release/rustscan`

  + Other Installation Rust
   - MacOS:   `brew install rustscan`

----------------------------------------------------------------------
----------------------------------------------------------------------

## 2) NMAPAUTOMATOR

----------------------------------------------------------------------
----------------------------------------------------------------------

## 3) NMAP

### Nmap Table of Contents
   1. Basic NMAP Scans 
   2. Subdomain NMAP Scans 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**1 - Basic NMAP Scans**

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

**2 - Subdomain NMAP Scans**

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

## 4) MASSSCAN

**USE RUSTSCAN INSTAEAD** 

```Basic_Masscan
masscan -p22,80,445 192.168.1.0/24
```

----------------------------------------------------------------------
----------------------------------------------------------------------

## 5) WIRESHARK 
+ If **Wireshark is available**, open it and see what `IP`s are
  communicating with your machine
 - Or try **install it**

----------------------------------------------------------------------
----------------------------------------------------------------------

## 6) DNS SCANNING 

**nslookup**
**dig**

----------------------------------------------------------------------
----------------------------------------------------------------------

## 7) SMB Enumerations 

  **WINDOWS**

  **LINUX**

----------------------------------------------------------------------
----------------------------------------------------------------------

