package op.OOP.lec6.Ex_Phone;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<BasePhone> phones1 = new ArrayList<BasePhone>();
        phones1.add(new IPhone());
        phones1.add(new Nokia3310());
        for (BasePhone basePhone : phones1) {
            basePhone.Call();
        }

        List<Fax> phones2 = new ArrayList<Fax>();//List<Fax> phones2 = new ArrayList<IPhone>(); не получилось прописать

        phones2.add(new IPhone());

    }
    
}
