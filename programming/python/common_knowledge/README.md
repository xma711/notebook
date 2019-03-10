more about sys.path
--------------------------------------------

reference: http://www.diveintopython3.net/your-first-python-program.html#importsearchpath

sys.path is nothing but a list.  
we can view it or modify it with standard list methods.


how does python search its modules to import
-------------------------------------------

reference: http://stackoverflow.com/questions/15252040/how-does-python-find-a-module-file-if-the-import-statement-only-contains-the-fil

there is an internal env variable PYTHONPATH that python follows to search the modules.

or i can see it by  
import sys  
print sys.path  

there seems to be some hardcoding elements here. 
because after i installed anaconda (which comes with python3.5),
and the sys.path in python3.5 is totally different from the sys.path in the original python3.4.

when using the system python, i can see from sys.path that the packages installed by pip (/usr/local/lib/python/dist-packages) 
will be used before the packages installed by apt-get (/usr/lib/python/dist-packages)


summary of reading of book "python in 24 hours"
---------------------------------------------

- Python class's constructor is __init__(self, args..)

- Like c++, python class can overwrite the == operator. 
Just define the __eq__ (self, toCompareObj) function. If we want to use !=, we have to explicitly overwrite the __ne__() function.

- To allow "print object" to work, we can define a __str__(self) function in the class and return a string! (Not print)

- Even int(object) can be achieved by overriding the correct method in the class!

- Package is a directory, while module is a file in the directory. 
A module can have several classes and functions. When we use import, we are importing a module. 
To import a particular class or function, use from module import class/function

- To make a directory act like a package, add an empty __init__.py file. Eg let s call the directory classes, and inside is a monsters.py file. 
To import this file, use import classes.monsters

- Use docstring ''' comments ''' below a class header or function header to explain. This is can be viewed using help(obj).

- Use built-in function vars(obj) to get a json object representation of the obj's attributes names and values! However, if an object has an attribute that is another object, the function won't work recursively. 
One solution is that we have to have a helper function in the class and bridge the vars(self) and vars(anotherObj) together and return it.

- Sqlite3 is a useful database. Python can work with it easily. Just google.

- Like django, flask is another python web framework. But it is used for small application. Django is designed to be used in large application.

- Python has this special type of function, the decorator function. Example: @app.route('/') (next line comes a normal function)

- Jinja2 is a template engine (a bit like php, but in python) that can be used by flask or django to dynamically generate HTML files.

- Pygame is a lib for users to create graphics, mostly for games. Another lib is pyglet that can be used for drawing 3d objects.

- Pdb to python is like gdb to c. Just add "-m pdb " when running a code for debugging.

- Desktop GUI lib: tkinter, pyjs, pygui, and wxpython.


list
-----------------

list is like an array in c. but the elements in list can be just anything while elements in an array have to be the same type.

a list can be declared as 

*new_list = []* 

to add an element to the list:

*new_list.append(711)*  # this is to add the number 711 to the list. note that append is to add one single element to the list

to extend the list with another list (merge to one list):

*new_list.extend(list_b)* # where list_b is sth like ['Python', True]

note that this is different from new_list.append(list_b). in this case, the whole list_b will be a single new element in the new_list

to get an element from the list: *new_list[2]* e.g.

to find out the length: *len(new_list)*

to extract a sub-list: *new_list[2:5]* or *new_list[2:]*  e.g.. note that the output is a list itself.



dictionaries
------------------

dictionaries are key-value pairs. in a list, the index is numbers. but in dictionaries, the index is a meaning immutable object, such as numbers, strings or even tuple (but a list cannot be a key). 

to declare a dictionary:

*person={}* # not that a list is enclosed by []

to add a key-value pair to the dictionary:

*person['name'] = 'xma'*

update the dictionary with another dictionary:

*person.update(another_dictionary)* # where another_dictionary can be sth like {'favorites':[7, 'movies'], 'gender':'male'}

note that the update command is like the extend command for list, which is to merge the last list/dictionary to the first list/dictionary 

any immutable objects can be dictionary keys:

*person[7] = 'favorite number'* or *person[(44.47, -73.21)] = 'coordinates'* # where (44.47, -73.21) is a tuple

to see all the keys: *person.keys()* # the output is in a list, sth like ['name', 'gender']

to see all the values: *person.values()* # the output is in a list, sth like ['xma', 'male']

to see all the key-value pairs in a list: *person.items()* # the output will be in a list, sth like [['name', 'xma'], ['gender', 'male']]



booleans
-------------------

a boolean is sth like this: *is_python = True*

everything is python can be cast to boolean: *is_python = bool("any object")*

all these things are equivalent to False: *are_false = False or 0 or "" or {} or [] or None*

most everything else is equivalent to True: *are_true = True and 1 and "Text" and {'a':'b'} and ['c', 'd']*



operators
------------------

arithmetic: power: *g = a \*\* 2* # g = a to the power of 2

logical: And: *a and b*; Or: *a or b*; Negation: *not a*; compound: (a and not (b or c)) 

Identity comparison: *is* 

e.g. *1 is 1* # output is True

e.g. *1 is not '1'* # output is True

e.g. *1 is True* # output is False. but *1 and True* will have a True output

string
-----------------

these are examples of strings:

