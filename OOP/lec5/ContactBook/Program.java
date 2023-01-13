package lec5.ContactBook;

public class Program {
    public static void main(String[] args) {
        // Presenter p = new Presenter(new Model(), new View());
        // p.buttonClick();
        int index=0;
        Contact contact = new Contact(index++, "Катя", "Красножен", "892");
        Contact contact2 = new Contact(index++, "Вася", "Кран", "893");
        int findId = contact.getId();
        System.out.println(findId);
        Model m  = new Model();
        m.addContact(contact);
        m.addContact(contact2);
        m.printConctactList();
        m.deleteById(findId);
        m.printConctactList();
    
    }
}
