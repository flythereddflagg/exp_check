import {
	HOME_SCREEN, 
	save_new_row, 
	get_today, 
	error_msg,
	debug
} from "./tools_consts.js";

function goto_home_screen()
{
	window.location.assign(HOME_SCREEN); 
}

function confirm_add_food()
{
	var day = document.getElementById("day_select").value;
	var month = document.getElementById("month_select").value;
	var year = document.getElementById("year_select").value;
	var name = document.getElementById("name").value;
	var date = `${month.padStart(2, '0')}/${day.padStart(2, '0')}/${year}`
	if (!name || !date){
		error_msg("You must specify a name and a date.");
		return;
	}
	if (name.includes(",") || name.includes(";")){
		error_msg("Names may not contain ',' or ';'.");
		return;		
	}
	save_new_row(name, get_today(), date);
	goto_home_screen();
}

function update_calandar()
{
	var day = document.getElementById("day_select");
	var month = document.getElementById("month_select");
	var year = document.getElementById("year_select");
	var cur_year = year.value;
	var cur_month = month.value;
	day.innerHTML = "";
	var n_days = new Date(cur_year, cur_month, 0).getDate();
		for (var i = 0; i < n_days; i++){
		var opt = document.createElement("option");
		opt.value = 1 + i;
		opt.text = 1 + i;
		day.add(opt);
	}
}

function init_dates()
{
	var today = new Date();
	var month = document.getElementById("month_select");
	var year = document.getElementById("year_select");
	
	month.onchange = update_calandar;
	year.onchange = update_calandar;

	var start_year = today.getFullYear();
	for (var i = 0; i < 30; i++){
		var opt = document.createElement("option");
		opt.value = start_year + i;
		opt.text = start_year + i;
		year.add(opt);
	}
	for (var i = 0; i < 12; i++){
		var opt = document.createElement("option");
		opt.value = 1 + i;
		opt.text = 1 + i;
		month.add(opt);
	}
	update_calandar();
}

function add_screen_init()
{
	document.getElementById("confirm button").onclick = confirm_add_food;
	document.getElementById("cancel add button").onclick = goto_home_screen;
	document.getElementById("name").focus();
	/* console.log(localStorage); */
	
	init_dates();
}

add_screen_init();
