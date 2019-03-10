# the 'object' in '()' is necessary to allow inheritance using the new-style constructor, 
# which is "super (SubClassName, self).__init__(args)"
class Book (object):
	# this is the constructor
	def __init__ (self, titleIn):
		self.title = titleIn;

	def print_info (self):
		print "The title of the book is: " + self.title

# btw, the reason that python needs to pass self into a class method is that:
# python tries to make method entirely the same as functions;
# in fact, we can define the same function outside the class, something like "def print_info(theBook)", 
# and then create a method for the Book class in the runtime: Book.print_info = print_info,
# and then we can immediately use bookObj.print_info().
# as a result, the attributes in a class and the methods are actually quite separated/independent from each other.
