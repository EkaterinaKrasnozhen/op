package seminar5.Pizza;

public class Main {
    public static void main(String[] args) {
        
        MyHouse house = new MyHouse();
        house.start();//уснул в своем потоке MyHouse

        PizzaBoy boy = new PizzaBoy(house);
        boy.start();//разбудит
    }
}
