Objective and setup
---------------------

Objective: try ad hoc commands.

Setup: use the script to create 3 containers


Command lines
-----------------

Ansible multi -i hosts -a "hostname"

-a means module arguments; seems that it allows shell commands..
(then why it is called module arguments?)

There is another option "-f", which means the number of parallel forks.
E.g. -f 1 means only 1 process. 
By default it is some number > 1.

Others:

```
ansible multi -i hosts -a "df -h"
ansible multi -i hosts -a "free -m"
ansible multi -i hosts -a "date"
```

To ensure ntp is install:  
ansible multi -i hosts -m apt -a "name=ntp state=present" -u root  
(can use -s instead of "-u root" too, but -s is deprecated)

To start ntp:  
ansible multi -i hosts -m service -a "name=ntp state=started enabled=yes"

Others:

```
ansible multi -i hosts -m apt -a "name=ntpdate state=present" -u root
ansible multi -i hosts -a "service ntp stop" -u root
ansible multi -i hosts -a "ntpdate -q 0.rhel.pool.ntp.org" -u root
ansible multi -i hosts -a "service ntpd start" -u root
```

Example: django and mysql
----------------------------------
Web app:

```
#ansible app -i hosts -m apt -a "name=mysql-server state=present" -u root  # maybe this line is not needed..
Ansible app -i hosts -m apt -a "name=python-setuptools state=present" -u root
ansible app -i hosts -m apt -a "name=libmysqlclient-dev state=present" -u root # for solving the "mysql_config: not found" problem when installing mysql-python 
ansible app -i hosts -m apt -a "name=gcc state=present" -u root # this line and next are needed for easy_install mysql-python
ansible app -i hosts -m apt -a "name=python-dev state=present" -u root
ansible app -i hosts -m easy_install -a "name=mysql-python" -u root
ansible app -i hosts -m easy_install -a "name=django" -u root
ansible app -i hosts -a "python -c 'import django; print django.get_version()'" -u root
```

database:

```
ansible db -i hosts -m apt -a "name=mariadb-server state=present" -u root
#ansible db -i hosts -m service -a "name=mariadb state=started enabled=yes" -u root  
ansible db -i hosts -m service -a "name=mysql state=started enabled=yes" -u root
(there is some iptable stuff at this point, to only accept web servers to contact the database. skip for now.)
Ansible db -i hosts -m apt -a "name=python-dev state=present" -u root
ansible db -i hosts -m apt -a "name=gcc state=present" -u root
ansible db -i hosts -m apt -a "name=libmysqlclient-dev state=present" -u root
ansible db -i hosts -m apt -a "name=python-setuptools state=present" -u root
ansible db -i hosts -m easy_install -a "name=mysql-python"
ansible db -i hosts -m mysql_user -a "name=django host=% password=somepassword priv=*.*:ALL state=present"
```

(Some problems installing mysql-python are solved by this link: http://www.linuxidc.com/Linux/2014-11/109246.htm)

(To be continued..)


Thinking
-------------------------

In fact, an alternative way to create a dockerfile for the ubuntu image is 
to create a playbook for the ubuntu image; 
so that we can set the container to the right state.  
However, this method is time-consuming in the sense that each container has to go through this setup process.
