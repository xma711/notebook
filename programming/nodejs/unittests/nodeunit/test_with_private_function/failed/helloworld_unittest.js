var hello = require('./helloworld') // need to add ./ to indicate the path..

// try with private variables

hello.print_private_var();

var copy_var = hello.get_private_var();

copy_var = "changed var" // no effect on the real private var in helloworld.js

hello.print_private_var();


// now try with private functions
hello.execute_private_function();

var copy_func = hello.get_private_function();

copy_func = function() { // also no effect on the real private function
	console.log("i want to change the private function");
}

hello.execute_private_function();
