export function print(...stuff){console.log(...stuff)};

export function write_data(field, data)
{
	localStorage.setItem(field, data);
	localStorage.setItem("last_write", Date.now().toString());
}

export function read_data(field)
{
	var data = localStorage.getItem(field);
	localStorage.setItem("last_read", Date.now().toString());
	return data;
}

export function get_now()
{
	print(Date().toString());
}

export function save_new_row(name, added, exp)
{
	var new_cells = [name, added, exp];
	var food_data = read_data("food_data");
	food_data += new_cells.join(',') + ";";
	write_data("food_data", food_data);
}