*str = 'this is a string'*

*str2 = "this is a string"*

*str3* = """string also, in multiple lines.
hello world on 2nd line!"""

to add two strings together: *anmial = "Cats "+ "Dogs "* # the animal variable is "Cats Dogs "

*animal += "Rabbits"* # the animal variable is updated to "Cats Dogs Rabbits"

to join a list of strings to a single string:

*fruit = ', '.join( ['Apple', 'Banana', 'Orange'] )* # the output is "Apple, Banana, Orange"

something similar to the function 'sprintf' in c is like this:

*date = "%s %d %d" % ('Sept', 11, 2010) # the output is "Sept 11 2010". Note that the input is a tuple

similar way can be applied to a dictionary as an input:

name = '%(first_name)s %(last_name)s' % {'first_name': 'Nowell', 'last_name': 'Strite'}


Control (if-else, while loop, for loop)
-----------------

if-else example:

*start of example:*

grade = 82

if grade >= 90:

	if grade == 100:

		print "A+"

	else:

		print "A"

elif grade >= 80:

	print "B"

else:

	print "whatever"


*end of example*

for if-else example, need to pay attention to the indentation and the semi-colon ":"


for loop examples:

e.g.1:

for x in range(10): # 0 to 9
	
	print x

e.g. 2:

fruits = ['Apple', 'Orange']

for fruit in fruits:

	print fruit

e.g. 3:

states = {'key1': 'val1', 'key2': 'val2', } # it seems that with or without the final comma ',', the dictionary is the same

for key, value in states.items(): # note that the output from items() is a list, not a dictionary

	print '%s: %s' % (key, value)


while loop examples: 


e.g. 1:
```
x = 0

while x < 100:

	print x

	x += 1
```

a list can be created in this way too: 
```
*odds = [ x for x in range(50) if x % 2]* # which is equivalent to

odds = []

for x in range(50):
	
	if x % 2:
		odds.append(x)
```

functions
---------------------

basic function:

*def my_function():*

	*"""function documentation"""*

	*print "hello world"*


function arguments:

def add(x, y):
	
	return x + y

This is actually called positional arguments, which are much similar to the arguments in c programming.


with default value (in fact this is called a keyword):

def shout (phrase = 'Yipee!'):

	print phrase

the last function can be used as *shout ()* or *shout("hello world")* or shout(phrase="hello hell"), which give "Yipee!" and "hello world" and "hello hell" as outputs respectively.

for arbitrary arguments, the function can be defined as:

def some_method(*args, **kwargs):
	
	for arg in args:
	
		print arg

	for key, value in kwargs.items():
		
		print '%s %s' % (key, value)

to use this function, one example is *some_method(1, 2, 3, name='Numbers', item="many")* and the output will be 

1

2

3

item

name

which means that single entities (positional arguments) are stored in "args" while key=value entities (keywords) are stored in "kwargs". args is a list while kwargs is a dictionary.

also note that all non-keyword arguments must be in front of all keyword arguments.


class
-----------------

example:

class User (object):

	is_staff = False

	def __init__(self, name="Anonymous"): # default name is 'Anonymous'

		self.name = name

		super(User, self).__init__() # init its parenet class i guess


	def is_authorized(self):

		return self.is_staff

# end of class

to use this class: 

*user = User() * # declare an object

*print user.name* # Anonymous

*print user.is_authorized()* # False

Notice that this is very similar to the c++ class. but the variables (e.g. name) inside do not have to explicitly declared. interestingly, the attributes name and is_staff are public by default.


class inheritance. example:

class SuperUser(User):

	is_staff = True

# end of clasls

to use the SuperUser class:

*xma = SuperUser('xma')*

*print xma.name* # xma

*print xma.is_authorized()* # Ture

there are no real private attributes and functions. private attributes start (but do not end) with "__". e.g. __privateNum, __privateName

Special class methods start and end with "__". e.g. __init__, __doc__, __cmp__, __str__


imports
--------------------

allow code isolatioin and re-use

add references to variables/classes/functions etc into the current namespace

e.g.

*import datetime*

*datetime.data.today()*

*datetime.timedelta(days=1)*

e.g.2:

*from datetime import date, timedelta*

*date.today()*

*timedelta(days=1)*

Notice the differences? a method needs to start from its parent class or grandparent class in the "import" command.

other examples of import:

*from my_module import date as my_date*

*from datetime import \** # this is not advisable to do


error handling
-------------------

```
import datetime, random

day = random.choice(['Eleventh', 11])

try:

	date = 'September ' + day

except TypeError:

	date = datetime.date(2010, 9, day)

else:

	date += ' 2010'

finally:

	print date
```
need more time to understand exceptions. (maybe i will create a separate topic specially for exceptions)


commandline arguments
-----------------------------------
reference: http://www.tutorialspoint.com/python/python_command_line_arguments.htm

```
#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# for example:
# "./commanlineArguments.py hello world" will give an output of:
# Number of arguments: 3 arguments.
# Argument List: ['./commanlineArguments.py', 'hello', 'world']
```

to parse the command line arguments, use  
*getopt.getopt(args, options[, long_options])*  
where args is the argument list, options is the string of option letters and long_options are a list of strings with the names of the long options.

e.g. 

```#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
```
