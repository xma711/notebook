
Variable names
-------------------
Use meaningful names for variables.


Functions
----------------
Function should be very short.

They should be just a few lines!!!

The number of argument to a function should not be more than 3!!


Comments
---------------

Comments are needed because codes cannot explain themselves,
which means a failure of codes..

The best way is to make the codes explain themselves,
e.g. using meaningful function names.

When comments are needed, they should carry meaningful messages;
like the intent of using this method in the codes.

Background-noise comments should be avoided.

Less comments (but easily-understood codes) is better,
because comments become outdated easily and 
people will forget to update comments.


Format
---------------

Place related codes together vertically.

Add an empty line to islands of codes

a caller function should be close to a callee function.


Object and data structure
-------------------------------

Object is like c++ object, that is created from a class.  
It has data variables inside as well as methods.

Data structure is like the structure in c.
It has only data variables but NO methods at all.

With data structure and another class that provides interface 
to use the data structure, 
it is easy to update the methods in the interface class
without changing the codes for the data strucuture.  
In fact, this is sequential.

With object, adding a new method may require changes to
many classes, because all classes need to have this new method.
E.g. each class is a shape (circule, square, rectangle),
and we want a new method call get_perimeter(), and then
we need to add this method to all classes.  
In data structure, we only need to add this method to the 
interface class.

So????
Think about if you want data to be changed often 
or methods to be changed often.
If data to be changed often, use object,
if methods to be changed often, use data structure.
(need double checking on this conclusion...)


Boundaries
-----------------

Sometimes we use 3rd party library.

It is better to write a wrapper class around the 3rd party library.
This is to ensure any change in the boundary won't cause problem 
to the main codes in the module.

Also, create tests for the library,
which serve as a learning process too,
and for future checking of the library if anything changes.


Handle error
-------------------

Use exception.

Don't return NULL!!!!!! (which i violated!)

Better don't use checked exception (what does this mean?)



Unit tests
-------------------------

Unit tests should be written immediately before production codes;
or the production codes may become to difficult to be unit-tested.  

Unit tests codes have to be very clean;
otherwsie at some point it is hard to update unit tests when production codes are updated.  

Unit tests are very important, 
because it allows production codes to be changed later,
without fearing of breaking other codes.


Class
------------------

Class should be small too. 
It should follow the single responsibility principle.
I.e. if it is changed, it is changed for one single reason.

In an ideal system, we incorporate new features by extending the system, 
not by making modifications to existing code.


