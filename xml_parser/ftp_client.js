var Ftp = require("jsftp"),
	events = require('events'),
	Mongolian = require("mongolian");

var ftp = new Ftp({
    host: "ftp.zakupki.gov.ru",
    user: "free",
    port: 21, // Defaults to 21
    pass: "free"
});


var server = new Mongolian("localhost:27017");
var db_zkupki = server.db("zakupki");


var zip_files = db.collection('zip_files');
zip_files.ensureIndex({"url":1},{unique:true});

function removetrash(dir,line)
{

	line = dir+line;
	return line.replace(/\r\n/g,"")
}




var spider = new events.EventEmitter();
var file_list= new Array();
//var zip_files=new Array();

spider.on('listDir',function(dir){
	console.log("Reading dir:"+dir)
	ftp.list(dir, function(err, data) {
    if (err)
        return console.error(err);  
	console.log(data+"");
	str=data+""
	re = /[\w-\.]+\r\n/g
	found = str.match(re)
	if(found != null){
	found = found.map(function (line){ return removetrash(dir,line)})
	file_list.push.apply(file_list,found)
	}
	setTimeout(function(){spider.emit('nextStep')},100);

	})
})


spider.on('nextStep',function(){
				console.log(file_list);
	            var file=file_list.pop()    

	            if(file.match(/.zip/)){
	            	//zip_files.push(file);

	            	var element= {
	            		url:file
	            	}

	            	zip_files.insert(element)

	            	spider.emit('nextStep');
	            } else {
		        console.log(file)
                setTimeout(function(){spider.emit('listDir',file+'/')},100)
            	}

})


spider.emit('listDir',"");//Banzay!!