
var fs = require('fs'),
    events = require('events'),
    xml2js = require('xml2js'),
    Mongolian = require("mongolian");



var workers=0;
var max_workers=1;

var parser = new xml2js.Parser({explicitRoot:true,trim:true,explicitArray:false});
var spider = new events.EventEmitter();


var path='';
var xml_list=[];
var number_files=0;
var stored_items=0;
var parsed_items=0;

var server = new Mongolian("localhost:27017");
var db = server.db("zakupki");

var contracts = db.collection('contracts');
contracts.ensureIndex({"oos:regNum":1,"oos:versionNumber":1},{unique:1});

var contractsprocedures = db.collection('contractsprocedures');
contractsprocedures.ensureIndex({"oos:regNum":1,"oos:id":1},{unique:1});

var notifications = db.collection('notifications');
notifications.ensureIndex({"oos:notificationNumber":1,"oos:versionNumber":1},{unique:true});

var protocols = db.collection('protocols');
protocols.ensureIndex({"oos:notificationNumber":1,"oos:versionNumber":1},{unique:true});


on_end = function(a,b)
{
//workers--;
stored_items++;
spider.emit('walk');
}

spider.on('storeData',function(data){

	if (data["contract"]){
		for (var i = 0; i < data["contract"].length; i++) {
  		e = data["contract"][i];
		//console.log("contracti Added")
        parsed_items++;
		contracts.insert(e,on_end);
		}
	}
	if (data["contractProcedure"]){
		var arr=data["contractProcedure"];
		for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                contractsprocedures.insert(e,on_end);
                }
	}

	if (data["notificationZK"]){
                var arr=data["notificationZK"];
                for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                notifications.insert(e,on_end);
                }

        }
	if (data["notificationEF"]){
                var arr=data["notificationEF"];
                for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                notifications.insert(e,on_end);
                }
        }
     if (data["notificationoOK"]){
                var arr=data["notificationOK"];
                for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                notifications.insert(e,on_end);
                }
        }

     if (data["notificationCancel"]){
                var arr=data["notificationCancel"];
                for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                notifications.insert(e,on_end);
                }
        }

Object.keys(data).forEach(function(key){

    if (key.match(/^protocol/)){
    console.log(key)
                var arr=data[key];
                for (var i = 0; i < arr.length; i++) {
                e = arr[i];
                parsed_items++;
                protocols.insert(e,on_end);


}}
}
);

number_files--;
workers--;
//spider.emit('walk');
});

function end_items()
{
    number_items--;
}


spider.on('loadFile',function(filename){

	fs.readFile(path+'/'+filename, function(err, data) {
    		parser.parseString(data, function (err, result) {
		//console.dir(result);
		spider.emit('storeData',result['export']);
        	//console.log('Done, still in pool:'+number_files);
	    });
	});
});


spider.on('loadDir',function(_dir){
	xml_list=fs.readdirSync(_dir);
    number_files=xml_list.length;
	console.log('We found:'+xml_list);
	spider.emit('walk');
    setTimeout(show_stats,3000);
});


spider.on('walk',function(){
//	console.log(xml_list.length);
	if (xml_list.length>0){
        if ((workers<max_workers)&(parsed_items-stored_items)<100){
		        var file=xml_list.pop()
		        if(file.match(/\.xml$/g)){
		        console.log(file);
                workers++;
                setTimeout(function(){spider.emit('loadFile',file)},1000);
		        } else {
                console.log("Not xml file:"+file)
                setTimeout(function(){spider.emit('walk')},1000);
                }


                }else{
                
	            setTimeout(function(){spider.emit('walk')},1000);
                }
	}

});

function show_stats(){
console.log('We parse and store:'+parsed_items+'/'+stored_items);
console.log('Still in pool files:'+number_files);
console.log('Working workers:'+workers);
setTimeout(show_stats,3000);
if((parsed_items==stored_items)&(workers==0)&(number_files==0))
{
console.log('Seems import done');
process.exit(0);
}
}

//var xml_list=fs.readdirSync('.');
//console.log(xml_list);
path=process.argv[2];
spider.emit('loadDir',path);//Banzay!!
