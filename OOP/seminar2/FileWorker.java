package seminar2;

public class FileWorker implements Writable {

    @Override
    public Object read() {
        System.out.println("прочитали");
        return null;
    }

    @Override
    public void save() {
        System.out.println("сохранили");
    }

    
    
}
