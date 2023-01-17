package seminar5.Pizza;

public class PizzaBoy extends Thread {
    MyHouse house;
    
    public PizzaBoy(MyHouse house) {
        this.house = house;
    }
    
    @Override
    public void run() {
        try {
            sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        house.pizza();
    }
}
