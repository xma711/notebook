
# this example shows how to access public and private attributes in a class

# all classes have a root parent object
class Book (object):
	__title = "" # this is a private attribute
	att1="this is a public attribute"

	# again, note that every method is quite independent from the class, as the self pointer has to be passed into the method!
	def __init__(self, title):
		self.__title = title

	def get_title(self):
		return self.__title

b = Book("journey to the west")
print b.get_title()

print b.att1 # this is okay

try:
	print b.__title # this leads to an exception
except:
	print "cannot access __title attribute in the obj"
