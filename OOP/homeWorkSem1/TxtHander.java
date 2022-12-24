package homeWorkSem1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.io.Serializable;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import homeWorkSem1.Human;

public class TxtHander implements Writeble {

    @Override
    public void save(Serializable serializable) {
        try (FileWriter fw = new FileWriter("FamilyTree.txt", true)) { 
            fw.write(serializable.toString());
        }catch (IOException e) {
            System.out.println(e.getMessage());
        }
        
    }

    // public String read() throws IOException {
    //     String treeArray = "";
    //     BufferedReader reader = new BufferedReader(new FileReader("FamilyTree.txt"));
    //     String line = reader.readLine();
    //     while (line != null) {
    //         treeArray += line;
    //         line = reader.readLine();
    //     }
    //     reader.close();
    //     return treeArray;

    // }

    /**метод read из файла с получением списка FamilyTree(human)*/
    public FamilyTree read() throws IOException {
        String treeArray = "";
        String [] result;
        BufferedReader reader = new BufferedReader(new FileReader("FamilyTree.txt"));
        String line = reader.readLine();
        while (line != null) {
            treeArray += line;
            line = reader.readLine();
        }
        reader.close();
        result = treeArray.replace(":", "").replace("[", "")
        .replace("]", "").replace(",", "").split(" ");
        boolean gender;
        FamilyTree tree = new FamilyTree();
        for (int index = 1; index < result.length-2;) {
        //не придумала как обработать male/female из файла, чтобы вставить boolean в new Human();   
            Human human = new Human(result[index], Integer.parseInt(result[index+2]), true, null, null);
            tree.add(human);
            index +=6;    
        }
        return tree;                
    } 
}
