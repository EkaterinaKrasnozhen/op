package seminar3;

public class Main {
    public static void main(String[] args) {
        Groups group = new Groups();
        Service service = new Service(group);
        service.createStudent("Катя");
        service.createStudent("Паша");
        service.createStudent("Вася");
        
        for (Students student : group) { //вывели список
            System.out.println(student);
        }

        service.sortbyName();;
        System.out.println();

        for (Students student : group) {//вывели отсортированный список по имени алфавит
            System.out.println(student);
        }

        service.sortById();;
        System.out.println();

        for (Students student : group) {//вывели отсортированный список по id
            System.out.println(student);
        }
    }
}
