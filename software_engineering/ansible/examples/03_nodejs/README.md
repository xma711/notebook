Reference
-------------------------

Book "ansible for devops", page 55.  
(In the book it uses Centos. In my test Ubuntu 16.04 docker container is used.)


Start this app
-------------------

Ansible-playbook -i hosts playbook.yml --extra-vars="node_apps_location=/usr/local/opt/node" -u root
