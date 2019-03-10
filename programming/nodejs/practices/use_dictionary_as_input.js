// try to pass a json object as an argument to a function

// to allow fun1 to get different types of argument, one way is to check inside the function how many arguments have been passed and what type they are.
var fun1 = function (obj) {
	console.log("port = " + obj.port);
	console.log("ip = " + obj.ip);
}


// call the function
fun1( {ip: "localhost", port: 8080});

// this will result port and ip to be undefined..
fun1(8080, "192.168.1.132");
