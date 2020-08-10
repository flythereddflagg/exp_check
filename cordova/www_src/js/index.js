import {print, write_data, read_data, delete_row, error_msg} from "./tools_consts.js";

// always name, date_added, exp_date
var table = document.getElementById("food data");

function clear_data()
{
	var yesno = confirm("Are you sure you want to clear all of your data?");
	if (!yesno) return;
	// localStorage.clear();
	write_data("food_data", "");
	init_data();
	load_data();
}

function select_row(row)
{
	for (var row_ of table.rows){
		if (row_.className == "selected") row_.className = "";
	}
	row.className = "selected";
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

function add_row_to_table(name, added, exp)
{
	var new_cells = [name, added, exp];
	var row = table.insertRow(-1);
	row.onclick = function () {select_row(row)};
	for (var value of new_cells){
		var cell = row.insertCell(-1);
		cell.innerHTML = value
	}
}

function load_data()
{
	var search_str = document.getElementById("search bar").value;
	table.innerHTML = "";
	var data_str = read_data("food_data");
	var rows = data_str.split(";");
	for (var row of rows){
		if (search_str && !row.includes(search_str)) continue;
		if (!row) continue;
		var cells = row.split(',');
		add_row_to_table(...cells);
	}
	// print(localStorage);
}

function search_for()
{
	print("Searching...");
	load_data();
}

function delete_food()
{
	var i = 0;
	for (i = 0; i < table.rows.length; i++){
		var row = table.rows[i];
		if (row.className == "selected"){
			var del_row = [];
			for(var cell of row.cells){
				del_row.push(cell.innerHTML);
			}
			delete_row(del_row.join(','));
			break;
		}
	}
	if (i == table.rows.length) error_msg("No food selected for deletion.")
	load_data();
}

function sort_by()
{
	var sorter_val = document.getElementById("sorter").value;
	var data = read_data("food_data").split(';');
	var out_str = ""
	if (sorter_val == "food name"){
		out_str = data.sort().join(";");
	}
	else if (sorter_val == "add date"){
		out_str = data.sort(function(a, b) {
			var date_a = new Date(a.split(',')[1]);
			var date_b = new Date(b.split(',')[1]);
			return date_a - date_b;
		}).join(";");
	}
	else if (sorter_val == "exp date"){
		out_str = data.sort(function(a, b) {
			var date_a = new Date(a.split(',')[2]);
			var date_b = new Date(b.split(',')[2]);
			return date_a - date_b;
		}).join(";");
	}
	else{
		error_msg("Unrecognized list value.");
		return;
	} 
	write_data("food_data", out_str);
	load_data();
}


function init()
{
	document.getElementById("clear data button").onclick = clear_data;
	document.getElementById("add food button").onclick = goto_add_screen;
	document.getElementById("delete food button").onclick = delete_food;
	document.getElementById("sorter").onchange = sort_by;
	document.getElementById("search bar").oninput = search_for;

	init_data();
	load_data();
}

init();

