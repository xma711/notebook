Swift
---------------------

previously Apple uses objective-c for app development for iphone and ipad.  
in 2014 apple annouced a new language Swift that will be used for app development instead.

overall reference: sams teach you swift in 24 hours (swift 1.0)


install swift in linux
--------------------------

swift is for the Apple app development platform xcode6.

however, the language itself can be installed in ubuntu linux.  
just follow: https://swift.org/download/#using-downloads  
(anyway it is just to download a tar, and export it to somewhere that PATH knows.)

to check how to write a program in swift in linux, refer to the example folder.  
one reference: https://itsfoss.com/use-swift-linux/


variables & constants
-----------------------

they are like java variables, each one is a class itself.  
e.g. Int, Double, Float.

to declare a variable, it is something like: var variable_name: type = value / expression  
to declare a constant, it is: let constant_name: type = value

the ': type' is optional; swift is smart enough to figure out what type of the input is.

examples: var i : Int = 1; (or simply "var i = 1")  
let j : String = "hello world!"; (or simply "let j = "hello world!"")


optionals
-----------------------

optionals are new concept in Swift.  
for normal variables, they cannot be nil in swift.

to allow this, there is a new type called optional.

optional is like a box containing a normal variable (cannot be constant).  
whenever we use optional, we need to firstly check if it is 'nil', if it is, use some ways to handle this.  
if it is not nil, then we can safely unwrap the optional to get the variable inside.

optional can be created with any variable type.  
example:  
var myString: String? = "Hello"; // note that there is a '?' in the normal variable declaration. simply doing this turns the variable to a optional.  
to check if this optional is nil, use:  
if myString != nil {  
	// do something;  
}
or  
if let string1 = myString {  
	// do something;  
	// btw, string1 is already an unwraped version of myString, i.e. the variable inside. this method to unwrap the optional is recommended  
}

another way to safely unwrap the optional: var x = myString ?? alternativeValue;

other ways: http://stackoverflow.com/questions/25195565/how-do-you-unwrap-swift-optionals


array, dictionary and tuple
----------------------------

array is like python list .. but unlike python list, an array in swift can only hold one type of data.

dictionary is like python dictionary .. the types for keys in swift are more limited.

tuple is like python tuple. tuple in swift can hold anything i think.


control flow
------------------

the usual if..else, while loop, for loop, for item in array, etc.

there is also switch, like in C.  
however, the switch in swift is more powerful, it can accept not just int (which is the case in c), 
but can be a range, or many types..


functions
--------------------

functions are like c functions.  
each function's parments have their types, and return has its type too.

but there are some extra features, like the parameter can have an external name (like a key in python function)
and an internal name (just the normal variable names).

the return value can be a tuple too.  
the types of each variable in the tuple are defined in the function header. 

format:  
funct functionName(parameter1: type, parameter2: type) -> returnTyupe {  
	statements;  
	return value;  
}


the function parameters can be reference types too, just like the "int * input1" in C or C++.  
in swift, the syntax is "parameterName: inout parameterType" (e.g. number: inout Int).

when calling this function, the variable input becomes &variable, exactly like what we do in C.  
e.g. function1( &variable1 )


closure
---------------------------

in fact, there are 3 types of functions, the global functions (the 'normal' ones),
nested functions, and closure expression.

nested functions are just functions defined inside a parent function.  
outside the parent function it is not accessible.  
the nested function is able to access and modify the variables defined in the parent function.  
in fact, this is very similar to nested functions in Node.js.

the last type, is a function without a name, and defined inside a {} directly.  
sounds familiar? it is very similar to the function without a name in Node.js or Javascript. 
(in node.js, such a f unction starts with function(){} ).

closure expression is usually used when it is passed in as a parameter to another function.  
another way of doing this is that we define a nested function or global function first, and then pass it in as a parameter.  
but for those that will be used only once and is short function, it may be neater to pass a closure expression as a parameter directly.

to define a closure expression, the complete way is  
{  (parameters: types) -> return_type in // the keyword in separates the header from the content of the function
    statements;  
    return value;  
}

however, this format can be greatly simplified.  
firstly, the (parameters: types) can be removed if the types are very obvious (the compiler can infer the types);  
secondly, the parameter names inside the functions can be referred by $0 $1 .. just like shell script.  
also, the return statement can be omiited too if the function is very simple (maybe just one line of code). 
the compiler is smart enough to know that the result from the only line of code is the return value;  
lastly, if it is a boolean result with something like "$0 > $1", it can be further simplifed to (>)..

also, the closure expression doesn't have to be inside the parameters list () of a function;  
it can be placed after the (), because usually the function parameter is at the last parameter in the list.
something like: function1(parameter1) {return $0+$1} // which is equivalent to function1(parameter1 : inputValue, parameterFunction: {return $0+$1})  
this is called "trailing closures".  
(compared to this trailing closure, the many () in Node.js functions seem more helpful to let us understand which function is which function's parameter.)

one example: https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html


struct and class
--------------------

struct and class are very similar. both can have variables and methods.

the main difference is that when declaring a struct, it is a variable type; while an object from a class is reference type.  
examples are the built-in Int, Double, String..  
when we do something like: a = b; // where b is a struct,  
we actually make a complete copy of b to a.
when we modify a, it won't affect b.  

if b is an object declared from a class, then a = b meaning a and b both point to the same memory area, thus the same object.
(exactly the same as the pointers in C.)  
if we make a change to a, then b will experience the same change.

methods in struct by default cannot modify variables.
to make them able to do so, add a keyword "mutating" in front of the method declaration.

also struct doesn't have a constructor. 
but we can assign a default value to each variable when defining the struct.

class has a constructor. anyway, class is almost exactly the same as the class concept in other programming languages.

struct can be used if we want to store a short list of data.  
(just imagine how we use struct and class in C++. similar idea applies here.)


enum
-----------------

enum in C is just to make a list of meaningful items with internal value from 0 to whatever.  
it is a bit like defining a new type with a finite set of values.

enum in swift shares this property too, but has much more other properties.

1stly, enum in swift doesn't have to be int. they can be many common types.  
in the header of a enum declaration, i can declare what type of internal values (raw values) will the elements be.  
when it is Int, it falls back to the c style enum. the raw values can be auto-complete too, just like c.  
when it is other type, like Double or String, then the raw value has to be declared and fixed when creating the enum.

another alternative way is to create a (paramter list) for each single element in a enum, without having to declare the exact values yet.  
when user declare an enum variable, he set set the corresponding values for parameters of an element, which looks like a constructor.  
later he can retrieve these values when needed.

also, enum in swift can have methods.  
so it seems enum in swift is very  close to a class.  
anyway, the method declaration is similar to that in a class. there is "this" keyword too.  
from the method's point of view, each element in the enum is like a private variable that it can access.  
ultimately, if i declare an enum variable, i can call the method using the common varableName.method().
