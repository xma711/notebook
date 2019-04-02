#!/usr/bin/python2.7

# hello world function, to be tested
def hello_world() :
	return "hello world"

# a hello world class, to be tested
class hello_world_class:
	# python implicitly passes the object to method calls, 
	# but you need to explicitly declare the parameter for it.
	# this is customarily named self
	def hello_world(self):
		return "hello world"

# main function
def main() :
	# get from function
	ret = hello_world()
	
	# need to declare an object from class hello_world_class
	hello_world_object = hello_world_class()
	ret2 = hello_world_object.hello_world() # python passes the object to method class at the back

	print "from function: %s" % (ret)
	print "from class: %s" % (ret2)

if __name__ == '__main__':
	main()



