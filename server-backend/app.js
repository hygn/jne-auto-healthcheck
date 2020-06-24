var http = require('http');
var url = require('url');

http.createServer(function (req, res) {
    var urlpart = url.parse(req.url,true);
    console.log(url.parse(req.url).pathname.split('/').join(''));
    if(url.parse(req.url).pathname.split('/').join('') == 'req'){
        try {
            queryparts = urlpart.query;
            console.log(queryparts);
        }
        catch{
            
        }
    }
    res.end();
}).listen(8080);