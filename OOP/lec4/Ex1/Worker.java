package lec4.Ex1;

public class Worker {
    private int id;
    public String firstName;
    public String lastName;
    public int salary;
    public int age;

    public Worker(int id, String firstName, String lastName, int salary, int age) {

        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.salary = salary;
    }

    public String fullName() {
        return String.format("%s %s", firstName, lastName);
    }
}
