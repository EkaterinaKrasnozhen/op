package seminar5;

public class Main {
    public static void main(String[] args) {
        Bank bank = new Bank();
        bank.value = 100;
        Client client1 = new Client(bank);
        Client client2 = new Client(bank);
        client1.start();
        client2.start();
    }
}
