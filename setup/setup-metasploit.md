[Setup]: Msfvenom_Setup (or just use supplied linux_x86_shellcode)
1. sudo add-apt-repository -y ppa:webupd8team/java
2. sudo apt update && sudo apt upgrade
3. sudo apt-get install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev curl zlib1g-dev gawk bison libffi-dev libgdbm-dev libncurses5-dev libtool sqlite3 libgmp-dev gnupg2 dirmngr
4. gpg2 --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
5. curl -L https://get.rvm.io | bash -s stable
6. rvm install "ruby-2.7.2"
7. source ~/.rvm/scripts/rvm
8. RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
9. rvm install $RUBYVERSION
10. rvm use $RUBYVERSION --default
11. cd /opt
12. sudo git clone https://github.com/rapid7/metasploit-framework.git
13. sudo chown -R `whoami` /opt/metasploit-framework
14. cd metasploit-framework
15. rvm --default use ruby-${RUBYVERSION}@metasploit-framework --create
16. gem install bundler
17. bundle install
18. sudo bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
19. echo "export PATH=$PATH:/usr/lib/postgresql/10/bin" >> ~/.bashrc
20. . ~/.bashrc
21. sudo usermod -a -G postgres `whoami`
22. sudo su - `whoami`
23. cd /opt/metasploit-framework/
24. ./msfdb init
25. gem install rex-text


Create shellcode binary: `msfvenom -p linux/x86/exec CMD="ls" R -o linux_x86_exec`
