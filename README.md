# ansible-project
sample code for dynamic inventory

Prerequisites
- Python
- Ansible
- PIP
- Ansible Playbook

Download or Clone the project on linux machine. Add or delete or Modify entries in hosts.csv file.

Try running the following commands as a sudo user. Ensure that you manually delete all temp files created in your working directory, during each fresh run.
$sudo ansible all -m ping -i flag1.py

$./flag1.py --list

$sudo ansible-playbook Playbook.yml -i flag1.py --verbose

Rename hosts_bigfile.csv to hosts.csv and run the following commands

$./flag1.py --list 

OR

$sudo python flag1.py --list




