package lec2;

public class Human extends Magician {
    int mp;
    public Object children;

    public Human (String name, int hp, int mp) {
        super();
        System.out.println("вызван Human(String name, int hp)");
        this.hp = (int)(hp*0.8); //напрмер решили здоровье уменьшить, привели к типу int
        this.mp = mp; //если нужно к конструктору Migician еще добавить
    }

    public Human() {
        this("", 0, 0);
        System.out.println("вызван Human()");
    }
}
