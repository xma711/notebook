
try {
	// deliberately throw an error for catch block to log the error;
	// one way to log different type of errors with one single catch block
	throw new Error("throw error in try!");
} catch(err) {
	console.log("in catch block. catch an exception: " + err);
}

