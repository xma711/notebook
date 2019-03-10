assert = require('assert')

var a = 1, b = 2

c = a+b

// btw, the console.log() is very similar to the print function in python2
assert(c === 3, "a plus b must equal to 3, but the result is " + c)

c= 5
assert(c === 3, "a plus b must equal to 3, but the result is " + c) // fail the assert deliberately

/*
=== and !== are strict comparison operators:

    JavaScript has both strict and type-converting equality comparison. For strict equality the objects being compared must have the same type and:

        Two strings are strictly equal when they have the same sequence of characters, same length, and same characters in corresponding positions.
        Two numbers are strictly equal when they are numerically equal (have the same number value). NaN is not equal to anything, including NaN. Positive and negative zeros are equal to one another.
        Two Boolean operands are strictly equal if both are true or both are false.
        Two objects are strictly equal if they refer to the same Object.
        Null and Undefined types are == (but not ===). [I.e. (Null==Undefined) is true but (Null===Undefined) is false]

*/
