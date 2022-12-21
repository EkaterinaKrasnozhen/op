public class example2 {

    public static void main(String[] args) {
        // Point2d a = new Point2d();// определяем экземпляр класса
        // a.x = 0; //а будет размещаться в стеке, остальное в куче
        // a.y = 2;

        // Point2d b = new Point2d(); //клиентский метод
        // b.y = 0; //раньше тут прописывали поля (перемееные)
        // b.y = 10;
        Point2d a = new Point2d(2, 0); //теперь сделали в Point2, так что сразу в скобках указываем
        Point2d b = new Point2d(10); //теперь сделали в Point2, так что сразу в скобках указываем

        System.out.println(b.getInfo());
        System.out.println(a.toString());
        a.setX(32);//задаем новое значение через метод
        System.out.println(a.getX());
        System.out.println(b.getY());
        var dis = Point2d.distance(a, b);//если static то обращение через имя тип Point2d, не через конкретные экз (a,b)
        System.out.println(dis);
    }
}
