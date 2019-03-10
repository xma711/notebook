
variable names
-------------------
use meaningful names for variables.


functions
----------------
function should be very short.

they should be just a few lines!!!

the number of argument to a function should not be more than 3!!


comments
---------------

comments are needed because codes cannot explain themselves,
which means a failure of codes..

the best way is to make the codes explain themselves,
e.g. using meaningful function names.

when comments are needed, they should carry meaningful messages;
like the intent of using this method in the codes.

background-noise comments should be avoided.

less comments (but easily-understood codes) is better,
because comments become outdated easily and 
people will forget to update comments.


format
---------------

place related codes together vertically.

add an empty line to islands of codes

a caller function should be close to a callee function.


object and data structure
-------------------------------

object is like c++ object, that is created from a class.  
it has data variables inside as well as methods.

data structure is like the structure in c.
it has only data variables but NO methods at all.

with data structure and another class that provides interface 
to use the data structure, 
it is easy to update the methods in the interface class
without changing the codes for the data strucuture.  
in fact, this is sequential.

with object, adding a new method may require changes to
many classes, because all classes need to have this new method.
e.g. each class is a shape (circule, square, rectangle),
and we want a new method call get_perimeter(), and then
we need to add this method to all classes.  
in data structure, we only need to add this method to the 
interface class.

so????
think about if you want data to be changed often 
or methods to be changed often.
if data to be changed often, use object,
if methods to be changed often, use data structure.
(need double checking on this conclusion...)


boundaries
-----------------

sometimes we use 3rd party library.

it is better to write a wrapper class around the 3rd party library.
this is to ensure any change in the boundary won't cause problem 
to the main codes in the module.

also, create tests for the library,
which serve as a learning process too,
and for future checking of the library if anything changes.


handle error
-------------------

use exception.

Don't return NULL!!!!!! (which i violated!)

better don't use checked exception (what does this mean?)



unit tests
-------------------------

unit tests should be written immediately before production codes;
or the production codes may become to difficult to be unit-tested.  

unit tests codes have to be very clean;
otherwsie at some point it is hard to update unit tests when production codes are updated.  

unit tests are very important, 
because it allows production codes to be changed later,
without fearing of breaking other codes.


class
------------------

class should be small too. 
it should follow the single responsibility principle.
i.e. if it is changed, it is changed for one single reason.

In an ideal system, we incorporate new features by extending the system, 
not by making modifications to existing code.


