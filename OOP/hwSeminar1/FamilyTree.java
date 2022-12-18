package hwSeminar1;

import java.util.ArrayList;
import java.util.List;

public class FamilyTree {
    
    List<Human> humans;
    
    /**Инициализация humans */
    public FamilyTree(List<Human> humans) {
        this.humans = humans;
    }

    /**Добавление нового human в список */
    public FamilyTree() {
        this(new ArrayList<>());
    }

    /**Добавление нового Human */
    public void add(Human human) {
        humans.add(human);
    }

    /**Поиск по имени */
    public List<Human> getHumanByName(String findByName) {
        List<Human> res = new ArrayList<>();
        for (Human human : humans ) {
            if (human.getName() == findByName) {
                res.add(human);
            }
        }
        return res;
    }

    /**Переопределение метода toString */
    @Override
    public String toString() {
        return "Family Tree: \n" + humans + " ";
    }
}
