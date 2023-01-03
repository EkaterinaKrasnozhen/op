package Ex1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

public class Program {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(12);
        nums.add(123);
        nums.add(12345);

        Iterator<Integer> iter = nums.iterator();
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }

        Worker worker = new Worker("Kate", "Kras", 37, 200000);
        Iterator<String> components = worker;
        while (components.hasNext()) {
            System.out.println(worker.next());
        }

        Random r = new Random();
        List<Integer> numbers  = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            numbers.add(r.nextInt(1, 20));
        }

        List<Worker> db = new ArrayList<>();
        for (int index = 0; index < 5; index++) {
            db.add(new Worker("Имя" + index, "Name" + index, r.nextInt(18, 45), 
            r.nextInt(100000, 150000)));
        }
        System.out.println(db);
        Collections.sort(db); //сортируем по возрасту, как указали в @override compareTo в Worker implements Comparable<Worker>
        System.out.println(db);
        db.sort(new SalaryComparator());// чтобы работал .sort можно создать отдельный класс SalaryComparartor implements Comparable<Worker>
        System.out.println(db);

        //еще вариант описать логику comparator

        Worker w1 = new Worker("Имя", "Фамилия", 20, 20);
        Worker w2 = new Worker("Имя", "Фамилия", 25, 20);
        //db.sort((w1, w2) -> Integer.compare(w1.age, w2.age)); // не работает
    }
}
