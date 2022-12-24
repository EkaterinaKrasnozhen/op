package homeWorkSem1;
import java.io.IOException;
import java.io.Serializable;
import java.util.List;
public interface Writeble {
    void save(Serializable serializable);
    FamilyTree read() throws IOException;
}
