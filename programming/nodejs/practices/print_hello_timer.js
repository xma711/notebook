// declare a function (later used as a callback function) and store it to a var
var function_helloworld = function () {
	console.log("hello world")
	setTimeout(function_helloworld, 2000) // set a timer to call itself
}


// setTimerout is like call a function but without waiting for return
// it doesn't matter if it is 
//setTimeout(function_helloworld, 2000)

function_helloworld() // like c, i cannot omit () even when there is no arguments;
// unlike c, if i forget to add (), nodejs won't complain, which makes it harder to debug this type of problems
