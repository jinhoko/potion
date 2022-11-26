var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');


/* GET home page. */
router.get('/', function(req, res, next) {

  if(res.query.header.length > 0){
    var options = {
      mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
      args: [res.query.header,]
    };
    PythonShell.run('../javascripts/script.py', options, function (err, results) {
      if (err) throw err;

    });
  }
  res.render('index', { title: 'Express', page : res.query.page });
});

module.exports = router;
