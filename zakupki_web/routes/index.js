
var server = require('../model/database.js').server;
var ObjectId = require('../model/database.js').ObjectId;
//var ObjectId = require("mongolian").ObjectId;


var Sequence = require("futures").sequence;

var db_name = 'zakupki';
var database = server.db(db_name);


exports.index = function(req, res){
  
  server.dbNames(function(err,db_names){

  console.log(err,db_names)

   res.render('index',{title:'Current databases:',names:db_names})
   ;});
 // res.render('index', { title: 'Express' });
};

exports.database = function(req,res){
	
	//var db_name = req.params.database;
    //console.log('Get DB: ' + db_name);
    //var db=server.db(db_name);
    database.collectionNames(function(err,coll_names){
    console.log(coll_names);
    res.render('index',{title:'Current collections:',names:coll_names});
    })
    
};


exports.collection = function(req, res){
  
  var collection =  req.params.collection;

  database.collection(req.params.collection).find({},{"_id":1}).
  limit(1000).toArray(function (err,names)
  {
    console.log(names);
    res.render('collections',{err:err,title:'Collection '+collection+':',names:names,coll:collection});
  })
  
};

exports.collection_by_field = function(req, res){
  
  var collection =  req.params.collection;
  var pk_field =  req.params.pk_field;
  var pk_value =  req.params.val;
  var query = {};
  var fields = {};

  query[pk_field]= pk_value;

  fields["_id"]=1
  fields[pk_field]= 1;

  database.collection(collection).find(query,fields).limit(1000).toArray(function (err,names)
  {
    res.render('collections',{err:err,title:'Collection :',names:names,coll:collection});
  })
  
};

exports.collection_by_field_and_fields = function(req,res){

  var sequence = Sequence();
  var collection =  req.params.collection;
  console.log(req.query.q);
  console.log(req.query.f);
  var type=req.query.t;
  var query=JSON.parse(req.query.q);
  var fields=JSON.parse(req.query.f);
  console.log(query,fields);
  
sequence
.then(function(next){
  
  if (type=='json') fields['_id']=0
  next(query,fields);

 }).then(function(next,query,fields){

  console.log(query);
  console.log(fields);


  database.collection(collection).find(query,fields).toArray(function (err,items)
  {

  if (type=='json'){

      res.json(items)

  }else{
      console.log(items.length)
      res.render('collections_table',{err:err,title:'Search:'
        ,fields:fields,items:items,coll:collection,
        q:JSON.stringify(query),
        f:JSON.stringify(fields)
        }) 
    }
  })
  
  //res.end()
}) 
};


exports.item = function(req, res){
  var collection =  req.params.collection;
  var id = new ObjectId(req.params._id);
  console.log(id)
  database.collection(collection).find({ _id : id }).toArray(function (err,items)
  {
    console.log(items);
    res.render('item',{ err:err, title:collection,item:items,coll:collection});
  })
};

exports.search = function(req, res){
  var collection =  req.params.collection;
  var id = new ObjectId(req.params._id);
  console.log(id)
  database.collection(collection).find({ _id:id }).toArray(function (err,items)
  {
    //console.log(ObjectID(id));
    console.log(items);
    res.render('item',{ err:err, title:collection,item:items,coll:collection});
  })
  
};


