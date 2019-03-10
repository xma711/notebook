var express = require('express');
var router = express.Router();

/* GET test page */
// note that the '/' here refer to the 'root directory' of whatever the path specified in app.js;
// e.g. if app.js route to this file when client requests for '/test', then the route will become "/" in this file;
// if we use router.get('test', function(){} ) instead, we need to access this page at localhost:3000/test/test ..
// but anyway, now i know how to add sub pages under this route... (just imagine one route is one directory..)
router.get('/', function(req, res, next) {
  res.render('test', { title: 'creating test page' });
});

// under the same route, we can define a function to handle the post!
router.post('/', function(req, res, next) {  
  console.log(req.body)
  res.send("post successfully. message from the client is: " + req.body.text_input);
});

module.exports = router;
