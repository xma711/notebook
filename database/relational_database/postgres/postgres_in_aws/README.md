Create a postgres instance in aws
---------------------------------------

Just go to aws RDS page and then choose postgres.  
Link: https://console.aws.amazon.com/rds/home?region=us-east-1#dbinstance:id=postgres-aws-test

after a few minutes, the endpoint (domain name) and port will appear.

The security group will be automatically created based on my current ip address.  
E.g. when accessing aws from nus, my public ip address is 137.132.190.150, and then the security group will be:  
```
Security group		Type		Rule
rds-launch-wizard	CIDR/IP		137.132.190.150/32
```

Connect to the instance from local ubuntu
----------------------------------------------

Reference: https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/

use tool sql workbench (not mysql-workbence):  
http://www.sql-workbench.net/getting-started.html

also need to download the JDBC driver from the PostgreSQL from https://jdbc.postgresql.org/download.html

driver is postgressql (this step will prompt me to select the driver just downloaded)

url is jdbc:postgresql://postgres-aws-test.cvbfx5rmnyq6.us-east-1.rds.amazonaws.com:5432/playground


Issues
----------------

Fail to connect with an error msg:  
"onnection to postgres-aws-test.cvbfx5rmnyq6.us-east-1.rds.amazonaws.com:5432 refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections."
