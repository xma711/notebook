// load the express module
var express = require('express');
app = express.createServer();

// respond to requests for / with 'Hello World'
app.get('/', function(req, res) {
	res.send('Hello World!');
})

// listen on port 80 (like a true web server)
app.listen(80)
console.log('Express server started successfully')
