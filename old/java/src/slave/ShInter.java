/**
The shell interface for our food editor
*/
package slave;

//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;
import java.util.Scanner;

public class ShInter 
{
    public void printf(String text)
    {
        // like the print function in python
        System.out.println(text);
    }
    
    /*public String input(String prompt)
    {
        String s;
        System.out.print(prompt);
        try {
            BufferedReader br = 
                new BufferedReader(
                new InputStreamReader(
                System.in));
             s = br.readLine();
        }
        catch (IOException e){
            s = "<ERR>";
            e.printStackTrace();
        }
        return s;
    }*/
    
    public String input(String prompt)
    {
        String s;
        System.out.print(prompt);

        Scanner sc = new Scanner(System.in);
        s = sc.nextLine();

        return s;
    }
    
    public void clear()    
    {
        try {
            System.out.print("\033[H\033[2J");
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}

