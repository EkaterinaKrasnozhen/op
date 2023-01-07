package seminar_3;


import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

// <> дженерики
public class Groups<T> implements Iterable<T> { //<T exstends Students> прямо все объекты дадут ошибку, лучше все таки ограничить например Students
    // Iterable = что то перебираемое
    //Iterator = абстракция, данный объект умеет перебирать
    private List<T> studentList;

    public Groups() {
        studentList = new ArrayList<>();
    }


    public void createStudent(T student) { //public <E> void createStudent(T student, E e) - можно два типа указать
        studentList.add(student);
    }

    public List<T> getStudentList() {
        return studentList;
    }

    @Override
    public Iterator<T> iterator() { //создаем объект класса итератор
        return new GroupsIterator<>(studentList);
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
