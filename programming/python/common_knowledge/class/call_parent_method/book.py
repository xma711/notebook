class Book(object):
	__title = ""

	def __init__(self, title):
		self.__title = title

	def get_title(self):
		return self.__title

	def get_all_info(self):
		print "the title is ", self.__title

class BookInfo(Book):
	__author = ""

	def __init__(self, title, author):
		parent = super(BookInfo, self)
		parent.__init__(title)
		self.__author = author

	def get_author(self):
		return self.__author

	# this method is fine, although it is unnecessary to get the pointer to the parent class first
	def get_title2(self):
		return super(BookInfo, self).get_title()

	# this method is not right, because child class cannot access __title directly
	# def get_title3(self):
	#	return self.__title

	# derived method
	def get_all_info(self):
		print "the title is ", self.get_title(), " and the author is ", self.__author

# main starts here
b = BookInfo("journey to the west", "wu cheng en")
print b.get_author()
print b.get_title() # parent's public method can be used directly by the child class
# so, is it that internally python tries to find the method in child's content and then if not found it continue to search the method in parent's content?

# we can get the parent class of the object
b_parent = super(BookInfo, b)
print b_parent.get_title() # this is fine

# print b_parent.get_author() # this will lead to error because the parent class doesn't have this method

print b.get_title2()

#print b.get_title3() # this leads to error, because the child class cannot access __title directly

b.get_all_info()
b_parent.get_all_info() # this is how to access the parent's function directly, a bit like c++
