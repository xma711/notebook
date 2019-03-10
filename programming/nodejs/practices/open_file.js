// fs is the module that handles file system
fs = require('fs')

// define a callback function for the readfile api
read_content = function(err, data) {
	if (err) {
		return console.log(err)
	} else {
		console.log(data)
	}
}

// use the api with a self-defined callback function
fs.readFile('/tmp/helloworld.txt', 'utf8', read_content)
