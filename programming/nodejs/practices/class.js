
// imagine there is a "hello_world_class" class already
// now proceed to declare its constructor and methods ..

// constructor
function hello_world_class(num) {
	this.num_greetings = num;
}

// declare a method
// in fact, it is just a method name = a local function
// this means i can declare a local function first and equal the method to this local function
// note that need to add "prototype" in the middle
hello_world_class.prototype.greeting = function greeting () {
	var i = 0
	while (1) {
		console.log("Hello world!");
		i++;
		if (i >= this.num_greetings) {
			return; // stop the loop
		}

	}
}

// export it if needed
module.exports = hello_world_class

// declare an object 
var object = new hello_world_class(10)
// run a method
object.greeting()
