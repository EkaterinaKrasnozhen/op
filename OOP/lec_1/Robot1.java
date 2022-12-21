package lec_1;

//Инакапсуляция  -  свойства системы, позволяющее оъеднитьи данные и методы, 
//работающие с ними в классе, скрыв детали реализации и защитив
// от пользователя этого класса объектов
// 1. Принцип - сокрытие данных


public class Robot1 {
    /** Уровень робота*/
    private int level;

    /**Имя робота */
    private String name;
        /**
     * Создание робота
     * @param name Имя робота не должно начинаться с цифры
     * @param level Уровень робота
     */

    /**метод чтения имени */
    public String getName(){
        return this.name;
    }

    /**метод чтения уровня */
    public int getLevel(){
        return this.level;
    }

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

    public  Robot1(String name, int level) {
        this.name = name;
        this.level = level;
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
    public void work() {System.out.println("working");}
    /** Прощание   */
    private void sayBye() {System.out.println("Bye");}
        
}
