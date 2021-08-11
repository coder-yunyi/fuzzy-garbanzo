#!/bin/sh

sudo pip3 install selenium
cd /home
sudo mkdir refresh
cd refresh
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo wget https://cdn.jsdelivr.net/gh/coder-yunyi/fuzzy-garbanzo@main/linux_amd64/main.py
sudo wget https://cdn.jsdelivr.net/gh/coder-yunyi/fuzzy-garbanzo@main/linux_amd64/chromedriver
export PATH=$PATH:/home/refresh
sudo python3 main.py
