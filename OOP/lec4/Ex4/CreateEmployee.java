package lec4.Ex4;

class CreateEmployee <T> {
    public static Programmer createNewEmployee(int i) {
       switch (i) {
        case 0:
            return new Junior();
        case 1:
            return new Middle();
        default:
            return new Seniors();
       } 
    }

    public static Junior createJunior() {
        return new Junior();
    }
    
    public static Middle createMiddler() {
        return new Middle();
    }

    public static Seniors createSeniors() {
        return new Seniors();
    }

}
