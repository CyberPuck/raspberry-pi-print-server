#!/bin/bash
# Script for setting up a printer server and support webserver for user instructions

# ------ PRINTER setup ------
echo Installing CUPS
# Install CUPS
sudo apt isntall cups

# create printer user
useradd printer
sudo passwd printer
# add printer account to the user group
sudo usermod -a -G lpadmin printer
# update cups config
sudo cp cupsd.conf /etc/cups/cupsd.conf
# restart CUPS
sudo /etc/init.d/cups restart

# ------ Web server setup ------
echo Installing nginx
# Install nginx
sudo apt install nginx

# move website to /www/data
sudo cp -r ./ /www/data/

# update nginx.conf
sudo cp nginx.com /etc/nginx/nginx.conf

# update sites folder
sudo cp helper-site /etc/nginx/sites-available/helper-site

# restart nginx
sudo nginx -s reload

echo Script completed