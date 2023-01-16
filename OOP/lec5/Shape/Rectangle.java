package lec5.Shape;

public class Rectangle extends Shape {
    private double width;
    private double height;

    public static Rectangle create(double width, double height, String name) throws UnacceptableValueExcetion {
        //if(width<0) ...
        var instance = new Rectangle();
        instance.name = name;
        instance.width = width;
        instance.height = height;
        return instance;
    }

    private Rectangle() {

    }

    @Override
    public double getArea() {
        return this.width * this.height;
    }
    @Override
    public String toString() {
        return String.format("Name: %s, Width: %d, Height: %d", name, width, height);
    }
}
