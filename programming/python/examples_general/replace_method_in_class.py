#!/usr/bin/python2

# test changing a method in a class

class hello_world():
	def print_hello(self):
		print "hello world!"

# normal obj
obj1 = hello_world()

print "use the original method"

obj1.print_hello()

ori_method = hello_world.print_hello

def mock_print_hello(self):
	print "mock printing hello"

hello_world.print_hello = mock_print_hello # this change is global!! need to be careful!!

print "\ntry the method in the same object after the class's method is changed"

# even though the obj1 is not changed, the method is changed!!!
obj1.print_hello()
