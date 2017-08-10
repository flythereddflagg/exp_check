// Code for food editor

class Food {
    constructor(year, month, day, fname)
    {
        this.year  = year;
        this.month = month;
        this.day   = day;
        this.fname = fname;
    }
    
    to_string()
    {
        outstring =
            this.month +
            "/"        +
            this.day   +
            "/"        +
            this.year  +
            " - "      +
            this.fname;
    }
}

function load_food()
{
    var food_list = document.getElementById("food_list");
    //document.write("This is a test");
    //console.log(food_list);
    var foods = [
        "17/12/23 - Beans",
        "17/12/23 - Corn",
        "17/12/23 - Chocolate",
        "17/12/23 - Cheese",
        "17/12/23 - Pickles"];

    for(var i = 0; i < foods.length; i++) {
        var opt = foods[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        food_list.appendChild(el);
    }
}


