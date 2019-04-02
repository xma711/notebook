Some points on C++
-----------------------

From book: Sams Teach Yourself C++ in One Hour a Day (7th Edition)

- Reference is an alias of a variable!! This explains a lot. Pointer is another variable that stores an address as it's content.  
	note that to declare a reference, it is: int& ref = i; and then ref acts as if it is i itself; ref also behaves like a variable, not a pointer, although it affects the original i like a pointer.

- New will throw exception if failed.

- Sizeof(array) returns the whole size. Sizeof(pointer) is usually 4.

- There is this thing called lambda function. 
	refer to my own examples for easier understanding.

- when a child object is created, parent's constructor will be called first, and then child's constructor is called.  
	when the child object is deleted, child's destructor will be called first, and then parent's destructor will be called (i.e. the reverse order of the constructor calls).

- When pass an object by value, it is a shallow copy, meaning pointers are copied over but not the contents that the pointers point to. 
	The function that accepts this input will create a new object and later will free the object which may include freeing the memory for the pointers. 
	So the pointers in the original object are freed too. Later it will cause problems. 
	The solution is to create a constructor to auto handle the copy case. 
	One has to explicitly create new buffer for pointers and copy contents from the input object to the new pointers.. 
	however, even with this, when using a=object, a will be a shallow copy of object. 
	To further solve this, need to override the "operator = " function in the object class.. 
	this is quite cool. Operator is nothing new but a function itself.  
	for a simple example of copy constructor, refer to my own examples.

- To disallow an object being copied, just define the copy constructor header and operator= constructor header under private..

- If I want only one exact same object no matter how many times they are instantiated, use Singleton. 
	To achieve this, follow the lastpoint first (disallow an object being copied). Also put normal constructor under private. 
	Then use static keyword on a normal method like getInstance(), which makes it a class method instead of an instance method. 
	Inside the method, create a static object of the class itself and return.

- Btw static makes a variable or function a class level, which is shared across objects..

- If I want a class to be in heap (i.e. only allow keyword 'new' to create this object) but cannot be in stack (i.e. disallow normal instantiation), 
	make destructor in private but create a customized destructor in public.

- If a class allows a global method to access it's private attributes, use friend function header. 
	If to allow another class to access, use friend class name.

- Without virtual on a method, subclass can still overwrite the method. 
	But once it (as a reference) is passed into a function that uses the base class as the argument type, 
	the function will still call the base class's method. 
	To avoid this, use virtual in the base class's methods that need to be polymorphic. 
	Note that destructor had to be virtual so that any function is able to call the right destructor (i.e. child's destructor, which will then call parent's destructor).

- inheritance has 3 levels. 
	the easiest is that for a common class (no virtual methods), we just do an inheritance and override some methods; polymorphism cannot be used in this case.
	a better design is that the parent class should have virtual methods, so that polymorphism can be used;
	an even better one is that we create an abstract class, and then we create derived classes from this abstract class. this is useful for performing unit testing too.

