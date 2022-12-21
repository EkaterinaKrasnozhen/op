package lec2;

import java.util.ArrayList;
import java.util.List;

public class ProgHero {
    public static void main(String[] args) {
        List<Healer> team1 = new ArrayList<>();
        team1.add(new Shaman());
        // team1.add(new Paladin());
        // team1.add(new Knights());
        // team1.add(new Shaman());
        // var h = team1.get(0);
        // if (h instanceof Healer) {
        //     ((Healer)h).healing(null); //тк team наполнен разными классами обращаемся Healer h
        // }
        // else if (h instanceof Warior) {
        //     ((Warior)h).attack(null);
        // }
        // else {
        //     //...
        // }

        List<Warior> team2 = new ArrayList<>();
        team2.add(new Knights());
        team2.add(new Paladin());
        team2.get(0).attack(null);

        List<Healer> team3 = new ArrayList<>();
        team3.add(new Shaman()); //война добавить не сможем
        team3.get(0).healing(null);
        team3.add(new God());
        //((Warior)team3.get(1)).attack(team1.get(0)); // God зкоманды Healer может стать Warior тк implements Healer, Warior
    }
}
