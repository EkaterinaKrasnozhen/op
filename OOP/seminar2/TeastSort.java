package seminar2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class TeastSort {
    public static void main(String[] args) {
        ArrayList list = new ArrayList<>(); //можно List = new ArrayList<>(); но тогда не видны методы addFirst и тд
        sort(list);
        LinkedList lis1 = new LinkedList<>();
        sort(lis1);//не работает с Linked, когда сделали в void sort (List list) все ок
    }

    public static void sort(List list) { //для демонстрации static/ сделали не конкретно Array List или Linked а просто List - это тоже интерфейс
        Collections.sort(list);
    }
}
