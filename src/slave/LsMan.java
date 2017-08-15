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

import java.util.ArrayList;
import java.util.List;

public class LsMan 
{
    private static String filename;
    private static List<String[]> data = new ArrayList<String[]>();
    
    public LsMan(String filenamep) 
    {
        filename = filenamep;
    }
    
    public List<String[]>  get_data()
    {
        String filestring = read_file();
        if (filestring == "< EMPTY >") {
            String[] arr = {filestring};
            data.add(arr);
            return data;
        }
        parse_csv(filestring);
        return data; 
    }
    
    public void delete_item(int index)
    {
        data.remove(index);
        write_to_csv();
    }
    
    public void write_to_csv()
    {
        String filestring = "";
        for (String[] row:data) {
            for (String el:row) {
                filestring += el + ",";
            }
            filestring += "\n";
        }

        try {
            File file = new File(filename);
            FileWriter fw = new FileWriter(file, false);
            file.createNewFile();
            fw.write(filestring);
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }           
    }
    
    public void parse_csv(String filestring)
    {
        // file format
        // YY, MM, DD, Food_name
        //System.out.println(filestring);
        data = new ArrayList<String[]>();
        String[] lines = filestring.split("\n");
        String[] splitline;
        for (String line:lines) {
            splitline = line.split(",");
            if (splitline.length != 4) continue;
            data.add(splitline);
        }
    }
    
    public String read_file(){
        BufferedReader br = null;
	    FileReader fr = null;
        String f_string = "\n";
        
	    try {
            File file = new File(filename);
            
            if (!file.exists()) {
                file.createNewFile();
                return "< EMPTY >";
            }
	    
		    fr = new FileReader(filename);
		    br = new BufferedReader(fr);

		    String sCurrentLine;

		    while ((sCurrentLine = br.readLine()) != null) {
			    f_string += sCurrentLine;
			    f_string += "\n";
		    }
	    } 
	    catch (IOException e) {
		    e.printStackTrace();
	    } 
	    finally {
		    try {
			    if (br != null) br.close();
			    if (fr != null) fr.close();
		    } catch (IOException ex) {
			    ex.printStackTrace();
		    }
	    }
	    
	    return f_string;
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
            //System.out.println("Done.");
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

