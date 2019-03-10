// run this test by: nodeunit in one directory up or nodeunit ./test_module.js

// reference: http://caolan.org/posts/unit_testing_in_node_js/  (this reference could be outdated)  
// need to refer to https://github.com/caolan/nodeunit/issues/198 for the new way of defining tests

var module1 = require('../module1');
var events = require('events');
var ori_console_log = console.log; // keep the original one, later at tear down need to revert it back because nodeunit also use console.log() itself

// test the module1.double() function
module.exports = {
	// define setup function
	setUp: function(callback) {
		return callback();
	},

	// define tear down function
	tearDown: function(callback) {
		console.log = ori_console_log; // this line is important, because nodeunit itself uses console.log too
						// without doing this, the final test will complain
		return callback();
	},

	// first test
 	testDouble: function (test) {
		test.equal(module1.double(2), 4); // expecting doubling 2 equals 4
		test.done();
	}, // end of testDouble

	testReadStdin: function(test) {
		test.expect(1); // this is important! need to tell the test how many assertions are expected

		var hello = 'hello world!';
	
		var mock_stdin_ev = new events.EventEmitter();

		// replace the function by our mocking one
		process.openStdin = function() {return mock_stdin_ev;}

		process.exit = test.done; // test.done must be something from the nodeunit module itself

		// replace the console.log function too
		console.log = function(str) {
			test.equal(str, hello); // this is the assert we expect
		};

		// again, the process.openStdin(), process.exit() and console.log() functions are functions that 
		// appeaer in the read_stdin() function that we are testing.
		// that's why we need to mock them.

		// now execute the function we want to test.
		// unlike a synchronous function, this function won't have any return value.
		// so the way to test it is to mock the console.log and inside it there is a test statment
		module1.read_stdin();
	
		// okay, now mock writing something to stdin
		mock_stdin_ev.emit('data', hello);
	} // end of testReadStdin

}; // end of module.exports
