var http = require('http') // variable http could be an instance of the module 'http'; or an instance of the class 'http'
var url = require('url')
var fs = require('fs')

// use http's API to create a server
// this function returns a new instance of http.server
// http.createServer([requestListener])
// The requestListener is a function which is automatically added to the 'request' event.

// request is the type http.IncomingMessage
// response is the type http.ServerResponse
request_listener = function( request, response) {
	console.log("url = " + request.url)
	console.log("headers = " + request.headers)	
	var file_pathname = url.parse(request.url).pathname
	console.log('client tries to request for resource: ' + file_pathname.substr(1))

	// ok, try to open the file now, using fs's API
	fs.readFile(file_pathname.substr(1), 
		function (err, data) {
			if (err) {
				console.log(err);
				response.writeHead(404, {'Content-Type':'text/html'}); 
				// wait! how come this callback function knows response, which should be outside of its scope..
				// --> it turns out that a sub function is able to access all the resources in the parent function, even if the sub function is a callback function
				// this is every different from C.
			} else {
				response.writeHead(200, {'Content-Type':'text/plain'});
				//console.log(data.toString());
				response.write(data.toString()); 
			}
			response.end(); // end the response; this has to be in the callback function because it must be after response.write()
		} // end of callback function(err, data)
	);

	//response.writeHead(200, {'Content-Type':'text/plain'});
	//response.end('Hello World\n');	
};
// the request_listener will be added to the event 'request'
// the format is request_listener(request, response), 
// where request is the type http.IncomingMessage
// and response is the type http.ServerResponse
// https://nodejs.org/api/http.html#http_http_createserver_requestlistener
var server = http.createServer(request_listener); 

// when the 'request' event happens, listener request_listener will be fired off

// to run the server at a port:
server.listen(8001)

console.log('server running at http://localhost:8001')
