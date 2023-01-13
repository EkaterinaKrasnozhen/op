package lec5.ContactBook;

import java.util.ArrayList;
import java.util.List;

public class Model {
    

    private List<Contact> contacts = new ArrayList<>();
    public void addContact(Contact contact) {
        contacts.add(contact);
    }

    public void printConctactList() {
        for (Contact contact : contacts) {
            System.out.println(contact);
        }
    }



    public void getContactById(int id) {    
        for (Contact contact : contacts) {
            if (contact.getId() == id) {
                System.out.println(contact);
            }
        }
    }


    public void deleteById(int id) {
        for (Contact contact : contacts) {
            if (contact.getId() == id) {
                contacts.remove(contact);
            }
        }
        System.out.printf("Контакт с ID: %d удален", id);
    }


    public void refreshPhone(int id, String newPhone) {
        for (Contact contact : contacts) {
            if (contact.getId() == id) {
                contact.setPhone(newPhone);
            }
        }
        System.out.printf("Телефона у контакта с iD: %d обновлен", id);
    }

}
