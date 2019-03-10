# this example is to show how to override operators like < and > for our own-created class;

class Cat (object):
	def __init__ (self, catName, catAge):
		self.name = catName;
		self.age = catAge;

	# allow "print catObject" to print meaningful info 
	def __str__ (self):
		return "I'm a cat. My name is " + self.name + ", and I am " + str(self.age) + " years old."

	# override the operator '<'
	def __lt__ (self, other):
		return self.age < other.age

	# override the operator '>'
	def __gt__ (self, other):
		return self.age > other.age

	# there are other operators, like __le__, __eq__, __ne__, __ge__
	
def main():
	cat1 = Cat("meow1", 5);
	cat2 = Cat("active", 3);

	print cat1;
	print cat2;

	if cat1 > cat2:
		print "cat1 {} is older than cat2 {}".format(cat1.name, cat2.name);
	else:
		print "cat1 {} is not older than cat2 {}".format(cat1.name, cat2.name);

main();
