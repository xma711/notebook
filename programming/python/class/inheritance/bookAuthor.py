import book

# Book will be its parent class
class BookAuthor(book.Book):

	def __init__ (self, titleIn, authorIn):
		# this is the "new style" of calling parent class' constructor
		# reference: http://stackoverflow.com/questions/3694371/how-do-i-initialize-the-base-super-class
		# obviously, super(BookAuthor, self) returns the pointer to the parent of 'self'
		super(BookAuthor, self).__init__(titleIn);
		self.author = authorIn;

	# this will override the parent's method
	def print_info (self):
		print "Title of the book is: " + self.title + "; and the author is: " + self.author;
