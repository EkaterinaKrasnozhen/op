package seminar_3;

import java.util.Iterator;
import java.util.List;

class GroupsIterator<T> implements Iterator<T> {

    private int index;
    private List<T> studentList;


    public GroupsIterator(List<T> studentList) {//получаем лист студентов и с ним работаем
        this.studentList = studentList;
    }

    @Override
    public boolean hasNext() {
        return index < studentList.size();
    }

    @Override
    public T next() {
        return studentList.get(index++);
    }
}
