package Ex1;

import java.util.Iterator;

public class Worker implements Iterator<String>, Comparable<Worker>{
    public String firstName;
    public String name;
    public int age;
    public int salary;

    public Worker(String firstName, String name, int age, int salary) {
        this.firstName = firstName;
        this.name = name;
        this.age = age;
        this.salary = salary;
        this.index = 0;

    }
    public String fullName() {
        return String.format("%s %s", firstName, name);
    }
    int index;

    @Override
    public boolean hasNext() {
        return index++ < 4; // 4 поля данных
    }

    @Override
    public String next() {
        switch (index) {
            case 1: //текущее значение index = 1
                return String.format("firstName: %s", firstName);
            case 2:
                return String.format("Name: %s", name);
            case 3:
                return String.format("age: %d", age);                
            default:
                return String.format("salary: %d", salary);
        }
    }
    
    @Override
    public String toString() {
        return String.format("\n%s %d %d", fullName(), age, salary);
    }

    @Override
    public int compareTo(Worker o) {
        return Integer.compare(this.age, o.age); //более простой способ через встроенный метод compare у Integer
        //можем сделать по salary

        // if (this.age > o.age)
        //     return 1;
        // else if (this.age < o.age)
        //     return -1;
        // else
        //     return 0;
    }

    @Override
    public boolean equals(Object obj) {
        Worker temp = (Worker) obj;

        return this.age == temp.age
                && this.salary == temp.salary
                && this.firstName == temp.firstName
                && this.name == temp.name;
    }

    @Override
    public int hashCode() {
        return age;
    }
}
