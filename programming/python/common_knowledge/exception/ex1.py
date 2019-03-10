#!/usr/bin/python2

def throw_exception():
	raise Exception("try exception");

try:
	throw_exception();
except Exception:
	print ("exception catched") 
	print ( Exception.message ) 
