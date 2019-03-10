// set two timers for 2 functions that have while loops inside
// in fact, the first function has 2nd while loop for 5 seconds
// this example is to show that when nodejs enters a callback function, it will finish it before moving on to the next callback.
// this is because nodejs is single-thread..
// this means that a callback function shouldn't be running for too long. it should be very fast one.

// a first function with blocking waiting time
var while_loop_func1 = function() {
	i = 0
	while (1) {
		console.log("a: hello world " + i)
		i++
		if (i > 20) {
			break;
		}
	}

	// create some artifical sleep duration.. which should never be used in reality
	// this is just to show that once entering a function, the thread will finish this function first before proceeding to the next
	console.log("Now going to loop for another 5 seconds")
	var stop = new Date().getTime();
	while(new Date().getTime() < stop + 5000) {
        ;
	}
	console.log("looping done")
}

// 2nd function with immediate execution
var while_loop_func2 = function() {
	i = 0
	while (1) {
		console.log("b: hello world " + i)
		i++
		if (i > 20) {
			break;
		}
	}
}

// for a callback function, there shouldn't be arguments, like while_loop_func(), which will cause the function to be executed immediately
setTimeout(while_loop_func1, 3000)

setTimeout(while_loop_func2, 3000)

console.log("end of program")

