import {
	debug, 
	write_data, 
	read_data, 
	delete_row, 
	error_msg
} from "./tools_consts.js";

// always: name, date_added, exp_date
var table = document.getElementById("food_data");

function clear_data()
{
	var yesno = confirm(
		"Are you sure you want to clear all of your data?"
	);
	if (!yesno) return;
	// localStorage.clear();
	write_data("food_data", "");
	init_data();
	load_data();
}

function select_row(row)
{
	var select_it = row.className == "selected" ? false : true;
	for (var row_ of table.rows){
		if (row_.className == "selected") row_.className = "";
	}
	if (select_it){
		row.className = "selected";
	}
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
	var search_str = document.getElementById("search_bar").value;
	table.innerHTML = "";
	var data_str = read_data("food_data");
	var rows = data_str.split(";");
	var rows = data_str.split(";");
	for (var row of rows){
		if (search_str && !row.includes(search_str)) continue;
		if (!row) continue;
		var cells = row.split(',');
		add_row_to_table(...cells);
	}
	// debug(localStorage);
}

function search_for()
{
	debug("Searching...");
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

function toggle_show_menu()
{
	document.getElementById("myDropdown").classList.toggle("show");
}

function unshow_menu(event) 
{
	// Close the dropdown menu if the user clicks outside of it
	if (!event.target.matches('.dropbtn')) {
		var dropdowns = document.getElementsByClassName("dropdown-content");
		var i;
		for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
				openDropdown.classList.remove('show');
			}
		}
	}
}

function check_dates()
{
	debug("Checking dates...");
	
	var message = "The following foods will expire soon:\n";
	
	var today = new Date();
	var exp_list = [];
	for (var datum of read_data("food_data").split(';')){
		var food = datum.split(',')
		var comp_date = new Date(food[2]);
		var diff = Math.ceil((comp_date - today)/86400000);
		if (diff <= 30){
			exp_list.push([food[0], diff])
		}
	}
	
	if (!(exp_list.length)) return;
	
	exp_list.sort(function(a, b){return a[1] - b[1];});
	for (var row of exp_list){
		message += `${row[0].padStart(20, ' ')} expires in ${new String(row[1]).padStart(5, ' ')} days.`;
		if (row[1] <= 0) message += " (Expired)";
		message += "\n";
	}
	navigator.notification.alert(
		message, 
		function () {}, 
		"Exp Check - Date Checker", 
	)
}

function onDeviceReady() 
{
	document.getElementById("m_check_dates").onclick = check_dates;
	var BackgroundFetch = window.BackgroundFetch;

	// Your background-fetch handler.
	var fetchCallback = function(taskId) {
		console.log('[js] BackgroundFetch event received: ', taskId);
		check_dates();
		// Required: Signal completion of your task to native code
		// If you fail to do this, the OS can terminate your app
		// or assign battery-blame for consuming too much background-time
		BackgroundFetch.finish(taskId);
	};

	var failureCallback = function(error) {
		console.log('[bg] - BackgroundFetch failed', error);
	};

	BackgroundFetch.configure(fetchCallback, failureCallback, {
		minimumFetchInterval: 86400, // <-- default is 15
		periodic: true,
		stopOnTerminate: false,
		startOnBoot: true,
		requiresBatteryNotLow: true
	});
	debug("Device Ready");
}

function init()
{
	// setup all the UI behavior
	document.getElementById("clear_data_button").onclick = clear_data;
	document.getElementById("add_food_button").onclick = goto_add_screen;
	document.getElementById("delete_food_button").onclick = delete_food;
	document.getElementById("menu").onclick = toggle_show_menu;
	document.getElementById("m_add_food").onclick = goto_add_screen;
	document.getElementById("m_delete_food").onclick = delete_food;
	document.getElementById("m_clear_data").onclick = clear_data;
	document.getElementById("sorter").onchange = sort_by;
	document.getElementById("search_bar").oninput = search_for;
	window.onclick = unshow_menu;
	
	// init and load data
	init_data();
	load_data();
	
	// load stuff needed for system (app external) actions
	document.addEventListener("deviceready", onDeviceReady, false);
}

init();
