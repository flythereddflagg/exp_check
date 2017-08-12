/**
The shell interface for our food editor
*/
package slave;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class ShInter 
{
    public void printf(String text)
    {
        // like the print function in python
        System.out.println(text);
    }
    
    public String input(String prompt)
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
    }
    
    public void clear()    
    {
        try {
            final String os = System.getProperty("os.name");
            
            if (os.contains("Windows")) {
                Runtime.getRuntime().exec("cls");
            }
            else {
                System.out.print("\033[H\033[2J");
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}

