var http = require('http')
var opn = require('opn');
var fs = require('fs');

function open_it()
{
    opn('./home_screen.html', '_blank');
}

function close_it()
{
    if (confirm("Close Window?")) {
        close();
    }
}

function generate_food_list()
{
    var food_list = document.getElementById("food_list");
    var data = readTextFile('data1.csv');
    add_options(food_list, data)
    
}

function add_options(list, data)
{
    for (var i = 0; i < data.length; i++){
        var opt = document.createElement('option');
        opt.value = data[i];
        opt.innerHTML = data[i];
        list.appendChild(opt);
    }
}

function readTextFile(file1)
{

    var file = new File([""], file1);

    file.open("r"); // open file with read access
    var str = "";
    while (!file.eof) {
        // read each line of text
        str += file.readln() + "\n";
    }
    file.close();
    alert(str);

}

function req_listen (request, response) 
{  
    var html = ""
    fs.read('./home_screen.html', html, callback = function (
        err, bytes_read, buffer){if (err) throw err;});
    response.writeHeader(200, {"Content-Type": "text/html"});  
    response.write(html);  
    response.end();
}

function setup_server()
{
    http.createServer(req_listen).listen(8000);
}


function main()
{
    setup_server();
    open_it();
    //generate_food_list();
}

main();