package lec2;

import java.util.Random;


public abstract class BaseHero { //асбтракция - определяются общие поля и методы, экземпляр и метод абстрактого класса вызвать нельзя, можно не описывать логику
    protected static int number;
    protected static Random r;

    protected String name;
    protected String surname;
    protected int hp;
    protected int maxHp;


    static {
        BaseHero.number = 0;
        BaseHero.r = new Random();
    } 



    public BaseHero(String name, int hp) {
        this.name = name;
        this.hp = hp;
        this.maxHp = hp;
    }

    public BaseHero() {
        this(String.format("%d", ++BaseHero.number),
                BaseHero.r.nextInt(100,200));
    }

    public String getInfo() {
        return String.format("Name: %s Hp: %d Type: %s",
        this.name, this.hp, this.getClass().getSimpleName());
    }

    public void healed(int Hp) {
        this.hp = Hp + this.hp > this.maxHp ? this.maxHp : Hp + this.hp;
    }

    public void GetDamage(int damage) {
        if (this.hp - damage > 0) {
            this.hp -= damage;
        }
        else {
            die(); // конкретная логика может быть описана уже в классе наследнике
        }
    }

    public abstract void die(); //указываем абстарктный метод в асбтсрактном классе, не описываем, тк вызвать нельзя будет

    public void Attack(BaseHero target) {
        int damage = BaseHero.r.nextInt(10, 20);
        target.GetDamage(damage);
    }
}
