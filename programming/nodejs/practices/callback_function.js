// an example to show how to pass a callback function into another function
// and how the callback function is used in the caller function

// this will be the callback function
var print_func = function(a) {
	console.log(a)
}


// this is the caller function that needs the callback function to do something
// argument of the main_function only tells us that it needs a callback function, which can handle a string.
// the real implementation of the callback function has to be done by whoever that wants to use this function
var main_function = function(callback) {
	
	callback("called from main function")
}
// when we use some built-in aysnc functions, like http.createServer( function{} ), 
// the http.createServer(callback) has been defined somewhere so we just use it.
// we need to implement our own callback function and pass it in as an argumenet

// this is the real execution of the main_function
// note that i need to pass the exact name of the callback function into the main function
main_function(print_func)

// of course, i can also pass the function(a) {console.log(a)} directly into the main function..
main_function( function(b) {console.log(b)} )


// an random function that will be called by the main3 function
var some_action = function ( do_something_callback) {
	do_something_callback();
}

main3 = function() {
	var string = "hello 3"; //  string is local to main3 function
	// inside main3, it calls the some_action function;
	// the callback function is an argument to the some_action function
	// surprisingly, the callback function is able to access the resources defined in the main3 function!!!
	some_action (
			function () {
				console.log(string); // a callback function has access to all the resources in main3 function
			} // end of the callback function
	); // end of some_action function

	// declare a callback function first;
	// this way also works!
	var cb2 = function () {
		console.log("2nd type: " + string); 
	};

	some_action (cb2); // end of some_action function
}


main3() ;

console.log("end of program")
