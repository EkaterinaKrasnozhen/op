package lec2;

public class Foo {
    public Integer value;
    private static Integer count; //если private не видно в extends, если protected - видно

    public static Integer getCount() {
        return count; //обращаясь к статическим членам this и super использовать не нужно
    }

    static {
        count = 0;
    }

    public Foo() {
        count++;
    }

    public void printCount() {
        System.out.println(count);
    }

}
