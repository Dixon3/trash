
var fs = require('fs'),
    events = require('events'),
    xml2js = require('xml2js'),
    Mongolian = require("mongolian"),
    Ftp = require("jsftp"),
    zlib = require('zlib'),
    AdmZip = require('adm-zip');



var ftp = new Ftp({
    host: "ftp.zakupki.gov.ru",
    user: "free",
    port: 21, // Defaults to 21
    pass: "free"
});


var workers=0;
var max_workers=1;

var parser = new xml2js.Parser({explicitRoot:true,trim:true,explicitArray:false});
var spider = new events.EventEmitter();

var zip_regex=process.argv[2];

var path='';
var xml_list=[];
var number_files=0;
var stored_items=0;
var parsed_items=0;

var server = new Mongolian("localhost:27017");
var db_zakupki = server.db("zakupki");

var db = server.db("zakupki");

var contracts = db.collection('contracts');
contracts.ensureIndex({"oos:regNum":1,"oos:versionNumber":1},{unique:true});

var contractsprocedures = db.collection('contractsprocedures');
contractsprocedures.ensureIndex({"oos:regNum":1,"oos:id":1},{unique:true});

var notifications = db.collection('notifications');
notifications.ensureIndex({"oos:notificationNumber":1,"oos:versionNumber":1},{unique:true});

var protocols = db.collection('protocols');
protocols.ensureIndex({"oos:notificationNumber":1,"oos:versionNumber":1},{unique:true});

var zip_files = db_zakupki.collection('zip_files');


on_end = function(a,b)
{
//workers--;
stored_items++;
//spider.emit('walk');


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

	ftp.get(filename, function(err, data) {
    if (err)
        return console.error(err);


    var zip = new AdmZip(data);
    var zipEntries = zip.getEntries();
//    console.log(zipEntries.length);

    for (var i = 0; i < zipEntries.length; i++){
        var unziped_data= zip.readAsText(zipEntries[i])   
        //console.log(unziped_data)
        parser.parseString(unziped_data, function (err, result) {
			console.dir(result);
			spider.emit('storeData',result['export']);
        //	console.log('Done, still in pool:'+number_files);
    	})
	}
	});

	//fs.readFile(path+'/'+filename, function(err, data) {
    //		parser.parseString(data, function (err, result) {
		//console.dir(result);
	//	spider.emit('storeData',result['export']);
        	//console.log('Done, still in pool:'+number_files);
	//    });
	//});
});


spider.on('walk',function(){


	 zip_files.findOne( { "url":new RegExp(zip_regex),"parsed":false},function(err,file){

	 	console.log(file)
	 	//db_name=file.url.split('/')[0]
	 	
	 	file.parsed=true; 
		spider.emit('loadFile',file.url)
	 	zip_files.save(file,function(){setTimeout(function(){spider.emit('walk')},1000);});
	 })

//	console.log(xml_list.length);
/*
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
*/
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


spider.emit('walk')
//var xml_list=fs.readdirSync('.');
//console.log(xml_list);
//path=process.argv[2];
//spider.emit('loadFile','Zabajkalskij_kraj_Aginskij_Burjatskij_okrug/protocols/protocol_Zabajkalskij_kraj_Aginskij_Burjatskij_okrug_inc_20121001_000000_20121101_000000_973.xml.zip');//Banzay!!
