package lec5.Shape;

import java.util.ArrayList;
import java.util.List;

public abstract class Shape {
    protected double area;
    protected String name;

    public double getArea() {
        return area;
    }

    protected void setArea(double value) {
        area=value;
    }

    public void setName(String value) {
        name=value;
    }

    public String getName() {
        return name;
    }

    public List<Shape> shapes = new ArrayList<Shape>();

    private void Print(StringBuilder sb, String indent) {
        sb.append(String.format("%s %s %s\n", indent, name, getArea()));
        for (Shape shape : shapes) {
            shape.Print(sb, indent);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Print(sb, name);
        return sb.toString();
    }
}
