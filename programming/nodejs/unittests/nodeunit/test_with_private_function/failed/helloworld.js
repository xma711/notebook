var exports = module.exports = {}

var private_function = function() {
	console.log ("hello world from private function");
}

var private_var = "private"



exports.get_private_var = function () {
	return private_var;
};

exports.print_private_var = function() {
	console.log(private_var);
};

exports.get_private_function = function () {
	return private_function; // return the function, not equal to this function
};

exports.execute_private_function = function () {
	private_function();
};
