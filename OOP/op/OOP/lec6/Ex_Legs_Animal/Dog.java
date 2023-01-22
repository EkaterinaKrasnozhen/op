package op.OOP.lec6.Ex_Legs_Animal;

public class Dog extends AbstractAnimal implements Legs {

    @Override
    public String getType() {
        return "собачка";
    }

    @Override
    public int getLegsCount() {
        return 4;
    }
    
}
