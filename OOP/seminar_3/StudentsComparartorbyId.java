package seminar_3;

import java.util.Comparator;

public class StudentsComparartorbyId implements Comparator<Students> {

    @Override
    public int compare(Students o1, Students o2) { //вызывает внутри метод сорт и сортирует внутри себя коллекцию
        return Integer.compare(o1.getId(), o2.getId());
    }
    
}
