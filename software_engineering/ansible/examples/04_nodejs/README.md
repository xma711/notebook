reference
-------------------------

book "ansible for devops", page 55.  
(in the book it uses centos. here i use ubuntu 16.04 docker container)


start this app
-------------------

ansible-playbook -i hosts playbook.yml --extra-vars="node_apps_location=/usr/local/opt/node" -u root
