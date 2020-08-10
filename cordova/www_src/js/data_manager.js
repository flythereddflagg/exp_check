export function get_now()
{
	const options = {year: 'numeric', month: '2-digit', day: '2-digit' };
	return new Date().toLocaleDateString('en-US', options);
}

export function print(...stuff){console.log(...stuff)};

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
	food_data += new_cells.join(',') + ";";
	write_data("food_data", food_data);
}
