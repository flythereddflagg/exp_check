import { print , write_data, read_data, save_new_row , get_now} from "./data_manager.js";

const index = "./index.html";

function goto_home_screen()
{
	window.location.assign(index); 
}

function confirm_add_food()
{
	save_new_row(
		document.getElementById("name").value,
		get_now(),
		document.getElementById("date").value
	);
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
	console.log(localStorage);
	get_now()
}

add_screen_init();
