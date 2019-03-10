// define a function like C
function hello() {
	console.log("hello world!");
};

// call a function like c
console.log('i can call the function directly:')
hello()

// new in nodejs: use a variable to equal to the function header and then the variable acts like the function
console.log('\nor i can call the function by a variable that equals to the function header:')
var hello_var = hello // hello_var is a variable, while hello is the function header to hello() function
hello_var()

// set a timer with the original function
console.log('\ni can set a timer with the original function')
setTimeout(hello, 2000)

// or set a timer with the variable
console.log('\ni can set a timer with the variable')
setTimeout(hello_var, 3000)

// seems that there is no real distinctions between the c-like function name and a variable that equals to this function header

// functions themselves are 'blocking' in the sense that once the function is run, the single thread is executing this function until it is finished.
// of course the good practice is not to write a function that needs a long time to finish execution


// a c-like function with immediate return
function return_int () {
	return 9999;
};

console.log('\ntry a function with immediate return value:')
var num = return_int()
console.log(num)


// a c-like function with a pointer being set to a number; which is not supported in nodejs
function set_int(a) {
	a = 10000;
};
var num2;
set_int(num2)
console.log('\ntry a function with an argument equals to a number (unfortunately this fails. the returned answer is undefined):')
console.log(num2) // 

// based on http://stackoverflow.com/questions/10231868/pointers-in-javascript
// JavaScript does not support passing parameters by reference 
// (i guess nodejs also doesn't support passing parameters by reference)
// in fact, javascript just copies exactly the same thing to a function

// however, to simulate passing by reference, we need to use this Object variable, 
// when variable is declared as an object, the variable is a reference already.
// when it is copied to a function's argument, the exact same thing, i.e. the reference, is copied.
function set_val (obj) {
	obj.Value = 10000;
}

var x = {Value: 0}; // x looks like a json 
set_val(x)
console.log('\nlet x be an object so it is a reference already.\nset the Value in the x json object to a number:')
console.log(x.Value)
// In this case, x is a reference to an object. When x is passed to the function a, that reference is copied over to obj. 
// Thus, obj and x refer to the same thing in memory. 
// Changing the Value property of obj affects the Value property of x.

// it turns out that in this case hello_again is not defined. 
// so it is equivalent to just var hello2 = function() {}
var hello2 = function hello_agin() {
	console.log('hello again')
}

//hello3 = hello_again // there will be an error at this line because hello_again is not considered defined.
//console.log('\n see if i can declare another hello3 to an existing var hello2 = functon hello_agin(){}...:')
//hello3()
