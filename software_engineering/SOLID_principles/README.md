SOLID
-----------------

For object-oriented programming, there are 5 basic principles of class design:

SRP: The single responsibility principle

OCP: The Open closed principle

LSP: the liskov substitution principle

ISP: the interface segregation principle

DIP: the dependency inversion principle

reference: http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod


liskov substitution principle (LSP)
-------------------------------------

Reference: http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle#comment13317449_584732

in math, a square is a rectangle.
So we may incline to make a square class by inheriting a rectangle class.

However, one basic question to ask is that:
in all the functions that uses a rectangle class reference,
can i substitute it with its derived class, such as the square class?

If the answer is no, it means square should not inherit from rectangle.

In fact, the answer is really no.
E.g. in a function that requires to setWidth and setLen of a rectangle,
and asserts the area = width set x length set,
passing in a square to the argument of the function will cause the function to crash.

Therefore, model the classes based on behaviors, not on properties.
(model data based on properties, not on behaviors ---> don't understand this sentence.)

Anyway, the LSP states that:
functions that use pointers or references to base classes must be able to use 
objects of derived classes without knowing it.

Practical tip:
set an invariant function on the base class. 
When rectangle is the base class, one invariant should be:
```
void invariant(Rectangle* r) {
	r->setHeight(200);
	r->setWidth(100);
	assert(r->getHeight() == 200 and r.getWidth() == 100);
}
```

i think another example is the ns2 simulator design.
There is a base class that basically has a recv() method only,
and all other classes simply inherit from this base class
and have different implementations on the recv() function.
