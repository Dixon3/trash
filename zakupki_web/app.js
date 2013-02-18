
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , report = require('./routes/report')
  , user = require('./routes/user')
  , http = require('http')
  , path = require('path');

var stache = require('stache');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(express.cookieParser('your secret here'));
  app.use(express.session());
  app.use(app.router);
  app.use(require('stylus').middleware(__dirname + '/public'));
  app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
//app.get('/:collection',routes.database);
//app.get('/:database/:collection',routes.collection);

//app.get('/:database/:collection/:_id',routes.item);
app.get('/reports',report.reports)
app.get('/report/new',report.report_new)
app.post('/report/new',report.report_new)
app.get('/report/:_id/',report.report_id)
app.get('/report/:_id/run',report.report_run)
app.get('/report/:_id/show',report.report_show)
app.get('/report/:_id/edit',report.report_edit)
app.post('/report/:_id/edit',report.report_edit)
//Work over collections
app.get('/:collection/',routes.collection);
app.get('/:collection/find/:_id/',routes.item);
app.get('/:collection/find/',routes.collection_by_field_and_fields);
app.get('/:collection/:pk_field/:val/',routes.collection_by_field);
app.get('/:collection/:pk_field/:val/fields/:fields/',routes.collection_by_field_and_fields);
app.get('/users', user.list);




http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
