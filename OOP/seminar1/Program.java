package seminar1;

import java.util.ArrayList;
import java.util.List;

public class Program {
    public static void main(String[] args) {
        VendingMachine vMachine = new VendingMachine();//первый констурктор, просто создали
        List<Product> prod = new ArrayList<>(); // некий список продкутов
        VendingMachine vMachine2 = new VendingMachine(prod);// с помощью 2го конструктор, сразу помещаем список продуктов
        vMachine.add(new Bottle("cola", 100, 2)); //анонимный класс, не создаем сслыку как до = 
        vMachine.add(new Product("fanta", 200));
        vMachine.add(new Product("sprite", 99));
        List<Product> list = vMachine.getProductbyCost(150);
        System.out.println(list);
        System.out.println(vMachine);
    }       
}