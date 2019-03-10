var express = require('express');
var router = express.Router();

/* GET home page. */
// this means when the path in requesting url is '/', we will reder the index.js inside the view/ folder, while passing in an json-like object
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Test1' });
});

module.exports = router;
