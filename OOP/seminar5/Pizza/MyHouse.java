package seminar5.Pizza;

public class MyHouse extends Thread{
    boolean arrivedPizza = false;

    public void eat() {
        synchronized(this) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("ням");
        }
    }

    public void pizza() {
        synchronized(this){
            arrivedPizza = true;
            notifyAll();//разбудит
        }
        
    }

    @Override
    public void run() {
        eat();
    }
}
