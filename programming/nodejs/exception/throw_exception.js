// check if the stuff after an exception is thrown will be executed or not

var throw_in_middle = function() {
	console.log("before throw exception...");

	throw new Error('exception');

	// it turns out this line won't be executed, which is good
	console.log("after throw exception ...");

}


var test_function = function () {
	try {
		throw_in_middle();
	} catch(err) {
		console.log('in test_function. catch an exception: ' + err);
		return;
	}
}


test_function();


// 2nd test, check whether an intermediate function will throw the err
var throw_in_middle_wrapper = function () {
	// the program won't die here if someone that calls throw_in_middle_wrapper tries to catch the exception
	// this means this function will automatically re-throw the exception to whoever that calls this function
	throw_in_middle();
}

var test_function2 = function () {
	try {
		throw_in_middle_wrapper();
	} catch(err) {
		console.log("in test_function2. catch an exception: " + err);
	}
}

test_function2();

// 3rd test, add one more layer
var second_wrapper = function() {
	throw_in_middle_wrapper();
}

var test_function3 = function () {
        try {
                second_wrapper();
        } catch(err) {
                console.log("in test_function3. catch an exception: " + err);
        }

}

test_function3();
