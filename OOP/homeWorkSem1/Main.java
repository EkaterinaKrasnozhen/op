package homeWorkSem1;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // Human human1 = new Human("Irina", 68, Gender.Female, null, null);
        // Human human2 = new Human("Leonid", 69, Gender.Male, null, null);
        // Human human3 = new Human("Liudmila", 62, Gender.Female, null, null);
        // Human human4 = new Human("Alexander", 65, Gender.Male,null, null);
        // Human human5 = new Human("Kate", 36, Gender.Female, human2, human1);
        // Human human6 = new Human("Pavel", 37, Gender.Male, human4, human3);
        // Human human7 = new Human("Yaroslav", 7, Gender.Male, human6, human5);
        // Human human8 = new Human("Sviatoslav", 3, Gender.Male, human6, human5);
        int index=0;
        FamilyTree tree = new FamilyTree();
        Human human1 = new Human("Irina", 68, Gender.Female, null, null, index++);
        Human human2 = new Human("Leonid", 69, Gender.Male, null, null, index++);
        System.out.println(human1);
        System.out.println(human2);

        tree.createHuman("Liudmila", 62, Gender.Female, null, null);
        tree.createHuman("Alexander", 65, Gender.Male,null, null);
        tree.createHuman("Kate", 36, Gender.Female, human2, human1);

        System.out.println(tree);
        


        

    }
}
