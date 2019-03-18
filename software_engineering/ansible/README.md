Overview
----------------------

Ansible playbook is like a wish list for what the system should behave in a computer.

If we run the playbook, ansible will ensure the system will follow the instructions and desired states in playbook.
Even if we run the playbook multiple times, the final state should be the same.

The same effects can be achieved by shell script, but with much more works to do.
Imagine in a shell script, we have to check if software exists; if yes, install it; if not, do not install it.
However, in ansible, it is just one line!


Installation
-----------------------

To install it directly to ubuntu, follow http://docs.ansible.com/ansible/intro_installation.html

nothing has to be started.
Ansible can be used from command line.

Another way is to install it using docker: docker pull ansible/ansible:ubuntu1604  
reference: https://hub.docker.com/r/ansible/ansible/

run container: docker run -d -v /home/xma/docker/ansible/etc/ansible:/etc/ansible -v /home/xma/docker/ansible/.ssh:/root/.ssh --name ansible --restart always ansible/ansible:ubuntu1604  

then inside the container, have to install ansible: apt-get install ansible 
(not sure why they don't simply install it for us)


inventory
----------------------------

Reference: http://docs.ansible.com/ansible/intro_inventory.html  

inventory by default is the /etc/ansible/hosts file, which defines hosts.

One example:  
```
[test_clients_docker]
172.17.0.4      ansible_connection=ssh  ansible_user=root

[host_machine]
172.17.0.1      ansible_connection=ssh ansible_user=xma

```

ad hoc usage
----------------------

Reference: http://docs.ansible.com/ansible/intro_adhoc.html  

example: ansible test_clients_docker -a "echo hello" -u root  
(btw if ansible_user is defined in hosts file, then no need ot use "-u root")  
(if "MODULE FAILURE" is encountered, check solutions to issues)

example: ansible test_clients_docker -m copy -a "src=/tmp/hello_from_ansible dest=/tmp/"

example: ansible test_clients_docker -m git -a "repo=https://github.com/xma711/pca.git dest=/tmp/pca version=HEAD"

when no module is specified, the default module is "command".  
Question: what is difference between command and shell?  
Answer: at least, when we neen to pipe output from a command to another like grep, we need shell.

State=present/absent --> this present or absent is the state desired. 
Present means we want something to be installed in not present, absent means we want something to be removed if present.

More ad hoc commands can be found in examples/02_multiple/README.md

playbook usage
----------------------


Issues encountered
--------------------------

When i add 172.17.0.4, a docker ubuntu client, to the hosts file, 
and then i do a 'ansible test_clients_docker -a "echo hello"',
it failed.  
The error msg is "MOUDLE FAILURE".  

The reason is the the client needs to have python2. 
The ubuntu docker container i used happens to not have python2.  
So the solution is to install python2 in client os.

Another solution is to use the module "raw" instead of the default module "command".  
So the full command is 'ansible test_clients_docker -a "echo hello" -u root -m raw' if i don't want to touch the client os.    

Reference of this solution: https://groups.google.com/forum/#!topic/ansible-project/kzLsqoEfX4U


the first time that a container is used, there could be this msg:  
" The authenticity of host '192.168.10.103 (192.168.10.103)' can't be established "  
i have to key in "yes" to proceed.  
How to solve this?
