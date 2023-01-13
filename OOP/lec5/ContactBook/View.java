package lec5.ContactBook;

import java.util.Scanner;

public class View {
    
    int index;
    Scanner in = new Scanner(System.in);

    public int getValue(String title) {
        System.out.printf("%s", title);
        return in.nextInt();
    }

    public Contact getNewContact() {

        System.out.println("Введите Имя нового контакта");
        String name1 = in.next();
        System.out.println("Введите Фамилию нового контакта");
        String name2 = in.next();
        System.out.println("Введите телефон нового контакта");
        String phone = in.next();
        Contact contact = new Contact(index++, name1, name2, phone);
        System.out.println("Новый контакт добавлен");
        return contact;
    }
}
