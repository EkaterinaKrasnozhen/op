package lec5.Shape.Core;

import lec5.Shape.Calculate;
import lec5.Shape.Canvas;
import lec5.Shape.Shape;

public class Model {
    Shape panel;
    Calculate calc;

    public Model(Calculate c, String canvasName) {
        panel = new Canvas(canvasName);//"Без имени (2).jpg");
        calc = c;
    }

    public void append(Shape shape) {
        panel.shapes.add(shape);
    }

    public double area() {
        return calc.visit(panel);
    }

    public String show() {
        return panel.toString();
    }
}
