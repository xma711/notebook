Setup
------------------------

Use the create_remove_ubuntu_test_containers.sh to create the containers.

Or use the followings.

Create ubuntu container: docker run -d --net dockernet --ip 192.168.10.101  -v /home/xma/docker/ubuntu_test/.ssh:/root/.ssh --name ubuntu_test_1 --restart always rastasheep/ubuntu-sshd:16.04-customized

this rastasheep/ubuntu-sshd:16.04-customized is created using the dockerfile in devops/example_2017/ubuntu_sshd_dockerfile/

btw the dockernet is created using docker. refer to the README.md in devops/example_2017/

of course have to setup the public key in the container so that the host machine (and thus ansible) can access the container.

In the book "Ansible for DevOps", the author uses centos in chapter 2, 
but in china it is quite inconvenient to download centos virtualbox image, so i use ubuntu docker image instead.


Use command line to ping
-------------------------------

Ansible -i ./hosts ubuntu_test -m ping -u root  
(use the local inventotry file "hosts" instead. -m refers to the module)


use playbook
------------------------------

Ansible-playbook -i ./hosts ./playbook.yml -u root  
(don't forget about the "-u root" to use the right ssh keys)


results
--------------------

```
TASK [Ensure NTP (for time synchronization) is installed] *************************************************************************************************************
ok: [192.168.10.101]
changed: [192.168.10.102]

TASK [Ensure NTP is running] ******************************************************************************************************************************************
changed: [192.168.10.102]
ok: [192.168.10.101]

PLAY RECAP ************************************************************************************************************************************************************
192.168.10.101             : ok=3    changed=0    unreachable=0    failed=0   
192.168.10.102             : ok=3    changed=2    unreachable=0    failed=0 
```

interpretation:  
ntp has been installed and running in 192.168.10.101, so there is nothing changed.  
But ntp is not installed in 102. ultimately there are 2 changes. one is to install ntp and the other is start ntp.  
If we run again, then both changes will be 0.