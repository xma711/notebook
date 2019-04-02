# this example shows what exactly a decorator is in python.
# it is nothing but a function that maps a function input to a function output.
# we can define our own decorator;
# and there are definitely built-in decorators that we can use directly.

# define my own decorator, which is nothing but a normal function
def repeater(ori_function):
	print "inside repeater function"
	def new_function(*args, **kwds):
		print "inside new_function"
		# also note that function (f2) inside another function (f1) can access attributes in f1; that's why it can use the "old_function" directly; a bit like Node.js
		ori_function(*args, **kwds)
		ori_function(*args, **kwds)
	# note that from argument's point of view, this new function is the one that accepts the arguments!
	return new_function

# using the @ to call the desired decorator function!!!
# it alters the function below directly;
# in this case the function below will be called twice inside the new function generated
@repeater
def hello():
	print "hello world!"

hello() # hello() will be called twice due to the repeater decorator


#def dummy(function):
#	print "inside dummy function"
#	def yet_another_new_function(*args, **kwds):
#		print "in yet_another_new_function"
#		function(*args, **kwds)
#	return yet_another_new_function

#@repeater(dummy)
#def whatever():
#	print "whatever"

#whatever()

# we can define a decorator that takes an argument and returns another decorator!
#def multiply(num):
#	# the 

def ignore(ori_function):
	print "ignore function"
	def new_function(*args, **kwds):
		print "in new_function. do nothing"
	return new_function

@ignore
def hi():
	print "hi"

hi()

