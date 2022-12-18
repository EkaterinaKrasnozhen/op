package seminar1;

public class Bottle extends Product {

    private double volume;

    /** конструктор для создания родительского объекта, со своими данными */
    public Bottle(String name, double cost, double volume) {
        super(name, cost);
        this.volume = volume;
    }

    @Override
    public String toString() {
        return super.toString() + " " + volume + "л.";
    }

    

}
