package exBeverage;

import java.util.ArrayList;

import java.util.List;

public abstract class Beverage implements Iterable<Ingredient> {
    List<Ingredient> components;
    int index;

    public Beverage() {
        components = new ArrayList<>();
        index = 0;
    }

    public void addComponent(Ingredient component) {

        if (!(components.indexOf(component) != -1))
            components.add(component);
    }
}