# Raspberry Pi Print Server Configurator
This repo contains configuration files for settings up a CUPS based printer on a Raspberry Pi.
The print targeted is a Canon iP 1800.  It requires the isntallation of the printer driver
named ```canonip1800.ppd```.  Use the CUPS web interface for setting it up.

# Installation
Run the shell script included in this repo.
```
sh setup_print_server.sh
```
It will:
1. Install and setup CUPS
2. Setup the CUPS user account
3. Install and setup nginx

## CUPS
Access the web service at:  ```https://<Raspberry Pi address>:631```.
Please use the CUPS documentation for maintaining and setting up the service.

## nginx
Access the web page from:  ```http://<Raspberry Pi address>```, it defaults to port 80.
This web page instructs Windows users on how to discover and connect to the printer for use.