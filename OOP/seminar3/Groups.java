package seminar3;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Groups implements Iterable<Students> {
    // Iterable = что то перебираемое
    //Iterator = абстракция, данный объект умеет перебирать
    private List<Students> studentList;

    public Groups() {
        studentList = new ArrayList<>();
    }


    public void createStudent(Students student) {
        studentList.add(student);
    }


    @Override
    public Iterator<Students> iterator() { //создаем объект класса итератор
        return new GroupsIterator(studentList);
    }

    public List<Students> getStudentList() {
        return studentList;
    }

    // class GroupsIteratot implements Iterator<Students> { //вынесли в отдельный файл

    //     private int index;
    //     @Override
    //     public boolean hasNext() {
    //         return index < studentList.size();
    //     }

    //     @Override
    //     public Students next() {
    //         return studentList.get(index++);
    //     }
    
        
    //}

}
