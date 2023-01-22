package op.OOP.lec6.Ex_Legs_Animal;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<AbstractAnimal> list1 = new ArrayList<>(Arrays.asList(new Dog(), new Python()));

        for (var animal : list1) {
            System.out.println(animal.getType());
        }

        List<Legs> list2 = new ArrayList<>(Arrays.asList(new Dog()/*new Python()*/)); //не добавит, тк не поддерживает интерфейс Legs
        for (var animal : list2) {
            System.out.println(animal.getLegsCount());
        }
    }
}
