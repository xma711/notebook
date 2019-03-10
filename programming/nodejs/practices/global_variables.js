// declare variables
var string="hello world" // anything outside of a function in the same file can be accessed by all functions
var num = 9999

num33 = 33; // this one is real global variable; any file that import this file will be able to read this number..  use with care! 

// try a function with the variables declared above
var print_hello = function () {
	console.log(string); // the string is automatically global variable.. 
	console.log(num)
	// in fact, this is similar to python; variables declared outside functions are global variables by default
}

// call the function
print_hello()
