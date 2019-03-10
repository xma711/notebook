// run two functions in sequntial
// the functions are called directly, not as callback functions 

var while_loop_func = function(a) {
	i = 0
	while (1) {
		console.log(a + ": hello world " + i)
		i++
		if (i > 20) {
			break;
		}
	}
}

// when i call these two functions sequentailly, they are in sequential also
while_loop_func("function1")

while_loop_func("function2")


console.log("end of program")

// now the question is, when will the function become async?
// when one of the argument has a callback function?
