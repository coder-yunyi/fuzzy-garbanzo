#!/bin/sh
sudo pip3 install selenium
cd /home
sudo mkdir refresh
cd refresh
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo git clone https://github.com/coder-yunyi/fuzzy-garbanzo.git
export PATH=$PATH:/home/refresh/fuzzy-garbanzo/linux_amd64
cd ./fuzzy-garbanzo/linux_amd64
sudo python3 main.py
