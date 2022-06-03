#!/bin/bash

# Install Packages in Arch based linux distros like Manjaro
sudo pacman -S open-vm-tools 

# Restart the service so screen fitting happens
systemctl stop vmtoolsd.service
systemctl start vmtoolsd.service
