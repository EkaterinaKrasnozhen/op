package homeWorkSem1.Service;
import java.io.IOException;
import java.io.Serializable;

import homeWorkSem1.FamilyTree;

public interface Writeble {
    void save(Serializable serializable) throws IOException;
    FamilyTree read() throws IOException, ClassNotFoundException;

}
