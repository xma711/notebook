SOLID
-----------------

for object-oriented programming, there are 5 basic principles of class design:

SRP: The single responsibility principle

OCP: The Open closed principle

LSP: the liskov substitution principle

ISP: the interface segregation principle

DIP: the dependency inversion principle

reference: http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod


liskov substitution principle (LSP)
-------------------------------------

reference: http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle#comment13317449_584732

in math, a square is a rectangle.
so we may inclind to make a squre class by inheriting a rectangle class.

however, one basic question to ask is that:
in all the functions that uses a rectangle class reference,
can i substitute it with its derived class, such as the square class?

if the answer is no, it means square should not inherit from rectangle.

in fact, the answer is really no.
e.g. in a function that requires to setWidth and setLen of a rectangle,
and asserts the area = width set x length set,
passing in a square to the argument of the function will cause the function to crash.

therefore, model the classes based on behaviours, not on poroperties.
(model data based on properties, not on behaviours ---> don't understand this sentence.)

anyway, the LSP states that:
functions that use pointers or references to base classes must be able to use 
objects of derived classes without knowing it.

practical tip:
set an invariant function on the base class. 
when rectangle is the base class, one invariant should be:
```
void invariant(Rectangle* r) {
	r->setHeight(200);
	r->setWidth(100);
	assert(r->getHeight() == 200 and r.getWidth() == 100);
}
```

i think another example is the ns2 simulator design.
there is a base class that basically has a recv() method only,
and all other classes simply inherit from this base class
and have different implementations on the recv() function.
