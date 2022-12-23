package seminar2;

import java.io.Serializable;

public interface Writable {
    //void save(Serializable serializable); //люой потом можем класс передавать
    void save();
    Object read();
}
