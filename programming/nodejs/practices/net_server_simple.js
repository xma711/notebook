// an echo server
// a server created by net.
// note that http is built on top of net and http is more for web-based applications.
// net is for generic TCP server-client application.
// reference: http://www.tutorialspoint.com/nodejs/nodejs_net_module.htm

var net = require('net');

var server = net.createServer(
	// the callback function for the "connection" event
        // the callback format is something like callback(conn)
	function(conn) {
		console.log("a new connection happens");

		// conn is the instance for the this particular client
		// conn is a stream.
                // conn itself is an eventEmitter object because stream itself is an EventEmitter
		// add an action to the event 'end'
		conn.on('end', function (){
			console.log("client disconnected");
		});

		// write a greeting when the connection is first established
		conn.write("Hello world\r\n"); // write a message

		conn.addListener('data', function(data) {
				console.log("received data: " + data);
			}
		);

		// this event has to be handled because once the error is thrown the program will die if no one handle the error.
		conn.on('error', function(err) {
				console.log("Encountered error: " + err);
				conn.destroy();
			}
		);

		// what does this mean? this means that it is an echo server
		// it is writing any data it receives back to the socket
		conn.pipe(conn);
	}
); // end of net.createServer

server.listen(8080, function() {console.log("server is listening")} );

// get the connections number every 5 seconds
setInterval(
	function() {
		server.getConnections(function(err, count) {
				console.log("The number of connections the server has: " + count);
			} // end callback function in getConnections()
		); // end getConnections()
	},// end callback function
	5000
);

