def hello_world ():
	print "hello world!"

def hi():
	print "hi there!"

# function is not much different from normal variable
def do_something(num, funct):
	for i in range(num):
		funct();

do_something(10, hello_world)

do_something(5, hi)
