package lec_1;
import java.util.ArrayList;

public class Robot3 {
    enum State {
        On, Off
    }

    private static int defaultIndex;
    private static ArrayList<String> names;

    static {
        defaultIndex = 1;
        names = new ArrayList<String>();
    }

    /** Уровень робота*/
    private int level;

    /**Имя робота */
    private String name;
            /**
     * Создание робота
     * @param name Имя робота не должно начинаться с цифры
     * @param level Уровень робота
     */

    public Robot3(String name, int level) { 
        if (name.isEmpty() || Character.isDigit(name.charAt(0)) || Robot3.names.indexOf(name) != -1) {
            this.name = String.format("DefaultName_%d", defaultIndex++);
        }   
        else {
            this.name = name;
        }
        Robot3.names.add(this.name);
        this.level = level;
        this.state = State.Off;
    }

    /**Состояние */
    private State state;

    /**кнопка ВКЛ */
    public void powerOn() {
        this.startBIOS();
        this.startOS();
        this.sayHi();
    }

    /**кнопка ВЫКЛ */
    public void powerOff() {
        this.sayBye();
        this.stopOS();
        this.stopBIOS();
    }

    

    // public Robot3(String name) { 
    //     if (name.isEmpty() || Character.isDigit(name.charAt(0)) || Robot3.names.indexOf(name) == -1) {
    //         this.name = String.format("DefaultName_%d", defaultIndex++);
    //     }   
    //     else {
    //         this.name = name;
    //     }

    //     Robot3.names.add(this.name);
    //     this.level = 1;
    //     this.state = State.Off;
    // }

    // public Robot3() { 
    //     
    //     this.name = String.format("DefaultName_%d", defaultIndex++);
    //     Robot3.names.add(this.name);
    //     this.level = 1;
    //     this.state = State.Off;
    // }

    public Robot3(String name) {
        this(name, 1);
    }

    public Robot3() {
        this("");
    }

    //методы вкл/выкл подсистем
    /** Загрузка BIOS   */
    private void startBIOS() {System.out.println("Start BIOS...");}
    /** Загрузка BIOS   */
    private void startOS() {System.out.println("Start OS..");}
    /** Приветствие   */
    private void sayHi() {System.out.println("Hello");}
    /** Выгрузка BIOS   */
    private void stopBIOS() {System.out.println("Stop BIOS...");}
    /** Выгрузка BIOS   */
    private void stopOS() {System.out.println("Stop OS..");}
    /** Работа   */
    //public void work() {System.out.println("working");}
    /** Прощание   */
    private void sayBye() {System.out.println("Bye");}

    public void power() {
        if (this.state == State.Off) {
            this.powerOn();
            this.state = State.On;
        }
        else {
            this.powerOff();
            this.state = State.Off;
        }
        System.out.println();
    }

    /** Работа   */
    public void work() {
        if (this.state == State.On) {
            System.out.println("working..");
        }
    }

    @Override
    public String toString() {
        return String.format("%s, %d\n", name, level);
    }
}


