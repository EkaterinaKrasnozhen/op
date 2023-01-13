package lec5.ContactBook;

import java.util.Scanner;

public class ModelSwitch {

    Scanner in = new Scanner(System.in);
    Model m = new Model();
    
    public void userRequest(int choice) {
        switch (choice) {
            case 1:
                m.addContact(null);
                break;
        
            default:
                break;
        }
    }
}
