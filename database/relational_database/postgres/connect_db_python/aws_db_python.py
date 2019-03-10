#!/usr/bin/env python

hostname = 'postgres-aws-test.cvbfx5rmnyq6.us-east-1.rds.amazonaws.com'
username = 'postgres'
password = 'postgres_123' # this password is not the corresponding linux user account's password; it is the password of the role "postgres1" in postgres
database = 'playground'

def doQuery(conn):
	cur = conn.cursor()

	cur.execute("SELECT * FROM table1")

	for row in cur.fetchall():
		print row

print "using psycopg2..."

import psycopg2

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

doQuery(myConnection)

myConnection.close()
