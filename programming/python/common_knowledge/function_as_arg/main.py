def hello_world ():
	print "hello world!"

def hi():
	print "hi there!"

# function is not much different from normal variable
def do_sth(num, funct):
	for i in range(num):
		funct();

do_sth(10, hello_world)

do_sth(5, hi)
