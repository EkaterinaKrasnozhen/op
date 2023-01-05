package seminar3;

import java.util.Iterator;
import java.util.List;

class GroupsIterator implements Iterator<Students> {

    private int index;
    private List<Students> studentList;


    public GroupsIterator(List<Students> studentList) {//получаем лист студентов и с ним работаем
        this.studentList = studentList;
    }

    @Override
    public boolean hasNext() {
        return index < studentList.size();
    }

    @Override
    public Students next() {
        return studentList.get(index++);
    }
}
