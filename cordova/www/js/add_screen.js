import {
	HOME_SCREEN, 
	save_new_row, 
	get_today, 
	error_msg
} from "./tools_consts.js";

function goto_home_screen()
{
	window.location.assign(HOME_SCREEN); 
}

function confirm_add_food()
{
	var name = document.getElementById("name").value;
	var date = document.getElementById("date").value;
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

function add_screen_init()
{
	const picker = datepicker(document.getElementById("date"), {
		formatter: (input, date, instance) => {
			const value = date.toLocaleDateString()
			input.value = value
	}});
	document.getElementById("confirm button").onclick = confirm_add_food;
	document.getElementById("cancel add button").onclick = goto_home_screen;
	document.getElementById("name").focus();
	/* console.log(localStorage); */
}

add_screen_init();
