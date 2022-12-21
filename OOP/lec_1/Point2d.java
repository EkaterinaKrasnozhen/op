
/** 
 * конструктор 2D
*/

public class Point2d {
    private int y, x; // не переменные, а поле. если не указывать private - по умолчанию public
    // если  private - то доступ из других файлов закрыт - и на просмотрт и на изменения, можно описать отдельный метод
    
    /**
     * метод опредение расстояния между 2мя точками
     * @param a точка a
     * @param b точка b
     * @return расстояние между a и b
     */
    
    static double distance(Point2d a, Point2d b) {
        return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2)); // не доступен если x, y = private
    }
    public  int getX() {//получить инфо о точке
        return x;
    }
    
    public  int getY() {
        return y;
    }

    public void setX(int value) { //присваиваем новое значение х
        this.x = value;
    }

    public void setY(int value) {//присваиваем новое значение y
        this.x = value;
    }
    
    /**
     * конструктор
     * @param valueX координата х
     * @param valueY координата y
     */
    public Point2d(int valueX, int valueY) { //можно быстро добавить снипетом ctor
        x = valueX;
        y = valueY;       // не метод, нет возвращаемого типа. Конструктор
    }

    
    public Point2d(int value) {
        this(value, value); //пробросили из верхнего метода, там уже описано поведение
    }

    public Point2d() { // принцип dry, один раз код - потом только подставляем значения
        this(0); // вызываем сначала метод Point2d(int value) -> потом он Point2d(int valueX, int valueY)
    }

    // public Point2d() { // делаем перегрузку констуктора
    //     x = 0;
    //     y = 0;
    // }

    // public Point2d(int value) { //public - модификатор доступа, доступен всем, private : внутри того класса, где делаем
    //     x = value;
    //     y = value;
    // }

    public String getInfo() {
        return String.format("x: %d; y: %d", x, y);
    }

    @Override // переопределили поведение, которое было до нас
    public String toString() {
        return getInfo();
    }
// перегрузка метода - для C#, Java, когда мы написали сами и переделали
   
}
