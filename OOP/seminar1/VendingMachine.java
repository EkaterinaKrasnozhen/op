package seminar1;

import java.util.ArrayList;
import java.util.List;

public class VendingMachine { // все классы наследуются от класса extends(расширяет) Object
    List<Product> products;// просто ссылка на лист продуктов, пока нет = ArrayList..

    public VendingMachine( List <Product> products) { //конструкторы должны отличаться набором аргументов или вообще ничего
        //super();
        this.products = products; 
    }

    /** инициализация products, вызываем верхний конструктор List <Product> products*/
    public VendingMachine() { //перегружаем встроенный метод, так так при создании public VendingMachine( List <Product> products)
        this(new ArrayList<>());                      //этот автоматически удалился. Он нужен для создания объекта класса
    }

    //сначала создаем объект родиетльского класса, super, в првом констуркторе он по умолчанию super();

    public List<Product> getProductbyCost(double cost) {
        List<Product> res = new ArrayList<>();
        for (Product product : products) {
            if (product.getCost() <= cost) {
                res.add(product);
            }
        }
        return res;
    }

    public void add(Product product) {
        products.add(product);
    }

    @Override
    public String toString() {
        return "VendingMachine [products=" + products + "]";
    }
}    
