Swift
---------------------

Previously Apple uses objective-c for app development for iPhone and iPad.  
In 2014 apple announced a new language Swift that will be used for app development instead.

Overall reference: sams teach you swift in 24 hours (swift 1.0)


install swift in Linux
--------------------------

Swift is for the Apple app development platform xcode6.

However, the language itself can be installed in Ubuntu Linux.  
Just follow: https://swift.org/download/#using-downloads  
(anyway it is just to download a tar, and export it to somewhere that PATH knows.)

To check how to write a program in swift in Linux, refer to the example folder.  
One reference: https://itsfoss.com/use-swift-linux/


variables & constants
-----------------------

They are like java variables, each one is a class itself.  
E.g. Int, Double, Float.

To declare a variable, it is something like: var variable_name: type = value / expression  
to declare a constant, it is: let constant_name: type = value

the ': type' is optional; swift is smart enough to figure out what type of the input is.

Examples: var i : Int = 1; (or simply "var i = 1")  
let j : String = "hello world!"; (or simply "let j = "hello world!"")


Optionals
-----------------------

Optionals are new concept in Swift.  
For normal variables, they cannot be nil in swift.

To allow this, there is a new type called optional.

Optional is like a box containing a normal variable (cannot be constant).  
Whenever we use optional, we need to firstly check if it is 'nil', if it is, use some ways to handle this.  
If it is not nil, then we can safely unwrap the optional to get the variable inside.

Optional can be created with any variable type.  
Example:  
var myString: String? = "Hello"; // note that there is a '?' in the normal variable declaration. simply doing this turns the variable to a optional.  
To check if this optional is nil, use:  
if myString != nil {  
	// do something;  
}
or  
if let string1 = myString {  
	// do something;  
	// btw, string1 is already an unwrapped version of myString, i.e. the variable inside. this method to unwrap the optional is recommended  
}

another way to safely unwrap the optional: var x = myString ?? alternativeValue;

other ways: http://stackoverflow.com/questions/25195565/how-do-you-unwrap-swift-optionals


array, dictionary and tuple
----------------------------

Array is like python list .. but unlike python list, an array in swift can only hold one type of data.

Dictionary is like python dictionary .. the types for keys in swift are more limited.

Tuple is like python tuple. tuple in swift can hold anything i think.


Control flow
------------------

The usual if..else, while loop, for loop, for item in array, etc.

There is also switch, like in C.  
However, the switch in swift is more powerful, it can accept not just int (which is the case in c), 
but can be a range, or many types..


Functions
--------------------

Functions are like c functions.  
Each function's parameters have their types, and return has its type too.

But there are some extra features, like the parameter can have an external name (like a key in python function)
and an internal name (just the normal variable names).

The return value can be a tuple too.  
The types of each variable in the tuple are defined in the function header. 

Format:  
funct functionName(parameter1: type, parameter2: type) -> returnTyupe {  
	statements;  
	return value;  
}


the function parameters can be reference types too, just like the "int * input1" in C or C++.  
In swift, the syntax is "parameterName: inout parameterType" (e.g. number: inout Int).

When calling this function, the variable input becomes &variable, exactly like what we do in C.  
E.g. function1( &variable1 )


closure
---------------------------

In fact, there are 3 types of functions, the global functions (the 'normal' ones),
nested functions, and closure expression.

Nested functions are just functions defined inside a parent function.  
Outside the parent function it is not accessible.  
The nested function is able to access and modify the variables defined in the parent function.  
In fact, this is very similar to nested functions in Node.js.

The last type, is a function without a name, and defined inside a {} directly.  
Sounds familiar? it is very similar to the function without a name in Node.js or Javascript. 
(in node.js, such a f unction starts with function(){} ).

Closure expression is usually used when it is passed in as a parameter to another function.  
Another way of doing this is that we define a nested function or global function first, and then pass it in as a parameter.  
But for those that will be used only once and is short function, it may be neater to pass a closure expression as a parameter directly.

To define a closure expression, the complete way is  
{  (parameters: types) -> return_type in // the keyword in separates the header from the content of the function
    statements;  
    return value;  
}

however, this format can be greatly simplified.  
Firstly, the (parameters: types) can be removed if the types are very obvious (the compiler can infer the types);  
secondly, the parameter names inside the functions can be referred by $0 $1 .. just like shell script.  
Also, the return statement can be omitted too if the function is very simple (maybe just one line of code). 
The compiler is smart enough to know that the result from the only line of code is the return value;  
lastly, if it is a Boolean result with something like "$0 > $1", it can be further simplified to (>)..

Also, the closure expression doesn't have to be inside the parameters list () of a function;  
it can be placed after the (), because usually the function parameter is at the last parameter in the list.
Something like: function1(parameter1) {return $0+$1} // which is equivalent to function1(parameter1 : inputValue, parameterFunction: {return $0+$1})  
this is called "trailing closures".  
(compared to this trailing closure, the many () in Node.js functions seem more helpful to let us understand which function is which function's parameter.)

One example: https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html


struct and class
--------------------

Struct and class are very similar. both can have variables and methods.

The main difference is that when declaring a struct, it is a variable type; while an object from a class is reference type.  
Examples are the built-in Int, Double, String..  
When we do something like: a = b; // where b is a struct,  
we actually make a complete copy of b to a.
When we modify a, it won't affect b.  

If b is an object declared from a class, then a = b meaning a and b both point to the same memory area, thus the same object.
(exactly the same as the pointers in C.)  
If we make a change to a, then b will experience the same change.

Methods in struct by default cannot modify variables.
To make them able to do so, add a keyword "mutating" in front of the method declaration.

Also struct doesn't have a constructor. 
But we can assign a default value to each variable when defining the struct.

Class has a constructor. anyway, class is almost exactly the same as the class concept in other programming languages.

Struct can be used if we want to store a short list of data.  
(just imagine how we use struct and class in C++. similar idea applies here.)


Enum
-----------------

Enum in C is just to make a list of meaningful items with internal value from 0 to whatever.  
It is a bit like defining a new type with a finite set of values.

Enum in swift shares this property too, but has much more other properties.

1stly, enum in swift doesn't have to be int. they can be many common types.  
In the header of a enum declaration, i can declare what type of internal values (raw values) will the elements be.  
When it is Int, it falls back to the c style enum. the raw values can be auto-complete too, just like c.  
When it is other type, like Double or String, then the raw value has to be declared and fixed when creating the enum.

Another alternative way is to create a (parameter list) for each single element in a enum, without having to declare the exact values yet.  
When user declare an enum variable, he set set the corresponding values for parameters of an element, which looks like a constructor.  
Later he can retrieve these values when needed.

Also, enum in swift can have methods.  
So it seems enum in swift is very  close to a class.  
Anyway, the method declaration is similar to that in a class. there is "this" keyword too.  
From the method's point of view, each element in the enum is like a private variable that it can access.  
Ultimately, if i declare an enum variable, i can call the method using the common varableName.method().
