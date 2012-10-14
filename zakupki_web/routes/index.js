
var Mongolian = require('mongolian');
var ObjectId = require("mongolian").ObjectId;

var server = new Mongolian("localhost:27017");
//var db = server.db("zakupki");
//var contracts = db.collection('contracts');
//var contractsprocedures = db.collection('contractsprocedures');
//var notifications = db.collection('notifications');
var db=null;



function get_collection(db_name){
	return server.db(db_name);
}

function set_database(db_name,callback){
	 db=server.db(db_name);
}

/*
 * GET home page.
 */

exports.index = function(req, res){
  
  server.dbNames(function(err,db_names){

   console.log(err,db_names)

   res.render('index',{title:'Current databases:',names:db_names})
   ;});
 // res.render('index', { title: 'Express' });
};

exports.database = function(req,res){
	
	var db_name = req.params.database;
    console.log('Get DB: ' + db_name);
    //var db=server.db(db_name);
    server.db(req.params.database).collectionNames(function(err,coll_names){
    console.log(coll_names);
    res.render('index',{title:'Current collections:',names:coll_names});
    })
    
};


exports.collection = function(req, res){
  
  var db =  req.params.database;
  var collection =  req.params.collection;

  server.db(req.params.database).collection(req.params.collection).find({},{"_id":1}).limit(100).toArray(function (err,names)
  {
    console.log(names);
    res.render('collections',{title:'Collection '+collection+':',names:names,db:db,coll:collection});
  })
  
};

exports.collection_by_field = function(req, res){
  
  var db =  req.params.database;
  var collection =  req.params.collection;
  var field =  req.params.field;
  var value =  req.params.val;
  var query = {};
  query[field]= value;
  server.db(db).collection(collection).find(query,{"_id":1,field:1}).limit(100).toArray(function (err,names)
  {
    
    console.log(db+collection+field+value);
    console.log(query);
    console.log(names);
    res.render('collections',{title:'Collection :',names:names,db:db,coll:collection});
  })
  
};

exports.item = function(req, res){
  
  var database = req.params.database;
  var collection =  req.params.collection;
  var id = new ObjectId(req.params._id);
  server.db(database).collection(collection).find({ _id : id }).toArray(function (err,items)
  {
  	//console.log(ObjectID(id));
    console.log(items);
    res.render('item',{title:'Item : '+collection+':',items:items,db:database,coll:collection});
  })
  
};


