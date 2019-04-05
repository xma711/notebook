Ruby
-------------

This document talks about the programming language Ruby, not the web framework Rails.

Overall, it seems Ruby is quite similar to Python and shell script.  
The concept that everything is an object in Ruby is also similar to python (or java)..  
Some new concepts include block, module...


Variables and constants
-----------------

Local variables: same as variables in C;  no special sign is needed.  
Instance variables: these are like normal variables in a c++ class, but they have to be preceded by the sign @.  
Class variables: such variables are available across different objects. preceded by @@. 
	this is kinda global among the same objects.. be careful.   
	the change to this class variable can be defined in the initializer or a method; effect is global.  
	in fact, this is similar to the static variable in a class in C++!  
Global variables: declare using sign $.

Constants MUST begin with an UPPERCASE letter!!

To unwrap a variable or constant in  puts "strings" (like printf in c), we use #{variableName} (variableName could have a sign in front). 
This is very similar to variables in shell script, except in shell script we don't always have to use {} when there is no ambiguity.

In fact, #{ expr } is to make any ruby expression into a string.  
Therefore, something like #{ number + num } is fine too.  
This should have an application in the html file.

To check if a variable is defined, use: defined? variableName.  
It can be used for checking a function, and others (super, yield..)


String
----------------

"" double quoted strings allow substitution and backslash / notation
but '' single quoted strings doesn't allow substitution (good for making some static string) and allow backslash notation only for \\ and \.


Array
--------------------

Example: ary = ["hello", 3.1415, "string", 1234]


hash
----------------

This is like python dictionary.  
Example: colors_hash = { "red" => 0xf00, "green" => 0x0f0, "blue" => 0x00f}

an array can be a key too..


Operators
-----------------

A+b is actually a.+(b)..  
This is cool man. '+' is the method name of object a, and object b is the argument to this method.  
Looks like everything is an object, just like Java.

In fact, this is similar to C++ operators too, which can be overwritten in c++ if needed.


Class
------------------

To declare an object: object1 = ClassName. new  ## note that there is a dot after the class name

to access constants, instance methods and class methods, use objectName::Something (when there is no objectName, it is a global variable).  
In Ruby, classes and methods may be considered constants too.
 
Seems that the result from the last statement in a method will be auto-returned.

To pass arguments to a method, there is no need for () ..  
(this can cause some confusion.)

To create a method, it is similar to python: define ... end (of course python doesn't need an end statement)

normally, to use a method inside a class, we have to create an object first.  
Ruby has one way to let users use a method inside a class directly. 
Inside a class Accounts, def a method Accounts.method_name; then we can use Accounts.method_name directly without having to create an Accounts object.


Control flows
---------------

If else are the same as other programming languages.  
There is a new one - unless, which is exactly opposite of if..

The usual "switch case default" is "case when else" in Ruby.

While loop: while do (similar to shell script)  
do while: begin (codes..) end while ..  

New one: until (conditional) do (codes) end   
this will execute codes while conditional is false.

For loop: for i in something (codes) end

new one: something.each do |i| (codes) end  
this is almost the same as a for loop

new one: redo, which is to restart the iteration of the most internal loop without checking loop condition.. works inside a if..else too.

Retry: begin.. rescue (retry) end : the retry will cause restart from the "begin".. it is inside the rescue section.


Block
---------------

A block of codes is like a function.  
The format is: block_name { statements }  (note that method declaration is def method_name ... end)
how to execute this block is simple: there must be a method with the same name as the block_name;  
once you define a block, that's it. 
At the appropriate time, the method with same name will obtain this block and execute it at where the "yield" keywords are placed.  
The simplest example is:  
```
# this is a method
def test
	yield
end  

# this is a block:  
test { puts "hello world!" }  # note that the block name is the same as the method name
```

some built-in METHODs that accept blocks are BEGIN and END. 
Just defines some BEGIN and/or END blocks will make the blocks of codes to be executed when the program is loaded and/or finished. 
(not limit to just one BEGIN or END)


module
---------------------

Modules define a namespace, a sandbox in which your methods and constants can play 
without having to worry being stepped on by other methods and constants.  
The format is same as class:  
```
module moduleName  
	statements
end
```
one example:
```
module Trig
	def Trig.sin(x)
		# some codes
	end
end
```
if the module is another file, to add it to this file, use require filename (after adding path to the LOAD_PATH global parameter)

"mixin" meaning is exhibiting multiple inheritance.  
Ruby doesn't support multiple inheritance but it has this mixin ability.  
When we define a module A and B separately (they look like classes), 
and we have a class Sample; we have include these two modules to the class Sample;
then class Sample is able to use methods from both module A and B. thus behaving like multiple inheritance.


String
--------------------

There seems to be raw string and class string.  
Raw string is like "hello world", class string is like myStr = String.new("hello world");

string * integer : string is repeated integer times and returned.


Range
---------------

Range is a bit like the Microsoft excel auto-completion.
We specify a starting item and ending item, and ruby will auto generate a list.  
Example: (1..10), ('a'..'d'), ('bar'..'bat')

two dots: inclusive range;  
three dots: exclusive of the last item.


File io
----------------

File reading and writing are quite standard. just google..  
But there are some methods to change file permissions, just like the "chmod" command in Linux. (in fact, the method is also called chmod..)

Besides the File class, there is also a Dir class to handle directories. 
The methods look exactly like Linux commands..

Btw there is a built-in method to create a platform-independent temporary file.


Exception
----------------

Syntax: begin (codes) rescue OneTypeOfException (codes) rescue AnotherException (codes) else (codes) ensure (codes) end;  
note that 'ensure' is a bit like 'final' that ensures the codes behind it will be executed no matter what.

'retry' can be used here sometimes to move control to the beginning of 'begin' after some proper new setup.
However, be careful when using 'retry' because it may cause infinity loop.

To throw an exception (simplest way): raise "Error message"


database
------------------

Ruby provides an abstraction layer.  
But overall we are still forming SQL commands and send them using ruby's API. this is a bit like php.  
Syntax: dbh.do("sql command...")
