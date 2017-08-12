/**
The engine for our food editor
*/
package slave;

import java.util.ArrayList;
import java.util.List;

public class Engine 
{
    private ShInter shi;
    private LsMan manager;
        private static List<String[]> food_data = new ArrayList<String[]>();
    private String msg;
    private String menu_list = "\n" +
        "Options:\n" +
        "  1 - Add Food\n" +
        "  2 - Delete Food\n" +
        "  3 - Refresh List\n" +
        "  0 - Quit Program\n";

    public Engine(ShInter shia, LsMan managera)
    {
        shi = shia;
        manager = managera;
    }
    
    public char menu()
    {   
        char choice;
        shi.printf(menu_list);
        String inp = shi.input("--> ");
        choice = (inp.length() > 0) ? inp.charAt(0) : '\0';
        return choice;
    }
    
    public void add_food()
    {
        shi.printf("Name for new food:");
        String name  = shi.input("  Name  > ");
        shi.printf("Expiration Date for new food:");
        String year  = shi.input("  Year  > ");
        String month = shi.input("  Month > ");
        String day   = shi.input("  Day   > ");
        
        int year2  = Integer.parseInt(year);
        int month2 = Integer.parseInt(month);
        int day2   = Integer.parseInt(day);
        if (day2 > 31   ||
            day2 < 1    ||
            month2 > 12 ||
            month2 < 1   ) 
        {   
            msg = "Error: Impossible date.";
            return;
        }
        year = String.format("%d", year2%2000);
        
        String new_entry = year + 
            ","   +
            month +
            ","   +
            day   +
            ","   +
            name  +
            "\n";
        manager.append_to_file(new_entry);
    }
    
    public void delete_food(){
        shi.printf("Select food for deletion:");
        String id = shi.input("  id > ");
        int idn = Integer.parseInt(id);
        // figure out how to delete!!!
    }
    
    public String get_food_list()
    {
        food_data = manager.get_data();
        String out = " _____________________________\n" +
        "  id - Exp Date - Name" +
        "\n _____________________________\n";
        String day;
        String month;
        String year;
        int index = 0;

        for(String[] row:food_data) {
            day = String.format("%02d", Integer.parseInt(row[2]));
            month = String.format("%02d", Integer.parseInt(row[1]));
            year = String.format("%02d", Integer.parseInt(row[0]));
            // format to mm/dd/yy
            out += "  " +
                String.format("%02d", index) +
                " - "  +
                month  + // month
                "/"    +
                day    + // day
                "/"    +
                year   + // year
                " - "  +
                row[3] + // name
                "\n";
                index ++;
        }
        out += " ____________________________";
        return out;
    }
    
    public void run()
    {
        shi.clear();
        int exit_it = 0;
        char choice;
        msg = "";
        while (exit_it == 0) {
            shi.printf(get_food_list());
            if (msg != "") {
                System.out.print("\nExp Check: ");
                shi.printf(msg);
                msg = "";
            }
            choice = menu();
            switch(choice){
                case '1':
                    add_food();
                    break;
                case '2':
                    delete_food();
                    break;
                case '3':
                    break;
                case '0':
                    exit_it = 1;
                    break;
                default:
                    msg = "That's not an option";
                    break;
            }
            shi.clear();
        }
        
    }    
}
