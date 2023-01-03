package exBeverage;



public class Program {
    public static void main(String[] args) {
        Beverage latte = new Coffee();
        latte.addComponent(new Water("Вода"));
        latte.addComponent(new Beans("Зерно"));
        latte.addComponent(new Milk("Молоко"));
        for (var ingredient : latte) {
            System.out.println(ingredient);                 
        }
    }

}
