# Raspberry Pi Print Server Configurator

This repo contains configuration files for settings up a CUPS based printer on
a Raspberry Pi.  The print targeted is a Canon iP 1800.  It requires the
installation of the printer driver named `canonip1800.ppd`.  Use the CUPS web
interface for setting it up.

## Dev Setup

This project uses Ansible to configure the Raspberry Pi.  There are some
assumptions on how the Pi is configured:

1. It has a distribution of Raspbian installed
2. The IP address of the Pi is known
3. The control node running the Ansible code has SSH access to the pi
    1. Generate SSH key pair on PI
    2. Export public key to control node

Once the Pi is configured, setup the control node.  Run:

1. Update permissions: `chmod 744 create-venv.sh`
1. `./create-venv.sh`, this will setup the Ansible environment
2. In your shell run `./venv/bin/activate`
3. Add SSH key to agent `ssh-agent bash && ssh-add ~/.ssh/keypair.pem`
4. Run `install-print-server.py -n <IP Address of Pi>`

TODO: Add unattended updates to installation

## Old Installation

TODO: Remove/modify these instruction to describe the updated installation
process.

Run the shell script included in this repo.
```
sh setup_print_server.sh
```
It will:
1. Install and setup CUPS
2. Setup the CUPS user account
3. Install and setup nginx

### CUPS

Access the web service at:  `https://<Raspberry Pi address>:631`.
Please use the CUPS documentation for maintaining and setting up the service.

### nginx

Access the web page from:  `http://<Raspberry Pi address>`, it defaults to port 80.
This web page instructs Windows users on how to discover and connect to the printer for use.
