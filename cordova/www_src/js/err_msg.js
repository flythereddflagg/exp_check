import { print , write_data, read_data, save_new_row } from "./data_manager.js";

const index = "./index.html";

function goto_home_screen()
{
	window.location.assign(document.referrer); 
}


function add_screen_init()
{
	document.getElementById("okay button").onclick = goto_home_screen;
	const urlParams = new URLSearchParams(window.location.search);
	document.getElementById("err msg").innerHTML = urlParams.get('err_msg');;
	print(window.location);
}

add_screen_init();