#!/bin/bash
sudo apt-get update
sudo apt-get install python -y
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
pip3 install --user ansible
ansible --version

ansible-playbook -i inventory.cfg playbook.yml