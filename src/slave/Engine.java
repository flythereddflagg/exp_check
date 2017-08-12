/**
The engine for our food editor
*/
package slave;

public class Engine 
{
    private ShInter shi;
    private LsMan manager;
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
    
    public void add_food(){
        ;
    }
    
    public void delete_food(){
        ;
    }
    
    public void run()
    {
        shi.clear();
        int exit_it = 0;
        char choice;
        String msg = "";
        while (exit_it == 0) {
            shi.printf(manager.get_food_list());
            if (msg != "") {
                System.out.print("\nExp Check: ");
                shi.printf(msg);
                msg = "";
            }
            choice = menu();
            switch(choice){
                case '1':
                    add_food();
                    shi.clear();
                    break;
                case '2':
                    delete_food();
                    shi.clear();
                    break;
                case '3':
                    shi.clear();
                    break;
                case '0':
                    exit_it = 1;
                    break;
                default:
                    msg = "That's not an option";
                    shi.clear();
                    break;
            }
        }
        shi.clear();
    }    
}
