// reference: http://www.tutorialspoint.com/nodejs/nodejs_net_module.htm

net = require('net')

// create a connection to server
// a net.Socket object
//conn = net.connect({port: 8080, host: 'whatever'}, function() {
conn = net.connect(8080, "localhost", function() {
		// doesn't seem to have argument for this callback
		console.log("connected to localhost");
	}
);

// apparently, net.connect supports two different types of inputs, one is "port[, host][, connectListener]" and the other is "options[, connectionListener]";
// the later allows a json/dictionary object
// while the former allows simple inputs with port, host, and callback

// based on online reference, there is no real function overloading in JavaScript since it allowes to pass any number of parameters of any type. 
// You have to check inside the function how many arguments have been passed and what type they are.

// this conn must be from the same class as that of the connection object created when a server receives a new connection from a client

// catch error if there is any
conn.on('error', function(err) {
	console.log("Encountered error: " + err);
});

// when received data, print it; data is a buffer i think
conn.on('data', function(data) {
	console.log("Data received is: " + data.toString());

	console.log("bytes read: " + conn.bytesRead);

//	conn.write("Hello too!\r\n");

	// end the connection, which will make the event 'end' emiited
//	conn.end();
});

// the end event
conn.on('end', function() {
	console.log("Disconnect from the server");
});
