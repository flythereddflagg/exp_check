/**
The list manager for our food editor
*/
package slave;

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class LsMan 
{
    private static String filename;
    
    public LsMan(String filenamep) 
    {
        filename = filenamep;
    }
    
    public void do_something()
    {
        System.out.println("Did it.");
    }
    public void read_file(){
        BufferedReader br = null;
	    FileReader fr = null;

	    try {

		    //br = new BufferedReader(new FileReader(FILENAME));
		    fr = new FileReader(filename);
		    br = new BufferedReader(fr);

		    String sCurrentLine;

		    while ((sCurrentLine = br.readLine()) != null) {
			    System.out.println(sCurrentLine);
		    }

	    } catch (IOException e) {

		    e.printStackTrace();

	    } finally {

		    try {

			    if (br != null)
				    br.close();

			    if (fr != null)
				    fr.close();

		    } catch (IOException ex) {

			    ex.printStackTrace();

		    }

	    }

    }
    
    public static void append_to_file(String data)
    {
        FileWriter     fw = null;
        BufferedWriter bw = null; // set to null initially
        
        
        try {
            File file = new File(filename);
            
            if (!file.exists()) {
                file.createNewFile();
            }
            
            fw = new FileWriter(file.getAbsoluteFile(), true);
            bw = new BufferedWriter(fw);
            
            bw.write(data);
            System.out.println("Done.");
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            try{
                if (bw != null) bw.close();
                if (fw != null) fw.close();
            }
            catch (IOException ex) {
            ex.printStackTrace();
            }
        }
    }
}

