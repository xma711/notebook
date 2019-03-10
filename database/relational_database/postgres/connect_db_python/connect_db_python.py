#!/usr/bin/env python

hostname = 'localhost'
username = 'postgres1'
password = 'postgres1_postgres' # this password is not the corresponding linux user account's password; it is the password of the role "postgres1" in postgres
database = 'postgres1'

def doQuery(conn):
	cur = conn.cursor()

	cur.execute("SELECT * FROM playground")

	for row in cur.fetchall():
		print row

print "using psycopg2..."

import psycopg2

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

doQuery(myConnection)

myConnection.close()
