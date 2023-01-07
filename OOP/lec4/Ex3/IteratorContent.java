package lec4.Ex3;

import java.util.Iterator;
import java.util.List;

public class IteratorContent<T> implements Iterator<T> {
    
    private int index;
    private List<T> ds;

    public IteratorContent(List<T> ds){
        this.ds = ds;
    }
    
    @Override
    public boolean hasNext() {
        return index < ds.size();
    }

    @Override
    public T next() {
        return ds.get(index++);
    }

}
