package seminar5.Bank;

public class Client extends Thread {

    Bank bank;
    public Client(Bank bank){
        this.bank = bank;
    }

    @Override
    public void run() {
        while (true) {
            synchronized(bank) {//как транзакция работает, блокирует банк пока не закончена итерация
                bank.value += 10;
                mySleep(10);
                bank.value -= 10;
                System.out.println(bank.value);
            }
        }
    }

    private void mySleep(int val) {
        try {
            sleep(val);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
