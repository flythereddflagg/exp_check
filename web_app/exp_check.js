
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

function get_food()
{
    var food_list = document.getElementById("food_list")
    
}

function readTextFile(file)
{
/**
* Pulled this function from stack overflow I don't really know 
* if it works
*/
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    rawFile.send(null);
}

