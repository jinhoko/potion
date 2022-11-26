var express = require('express');
var http = require('http')
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var showdown  = require('showdown')

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();
app.set('view engine','ejs');
app.set('views','./views');

app.set('port', process.env.PORT || 3000);
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


app.use('/', indexRouter);
app.use('/users', usersRouter);

module.exports = app;

http.createServer(app).listen(app.get('port'), function(){
    console.log('Express server listening on port ' + app.get('port'));
});