import slave.LsMan;

public class main {
    public static void main(String[] args)
    {
        LsMan manager = new LsMan("food_list.txt");
        manager.do_something();
        manager.append_to_file("Just a test...\n");
        manager.read_file(); // make it return a string
    }
}

