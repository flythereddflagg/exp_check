import { print , write_data, read_data, save_new_row } from "./data_manager.js";

// always name, date_added, exp_date
var table = document.getElementById("food data");

function clear_data()
{
	confirm("Are you sure you want to clear all of your data?")
	// localStorage.clear();
	write_data("food_data", "");
	init_data();
	load_data();
}

function init_data(){
	if (read_data("food_data") == undefined){
		write_data("food_data", "");
	}
}

function goto_add_screen()
{
	window.location.assign("./add_screen.html"); 
}

function error_msg(err_msg)
{
	window.location.assign("./err_msg.html?err_msg=" + err_msg); 
}

function add_row_to_table(name, added, exp)
{
	var new_cells = [name, added, exp];
	var row = table.insertRow(-1);
	
	for (var value of new_cells){
		var cell = row.insertCell(-1);
		cell.innerHTML = value
	}
}

function load_data()
{
	table.innerHTML = "";
	var data_str = read_data("food_data");
	var rows = data_str.split(";");
	for (var row of rows){
		if (!row) continue;
		var cells = row.split(',');
		add_row_to_table(...cells);
	}
	print(localStorage);
}

function init()
{
/* 	document.getElementById("clear data button").onclick = function () {
		error_msg("Here is an error")
	}; */
	document.getElementById("clear data button").onclick = clear_data;
	document.getElementById("add food button").onclick = goto_add_screen;

	init_data();
	load_data();
}

init();

