package Ex1;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

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
    }
}
