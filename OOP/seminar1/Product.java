package seminar1;

public class Product {
    private String name; //скрыли, невозможно в main обратиться product.name = ..
    private double cost; // все поля пишем вверху класса

    //потом публичные методы
    // потом приватные

    public Product(String name, double cost) {
        this.name = name; 
        this.cost = cost;
    }
    
    //инкапсуляция, скрыть информацию. Например банкомат = для клиента внести/снять.. 
    //А скрыто - отправить инфу в банк, сделать запрос в банк

    //геттеры - получить инфу
    //сеттеры - задать
    
    public String getName() { //public - открытый
        return name;
    }

    public double getCost() {
        return cost;
    }

    public void setCost(double cost) {
        if (cost > 0) {//проверка на положительное значение
            this.cost = cost;
        }
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override //переопределяем метод из родительского класса, полиморфизм
    public String toString() {
        return name + " " + cost + " руб.";
    }

}
