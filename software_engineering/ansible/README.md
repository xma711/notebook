overview
----------------------

ansible playbook is like a wish list for what the system should behave in a computer.

if we run the playbook, ansible will ensure the system will follow the instructions and desired states in playbook.
even if we run the playbook multiple times, the final state should be the same.

the same effects can be achieved by shell script, but with much more works to do.
imagine in a shell script, we have to check if software exists; if yes, install it; if not, do not install it.
however, in ansible, it is just one line!


installation
-----------------------

to install it directly to ubuntu, follow http://docs.ansible.com/ansible/intro_installation.html

nothing has to be started.
ansible can be used from command line.

another way is to install it using docker: docker pull ansible/ansible:ubuntu1604  
reference: https://hub.docker.com/r/ansible/ansible/

run container: docker run -d -v /home/xma/docker/ansible/etc/ansible:/etc/ansible -v /home/xma/docker/ansible/.ssh:/root/.ssh --name ansible --restart always ansible/ansible:ubuntu1604  

then inside the container, have to install ansible: apt-get install ansible 
(not sure why they don't simply install it for us)


inventory
----------------------------

Reference: http://docs.ansible.com/ansible/intro_inventory.html  

inventory by default is the /etc/ansible/hosts file, which defines hosts.

one example:  
```
[test_clients_docker]
172.17.0.4      ansible_connection=ssh  ansible_user=root

[host_machine]
172.17.0.1      ansible_connection=ssh ansible_user=xma

```

ad hoc usage
----------------------

reference: http://docs.ansible.com/ansible/intro_adhoc.html  

example: ansible test_clients_docker -a "echo hello" -u root  
(btw if ansible_user is defined in hosts file, then no need ot use "-u root")  
(if "MODULE FAILURE" is encountered, check solutions to issues)

example: ansible test_clients_docker -m copy -a "src=/tmp/hello_from_ansible dest=/tmp/"

example: ansible test_clients_docker -m git -a "repo=https://github.com/xma711/pca.git dest=/tmp/pca version=HEAD"

when no module is specified, the default module is "command".  
question: what is difference between command and shell?  
answer: at least, when we neen to pipe output from a command to another like grep, we need shell.

state=present/absent --> this present or absent is the state desired. 
present means we want something to be installed in not present, absent means we want something to be removed if present.

more ad hoc commands can be found in examples/02_multiple/README.md

playbook usage
----------------------


issues encountered
--------------------------

when i add 172.17.0.4, a docker ubuntu client, to the hosts file, 
and then i do a 'ansible test_clients_docker -a "echo hello"',
it failed.  
the error msg is "MOUDLE FAILURE".  

the reason is the the client needs to have python2. 
the ubuntu docker container i used happens to not have python2.  
so the solution is to install python2 in client os.

another solution is to use the module "raw" instead of the default module "command".  
so the full command is 'ansible test_clients_docker -a "echo hello" -u root -m raw' if i don't want to touch the client os.    

reference of this solution: https://groups.google.com/forum/#!topic/ansible-project/kzLsqoEfX4U


the first time that a container is used, there could be this msg:  
" The authenticity of host '192.168.10.103 (192.168.10.103)' can't be established "  
i have to key in "yes" to proceed.  
how to solve this?
