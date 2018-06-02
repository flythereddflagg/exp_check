
function open_it()
{
    open('./home_screen.html', '_blank');
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

    var file = new File(file1);

    file.open("r"); // open file with read access
    var str = "";
    while (!file.eof) {
        // read each line of text
        str += file.readln() + "\n";
    }
    file.close();
    alert(str);

}

