Subfolders
---------------------

Connect_db_python: an example showing how to connect to postgres database using python

postgres_in_aws: how to create a postgres database in aws and how to connect to it


postgres
------------------

Reference: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

postgreSQL or postgres is a relational database management system that provides an implementation of the SQL querying language.

It has the advantage of being standards-compliant 
and having many advanced features like reliable transactions and concurrency without read locks.

To install postgres and a contrib package that adds some additional utilities:  
sudo apt-get install postgresql postgresql-contrib


useful commands in psql
------------------------------

\q : exit  
\l or \list : list databases  
\d : list tables  in the current database  
\dt : list tables without the sequence table in the current database  
\conninfo : display current connection info  
\connect DBNAME : connect to a database  

some concepts about "roles"
--------------------

By default, postgres uses a concept called "roles" to handle authentication and authorization.  
These are similar to the regular unix-style accounts and 
postgres does not distinguish between users and groups and instead prefers the more flexible term "role".

Upon installation postgres is set up to use ident authentication,
which means that it associates posgres roles with a matching unix/linux system account.  
If a role exists within postgres, a unix/linux username with the same name will be able to sign in as that role. (to understand this line more, read section "create a new role".)


"postgres" role
-----------------------

The installation procedure created a user account (in the linux system) called "postgres" that is 
associated with the default Postgres role (i.e the "postgres" role).

We can switch to the "postgres" account by typing:  
sudo -i -u postgres # this is just to switch to a user in the linux terminal; at this step there is nothing to do with postgres database yet

now access a postgres prompt by typing:  
psql  

to exit the prompt:  
postgres=# \q 

alternatively, to run command psql in "postgres" user at one go, use:  
sudo -u postgres psql


create a new role
--------------------------

Log in as the postgres account first (sudo -i -u postgres), then:  
createuser --interactive

subsequently, follow the prompt to enter the specifications.

Note that "createuser" is nothing but an executable.
It can be executed from any linux account but so far only "postgres" account will allow the command to proceed.

After creating the new role (in postgres), we have to a user with the same name in the linux machine if it has not existed.  
E.g. if i created "postgres1" using createuser, then i need to create the postgres1 user in the linux machine in the normal way (sudo adduser postgres1).  
(btw in my test i did create this account with an easy password.)

Create a database
--------------------------

By default, another assumption postgres authentication system makes is that 
there will be an database with the same name as the role being used to login,
which the role has access to.

A role will attempt to connect to a database with the same name by default. 
(meaning: after running the "psql" command, it automatically connects to the default database;
this can be verified using "\conninfo".)

To create a database, user:  
createdb database_name  
e.g. createdb xma  (for the account xma)


example:  
```
postgres@vcdim:~$ psql 
psql (9.5.8)
Type "help" for help.

Postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```

grant database to a role
------------------------------------

Sudo -i -u postgres # linux terminal goes to this user

then create the "new_user" if not created: createuser --interactive

enter 'psql'.

Then set a password for new_user: 
ALTER USER newuser password 'enter_password'
 
now proceed to (re)create the database:    
CREATE DATABASE "django_db";  
GRANT ALL PRIVILEGES ON DATABASE django_db TO new_user;


create and delete table
--------------------------

The basic syntax for creating a table is:  
CREATE TABLE table_name (  
	column_name1 col_type (field_length) column_constraints,  
	column_name2 col_type (field_length),  
	column_name3 col_type (field_length)  
);  

in this command, we give the table a name, and then define the columns we want, as well as the column type and the max length of the field data.
We can optionally add table constraints for each column.

In fact, this is exactly the same as the command in MySQL.

One example:  
```
CREATE TABLE playground (
	equip_id serial PRIMARY KEY,
	type varchar (50) NOT NULL,
	color varchar (25) NOT NULL,
	location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
	install_date date
);
```
This table is to record inventories the equipment that we have.  
Equipment id is of Serial type, which is an auto-incrementing integer.
Being primary key means that the values must be unique and not null.  

For equip_id and install_date, we have not given a field length.
This is because the set length is implied by the type in this case.

There is a constraint for the "location" column that requires the value to be one of 8 possible values.

To see the new table created:  
postgres=# \d  

example:  
```
postgres=# \d
                   List of relations
 Schema |          Name           |   Type   |  Owner   
--------+-------------------------+----------+----------
 public | playground              | table    | postgres
 public | playground_equip_id_seq | sequence | postgres
(2 rows)
```
our playground table is here, but we also have something called playground_equip_id_seq that is of the type 'sequence'.  
This is a representation of the 'serial' type we gave our equip_id column.

If just to see the table without the sequence, can type:  
postgres=# \dt  


add, query and delete data in a table
-------------------------------------------

Same as mysql..

Example of insert:  
INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2014-04-28');


postgreSQL for django
-------------------

Https://help.ubuntu.com/community/PostgreSQL
to use postgreSQL commands, login as user postgres: sudo su postgres


login to postgres shell: psql
Then can use commands similar to sql.
E.g. CREATE USER, DROP USER,
ALTER USER name PASSWORD “newpassword”


to switch database in shell: \connect DBNAME
it seems psql is a bridge written for sql people to use postgres.


In setting.py, 
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dtut2',
            'USER': 'tut2',
            'PASSWORD': 'password',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
}

it seems the owner of database dtut2 must be tut2.


Login as postgres: sudo su postgres
create user: createuser userName -P
create database: createdb --owner userName databaseName
