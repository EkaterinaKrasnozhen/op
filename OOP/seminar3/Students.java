package seminar3;

public class Students implements Comparable<Students>{
    private String name;
    private int id;


    public Students(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setId(int id) {
        this.id = id;
    }
    
    public void setName(String name) {
        this.name = name;
    }


    @Override
    public String toString() {
        return id + " " + name;
    }

    @Override
    public int compareTo(Students o) { //если считаем Объект больше = возвращаем 1, меньше -1, не сравниваем  =0
        return name.compareTo(o.getName()); //у String уже описан compareto
    }


}
