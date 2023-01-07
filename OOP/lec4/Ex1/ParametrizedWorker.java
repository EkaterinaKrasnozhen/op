package lec4.Ex1;

public class ParametrizedWorker<E> { //при создании экземпляра, вместо E укажем например Integer и тогда id будет Integer
    private E id;
    public String firstName;
    public String lastName;
    public int salary;
    public int age;

    public ParametrizedWorker(E id, String firstName, String lastName, int salary, int age) {

        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.salary = salary;
    }
}

