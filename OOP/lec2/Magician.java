package lec2;
import java.util.List;
import java.util.ArrayList;

// 2. Принцип Инкапсуляции - Наследование: св-во системы, позволяющее описать новый класс на основе уже существующего, 
// с частично или полностью заимствованной функциональностью. Класс, от которого наследование - родительский/базовый.
// Новый класс - потомок, наследник, произвольный класс.

public class Magician extends BaseHero{ // Magician производное от BaseHero


    private int mana;
    private int maxMana;

    public Magician() {
        super(String.format("Hero_Magician #%d", ++Magician.number),
                Magician.r.nextInt(100,200));
        this.maxMana = Magician.r.nextInt(50, 150);
        this.mana = maxMana;
    }

    public int Attack() {
        int damage = Magician.r.nextInt(20,30);
        this.mana -= (int)(damage * 0.8);
        if (mana < 0) return 0;
        else return damage;
    }

    public String getInfo() {
        return String.format("%s Mana: %d",
        super.getInfo(), this.mana);
    }

    @Override
    public void die() {
        System.out.println("Умирает Волшебник");
    }
}
