import slave.*;


public class main {
    public static void main(String[] args)
    {
        ShInter shi = new ShInter();
        LsMan manager = new LsMan("food_list.txt");
        Engine eng = new Engine(shi, manager);
        eng.run();
    }
}

