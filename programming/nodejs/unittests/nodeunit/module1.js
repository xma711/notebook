// this one is synchronous function, which is relatively easy to be tested
exports.double = function(num) {
	return num *2;
};

// this is an asynchronous code
exports.read_stdin = function() {
	var stdin = process.openStdin(); // stdin is eventEmitter

	// listen for event "data"
	stdin.on('data', function(chunk) {
			console.log(chunk); // print the stdin
			process.exit();
		} // end of function(chunk)
	);
};
// how to test this read_stdin function?
// we need to mock the function process.openStdin(), so later we can mock the case that there is an input in the stdin.
// also, process.exit() cannot tell us if the function is sucessful, so we also need to mock the exit function.
// finally, we also need to mock console.log so that we can verify if the 'chunk' msg is what we key in 
