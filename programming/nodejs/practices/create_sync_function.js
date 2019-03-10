
// this function allows a user to input a string and then the string will be printed x seconds later
var an_async_function = function (string, x_seconds) {
	console.log ("print the string '" + string + "' in " + x_seconds + " seconds")
	setTimeout(	function() {
				console.log(string);
			},
			x_seconds*1000
	); // end of setTimeout	
} // end of the async function


an_async_function("hello world", 4)

an_async_function("i will be first", 2)

// create a function to use a callback to act on a string;
// both string and callback are user inputs;
// the trick is to declare a callback function that wraps around the input callback and use it as the argument to the setTimout() function
var second_async_function  = function(string, callback, x_seconds) {
	console.log("use a callback function to act on string: " + string)
	setTimeout(	function() {
				callback(string);
			}, 
			x_seconds*1000);
// another way:
//var hello = "Hello World";
//setTimeout(alert, 1000, hello);
} // end of second_async_function


// declare a callback function that acts on a string
var print_string = function( str) {
	console.log('time to fire the callback function:')
	console.log(str)
}
// use the asyn function
second_async_function ("waiting for 6 seconds", print_string, 6)
