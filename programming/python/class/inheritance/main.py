import book
import bookAuthor

b1 = book.Book("Learn python in 24 hours");
b1.print_info();

b2 = bookAuthor.BookAuthor("Learn java in 24 hours", "whoever");
b2.print_info();

# try pass both parent and child object to the same function
def print_book_info_local (abook):
	abook.print_info()

print "\ntry passing parent and child object to the same function:"
print_book_info_local(b1);
print_book_info_local(b2);

# the results show that we don't have to worry about a function may use the parent's method when a child object is passed into the function;
# such concern will have to be taken care in language like c++ (the solution is using virtual method.)
# this is probably because python is not a type language like c++

print "\ntry create a new method on the fly:"
def say_hello(abook):
	print "book {} says hello.".format(abook.title)

book.Book.greeting = say_hello;
b3 = book.Book("hong lou meng");
b3.greeting();

# in fact, this one works too!! although it is created before we added the function to the Book class!
b1.greeting();
