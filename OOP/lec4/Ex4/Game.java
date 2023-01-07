package lec4.Ex4;

public class Game {
    public static void main(String[] args) {
        System.out.println("Game1");

        Team<Junior> team1 = new Team<>("Воробушки");
        team1.add(CreateEmployee.createJunior());
        team1.add(CreateEmployee.createJunior());
        
        System.out.println(team1);

        Team<Junior> team2 = new Team<>("Хлебушки"); //указали что создаем камнаду Juinior
        team2.add(CreateEmployee.createJunior());
        team2.add(CreateEmployee.createJunior());
        //team2.add(CreateEmployee.createMiddler()); //добавить Middle уже не получится
        System.out.println(team2);

        var o = new Olympiad<Junior>(team1, team2);
        o.start();

    }
}
