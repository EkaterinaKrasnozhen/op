package lec5.ContactBook;

public class Presenter {

    View view;
    Model model;

    public Presenter(Model m, View v) {
        model = m;
        view = v;
    }

    public void buttonClick() {
        
        while (true) {
            int request = view.getValue(
                "Меню: 1 - Создать контакт, 2 -  Вывести список контактов, 3 - Найти контакт по ID, 4 - Удалить контакт, 5 - выход");
            userRequest(request);
        }
    }

    public void userRequest(int choice) {

        switch (choice) {
            case 1:
                Contact contact = view.getNewContact();
                model.addContact(contact);
                model.printConctactList();
                break;
            case 2:
                model.printConctactList();
                break;
            case 3:
                int findById = view.getValue("Введите ID для поиска: ");
                model.getContactById(findById);
                break;
            case 4:
                int deleteById = view.getValue("Введите ID для удаления: ");
                model.deleteById(deleteById);
                break;

            default:
                System.out.println("Bye");
                break;
        }

    }
}
