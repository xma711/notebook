#!/usr/bin/python

# a script to show how to create a table 
# and write data to the table
# reference: http://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb 

# open database connection to database simpleDB
# the input parameters are hostname, username, password, databaseName
print "open connection"
db = MySQLdb.connect('localhost', 'xma', '', 'simpleDB' )

# prepare a cursor
cursor = db.cursor()

# execute SQL query using execute() method
# this is exactly the same as running SQL commands in the terminal
sql_command = "SELECT VERSION()"
print "execute SELECT VERSION"
cursor.execute(sql_command) # obtain the version

# fetch a single row using fetchone()
data = cursor.fetchone()

print "Database version: %s" % data

# drop table if it already exist using execute() method
sql_command = "DROP TABLE IF EXISTS EMPLOYEE"
try:
	cursor.execute(sql_command)
except:
	print "no such table to delete"

# create table 
sql_command = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

print "execute create table"
cursor.execute(sql_command)

# a function to insert data to a table in a table base
def insert_data(command, database, cursorIn):
	try:
		print "try execute command: %s" % command
		cursorIn.execute(command)
		# commit the changes in the database
		database.commit()
	except:
		# rollback in case there is any error
		database.rollback()	

# insert a data
sql_command = """INSERT INTO EMPLOYEE (FIRST_NAME, 
		LAST_NAME, AGE, SEX, INCOME)
		VALUES ('HELLO', 'LIN', 29, 'M', 1000)"""
insert_data(sql_command, db, cursor)


# insert a data
sql_command = """INSERT INTO EMPLOYEE (FIRST_NAME, 
		LAST_NAME, AGE, SEX, INCOME)
		VALUES ('WORLD', 'Feyman', 50, 'F', 2000)"""
insert_data(sql_command, db, cursor)

# select all from the table
sql_command="SELECT * FROM EMPLOYEE"
cursor.execute(sql_command)
# use fetchall to get all data
data=cursor.fetchall()

print data

# disconnect from server
db.close()
