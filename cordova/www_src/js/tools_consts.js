// non exports
function get_now()
{
	return Date().toString()
}

// consts
export const HOME_SCREEN = "./index.html";
const SUPPRESS_OUTPUT = true;


export function get_today()
{
	const options = {year: 'numeric', month: '2-digit', day: '2-digit' };
	return new Date().toLocaleDateString('en-US', options);
}

export function print(...stuff)
{
	if (!SUPPRESS_OUTPUT) console.log("[APP]", ...stuff)
};

export function write_data(field, data)
{
	localStorage.setItem(field, data);
	localStorage.setItem("last_write", get_now());
}

export function read_data(field)
{
	var data = localStorage.getItem(field);
	localStorage.setItem("last_read", get_now());
	return data;
}


export function save_new_row(name, added, exp)
{
	var new_cells = [name, added, exp];
	var food_data = read_data("food_data");
	if (food_data) food_data += ";";
	food_data +=  new_cells.join(',');
	write_data("food_data", food_data);
}


export function delete_row(del_row_str)
{
	var food_data = read_data("food_data");
	var to_write = [];
	for(var row of food_data.split(";")){
		print(row, del_row_str, ";")
		if (row == del_row_str) {
			print("Deleting row", row)
			continue;
		}
		to_write.push(row);
	}
	food_data = to_write.join(';')
	write_data("food_data", food_data);
}


export function error_msg(err_msg="")
{
	// Get the snackbar DIV
	var msg = document.getElementById("toast");
	msg.innerHTML = "Error: " + err_msg;
	// Add the "show" class to DIV
	msg.className = "show";

	// After 3 seconds, remove the show class from DIV
	setTimeout(function(){
			msg.className = msg.className.replace("show", ""); 
		}, 
		3000
	);
}
