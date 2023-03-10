package lec4.Ex3;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Repository <T extends Content> implements Iterable<T> { //прописываем Т - обобщения, которые могут быть только Content
    
    List<T> ds;
    private String name;


    public Repository(String name) {
        this.ds = new ArrayList<>();
        this.name = name;
        //System.out.printf("\n >> %s created\n", this.name);
    }

    public void add(T content) {
        ds.add(content);
    }

    public int count(){
        return ds.size();
    }

    public T get(Integer index) {
        return ds.get(index);
    }

    public void merge(Repository<T> list) {
        for (T element : list) {
            ds.add(element);
        }
    }

    @Override
    public Iterator<T> iterator() {
        return new IteratorContent(ds);
    }
    
}