- An abstract class in c++ is the same as an interface in Java. 
	To make a abstract class in c++, simply define all methods as virtual method name(args)=0 (this is called a pure virtual function). 
	(Or some of the methods if only these methods are required to be implemented by subclass.
	any class with one or more pure virtual functions is an ADT (abstract data type), and it is illegal to instantiate an object of a class that is an ADT.

- inheritance allows child class to have its own methods. but this will break polymorphism, because the base class's vtable doesn't have a pointer to the method that exists only in child class.
	if this really happen, it could be a design problem.
	if there is no other way to do it but to have a special method in the derived class, then we have smartly cast the base class pointer to the derived class in a function. this is not very elegant of course.

- To solve the diamond problem, use virtual keyword on the intermediate derived class definition, something like class derivedClass : public virtual baseClass {}

- Operators, like methods, can be overwritten by classes.. this allows a customized class to use operators like ++..

- The style of casting types i know is actually c-style. C++ has its own style, something like castType <destinationType> object.

- The map lib is like the python dictionary.

- A function object is a class that implements operator() and makes the resultant object behave like a function.

- Lambda function is a function object without a name. It is like the 'closure' in JavaScript or Swift.

- Closure in other languages means it closes the parent environment (able to access variables etc). 
	And it is an anonymous function too (I.e. lambda function). A lambda function in c++ cannot access parent scope.

- Lambda function is just a succinct representation of a class or structure with operator().

- C++ has a bitset class, which is able to store bits. E.g. bitset<5> fivebits ("10110"); 
	another more flexible way is to use vector<bool>, which size can be adjusted dynamically (unlike bitset).

- C++ has this smart pointer (contrast to conventional raw pointer). 
	It is actually a class with overloaded operators, something like a wrapper around the raw pointer. 
	One advantage of this is that it can auto-free the memory after use! 
	The specific class we can use is std:: unique_ptr. Don't use the auto_ptr which is obsolete!

- There are many different smart pointer types, such as deep copy, copy on write (cow), reference-counted, reference-linked, destructive copy..

- Exception handling: try{codes;} catch(specific _exception){codes;}catch?(...){codes;}; the 2nd catch is to catch any type of exception.


More specific - hour 5 calling functions
----------------------------

Modern compilers do  good job on their own of making c++ code execute quickly,
so there is often little to be gained from declaring a function inline.

Anyway, to make a function inline, just put an "inline" keyword in front of function prototype (in both .h and .cpp files).


More specific - hour 10 stack and heap
------------------------------

After delete a pointer (i.e. free memory), set the pointer to NULL.
This makes a 2nd delete of the same pointer harmless.  
However, NULL actually is equivalent to 0 in c++. it is better to use "nullptr" which will not be converted to 0.  
To use nullptr, have to compile with flag" -std=c++11".

When using new, remember to use delete to free the memory.
Otherwise there could be memory leak.

Btw, memory leak happens when we allocate some memory from heap,
but later we lose the pointer to this memory while the memory allocated is still there.
Then there is no way to free it until the program ends.


More specific - hour 11 advanced pointers
----------------------------------

Const int *p1; // a pointer to a constant integer. 
		// the value that is pointed to cannot be changed using THIS pointer.

Int* const p2; // a constant pointer to an integer.
		// this pointer cannot be reassigned.

Const int* const p3; // a constant pointer to a constant integer


more specific - hour 12 references
-----------------------------------

A reference is an alias.  
The syntax is something like: int &rSomeRef = intOne;

note that it is different from &intOne, which is the address of intOne variable.

After creation of rSomeRef, then &rSomeRef and &intOne are the same result -  the address of the original intOne.

When a method is defined as void swap (int &rx, int &ry),
it means it is expecting references to be passed in.
Operations on rx and ry in the swap function have real effects on the source x and y.
But in swap() function, they treat rx and ry as variables instead of pointers.  
(if this is too confusing, then just use pointers..)


Const behind a method
---------------------------

Reference: http://stackoverflow.com/questions/9790927/what-does-const-behind-a-function-header-mean  
and http://stackoverflow.com/questions/4059932/what-is-the-meaning-of-a-const-at-end-of-a-member-function

it means that *this is a const inside that member function,
i.e. it cannot alter the object.  
If the member function is declared const, the type of this is "const CLASSNAME*" !


To prevent copy and assignment (i.e. =) operation
-----------------------------------------------

Just place the copy constructor and operator= method in "private".  
Example (inside the BH1750 class):  
```
    private:
        BH1750(const BH1750&);
        BH1750& operator=(const BH1750&);
```

another way is declare a macro that any class can use. e.g.  
```
#define DISALLOW_COPY_AND_ASSIGN(TypeName) \
  TypeName(const TypeName&);               \
  void operator=(const TypeName&)
```
Then in the BH1750 class, i just have to do:  
```
private:
DISALLOW_COPY_AND_ASSIGN(BH1750);
```


class inheritance
-------------------

Reference: http://stackoverflow.com/questions/860339/difference-between-private-public-and-protected-inheritance

There are three accessors that I'm aware of: public, protected and private.

Let:

class Base {
    public:
        int publicMember;
    protected:
        int protectedMember;
    private:
        int privateMember;
};

Everything that is aware of Base is also aware that Base contains publicMember.  
Only the children (and their children) are aware that Base contains protectedMember.  
No one but Base is aware of privateMember.  
By "is aware of", I mean "acknowledge the existence of, and thus be able to access".

Next:

The same happens with public, private and protected inheritance. Let's consider a class Base and a class Child that inherits from Base.

If the inheritance is public, everything that is aware of Base and Child is also aware that Child inherits from Base.  
If the inheritance is protected, only Child, and its children, are aware that they inherit from Base.  
If the inheritance is private, no one other than Child is aware of the inheritance.

'''
Class A 
{
public:
    int x;
protected:
    int y;
private:
    int z;
};

class B : public A
{
    // x is public
    // y is protected
    // z is not accessible from B
};

class C : protected A
{
    // x is protected
    // y is protected
    // z is not accessible from C
};

class D : private A
{
    // x is private
    // y is private
    // z is not accessible from D
};
'''

regarding volatile keyword
-----------------------------

Reference: http://stackoverflow.com/questions/72552/why-does-volatile-exist

volatile is needed if you are reading from a spot in memory that 
a completely separate/device process may write to.

This is to prevent the compiler optimizes the codes regarding the volatile variable away.  
This kinda forces the compiler to make sure every time we need to read/write the value, it will do it;
instead of assuming the value is not changed since last read/write.

Another explanation is that by declaring an object to be volatile, we are telling the compiler that
the object might change state even though no statements in the program appear to change it. 
(that's why the object is 'volatile'!)

