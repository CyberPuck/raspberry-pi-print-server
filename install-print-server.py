# Script for installing the Printer Pi, this requires knowing the IP address of
# the Pi being configured.  This script will:
# 1. Generate the inventory file based on user input
# 2. Call the Ansible playbook `setup-printer.yaml`

import argparse
import subprocess


def setup_parser():
    parser = argparse.ArgumentParser(prog = "install-print-server",
                        description = "Generates an inventory file that is run by an Ansible playbook to configure a print server")
    parser.add_argument('-n', '--network', help='IP Address of the Pi print server', required=True)
    parser.add_argument('-i', '--inventory', help='Name of the inventory file', default='inventory.yaml')
    return parser.parse_args()

# Given a file_name (inventory file) and ip_address of a networked pi,
# generate an inventory file that will be used by Ansible.
def generate_inventory_file(file_name, ip_address):
    with open(file_name, 'w') as inventory_file:
        inventory_file.write("---\nall:\n\thosts:\n\t\tprinter: " + ip_address + "\n")

# Start up Ansible playbook to run the setup and configuration.
# The file_name is expected to be the inventory file.
def start_ansible(file_name):
    subprocess.run(['ansible-playbook', 'setup-printer.yaml', '-i', file_name])

if __name__ == "__main__":
    args = setup_parser()
    generate_inventory_file(args.inventory, args.network)
    print("Then run playbook with: " + args.inventory)
