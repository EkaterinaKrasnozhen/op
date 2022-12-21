package lec2;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;



public class ProgMagicPriest {
    public static void main(String[] args) {
        BaseHero hero1 = new Magician(); //делаем из BaseHero Magician, принцип полиморфизма
        // System.out.println(hero1.getInfo());

        // BaseHero hero2 = new Priest();
        // System.out.println(hero2.getInfo());

        // BaseHero hero3 = new Priest();
        // System.out.println(hero3.getInfo());

        // hero3.Attack(hero1);
        // System.out.println("________");
        // System.out.println(hero1.getInfo());
        // hero3.Attack(hero3);//сам себя атаковал, неправильно
        // System.out.println("________");
        // System.out.println(hero3.getInfo());

        int teamCount = 10;
        Random rand = new Random();
        int magicalCount = 0;
        int priestCount = 0;

 
        List <Integer> r = new ArrayList<>();

        List <BaseHero> teams = new ArrayList<>();
        for (int index = 0; index < teamCount; index++) {
            int val = rand.nextInt(4);
            switch (val) {
                case 0:
                    teams.add(new Priest());
                    break;
                case 1:
                    teams.add(new Magician());
                    break;
                default:
                    //teams.add(new BaseHero()); //создать героя типа герой - неправильно, можно сделать класс BaseHero adstract и тогда не даст создать
                    break;
            }
            System.out.println(teams.get(index).getInfo());
                

        }
    }
}
