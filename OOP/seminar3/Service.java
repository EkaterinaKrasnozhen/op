package seminar3;

import java.util.Collections;

public class Service {
    private Groups group;
    private static int id; //делаем здесь, чтобы была одна общая переменная для всех учебных групп

    public Service(Groups group) {
        this.group = group;
    }
    
    public void createStudent(String name) {
        Students student = new Students(name, id++); //или group.createStudent(New Students student(name, id++)); или ++id тогда первый студент = 1
        group.createStudent(student);
    }

    public void sortbyName() { //можно передать учебную группу в качестве аргумента
        Collections.sort(group.getStudentList());
    }

    public void sortById() {
        Collections.sort(group.getStudentList(), new StudentsComparartorbyId());
    }



    //Comparartor = умеет сравнивать объекты
}
