package lec2;

public class Task1 {
    public static void main(String[] args) {
        Foo f1 =  new Foo();        
        f1.value = 123; // когда вызываем Foo будет count++
        //System.out.println(f1.value);
        System.out.println();
        f1.printCount(); //1 

        Foo f2 =  new Foo();
        f2.value = 222;
        //System.out.println(f2.value);
        System.out.println();
        f2.printCount();//2

        Foo f3 =  new Foo();
        f3.value = 444;
        //System.out.println(f3.value);
        System.out.println();
        f3.printCount();//3

    }
}
