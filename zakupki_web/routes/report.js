var server = require('../model/database.js').server;
var ObjectId = require('../model/database.js').ObjectId;
var Sequence = require("futures").sequence;
var database = server.db('zakupki');
var reports =database.collection(reports);


exports.reports=function(req,res){

	reports.find({},{"_id":1,"description":1}).toArray(function(err,items){
		console.log(items)
		res.render('reports',{title:'Reports:',reports:items})
		})

}


//app.get('/report/:_id',routes.report)
exports.report_id=function(req, res){
	var id = new ObjectId(req.params._id);
	console.log(id)
	reports.findOne({_id:id},function(err,item){

		console.log(item)
		console.log(item.description)
		res.render('report',
		{
			title:item.description,
			rep:item
		})	
	})
}



//app.get('/report/:_id/new',routes.report_new)
exports.report_new=function(req, res){


	res.render('report_new',{title:'Create new report'});

	if(req.method=='POST'){

	console.log(req);

	var report={}
	report['datasource1']=req.param('ds1');
	report['datasource2']=req.param('ds2');
	report['description']=req.param('d')
	report['query']=req.param('q')
	report.result={};
	console.log(report)
	reports.save(report,function(err,value){
		console.log(value);
	});

	res.redirect('/reports')

	} 

}

exports.report_save=function(req,res){


	var report={}
	report['datasource1']=req.query.ds1;
	report['datasource2']=req.query.ds2;
	report['description']=req.query.d;
	report['query']=req.query.q;
	report.result={};
	reports.save(report);

}

//app.get('/report/:_id/run',routes.report_run)

exports.report_run=function(req, res){


	
}


//app.get('/report/:_id/edit',routes.report_edit)

exports.report_edit=function(req, res){


	var id=req.params.id;

	
}

