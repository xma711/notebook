// export this module so that other nodejs files can use this module
// reference: http://www.sitepoint.com/understanding-module-exports-exports-node-js/
// i think one way to make things neater is that i declare local functions first
// then at the end of the file i just export thoese functions that i want to export

// declare an exports object; apparently, 'module' doesn't have to be imported
// this is simply a python-like dictionary
// the keys are the function/class names, and the values are the real function implementations
var exports = module.exports = {}

// the above line is not equivalent to:
//module_again = require('module')
//var exports = module_again.exports = {}

say_hello_in_english_local = function() {
	console.log("Hello");
}

exports.say_hello_in_english = say_hello_in_english_local

exports.say_hello_in_spanish = function() {
	console.log("Hola");
}

// this creates a function require('./greeting_export').say_hello_in_english.longer_greeting() that has nothing to do with say_hello_in_english();
// this can be confusing though, because we may tend to think longer_greeting() is a method in say_hello_in_english() but it is not.
exports.say_hello_in_english.longer_greeting = function() {
	console.log("Hello! How do you do!");
}

// declare a local function first; then link it to an exported function
// this means that this file can have other local functions that assist an exported function but the local functions do not have to be exposed
function say_hello_in_german_local () {
	console.log("Hallo")
}

// export the local function
exports.say_hello_in_german = say_hello_in_german_local

// let's create a local class "greetings_in_different_languages" and later export it
// constructor
function greetings_in_different_languages () {
	console.log ('object greetings_in_different_languages is initiated');
	this.number = 3; // try if other module can see this number --> yes 
}
// methods
greetings_in_different_languages.prototype.say_hello_in_english = say_hello_in_english_local
greetings_in_different_languages.prototype.say_hello_in_german = say_hello_in_german_local

// export the class
// it looks like i just have to export the constructor
exports.greetings_in_different_languages = greetings_in_different_languages

console.log(exports)

var num = 1; // try if another file  is able to get this --> it turns out this will fail

exports.num = num; // but this is okay
exports.num2 = num22 = 1234; // num2 cannot be used locally
num33= 333; // global global variable

greetings_in_different_languages.prototype.set_some_numbers = function (a, b, c) {
	this.a = a;
	this.b = b;
	if (c == undefined) {
		console.log("set c to default value 3");
		c = 3;
	}
	
	this.c = c;
	console.log("a,b,c = " + a + "," + b + "," + c);
	console.log("in export: num22 = " + num22);
}

