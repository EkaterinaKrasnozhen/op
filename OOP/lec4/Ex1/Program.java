package lec4.Ex1;


import java.util.UUID;

//парметрический полиморфизм = какое то поле какого-то типа
public class Program {
    public static void main(String[] args) {
        Worker w = new Worker(1, "Kate", "Kras", 100000, 37);
        ParametrizedWorker<Integer> pw = new ParametrizedWorker<Integer>(222, 
        "Pavel", "Blinov", 200000, 38);
        String uid = UUID.randomUUID().toString();
        ParametrizedWorker<String> pw2 = new ParametrizedWorker<String>(uid, "Yarik",
        "Blinov", 500000, 18);
    }
}
