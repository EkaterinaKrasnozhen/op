
// public class program {

//     public static void main(String[] args) {
//         System.out.println("да");
//     }
// }


// class Program 
// {

//     public static void main(String[] args) {
//         short age = 10; // более мелкие int
//         int salary = 60000; // 4 байта занимает, 23_234_23 разделить разряды
//         System.out.println(age);
//         System.out.println(salary);
//     }
// }
// {
// public static void main(String[] args) {
//     float e = 2.7f;
//     double pi = 3.1415; // D необязательный суффикс для double
//     System.out.println(e);
//     System.out.println(pi);
// }
// }


// {
//     public static void main(String[] args) {
//         char ch = '1';
//         System.out.println(ch);
//         System.out.println(Character.isDigit(ch));
//         char c = 'a';
//         System.out.println(Character.isDigit(c));
//         String s = "qwe";
//         System.out.println(s.charAt(0)); // обращение к индексу строки
//     }
// }

// {
//     public static void main(String[] args) {
//         boolean fi = 123 <= 236;
//         System.out.println(fi);//true
//         boolean fi2 = 123 >= 235 || fi;
//         System.out.println(fi2); //true
//         boolean fi3 = fi ^ fi2; // дизъюнкция, возвращает true тогда и только тогда, когда только одно! из значений true
//         System.out.println(fi3); //false
//     }
// }


// {
//     public static void main(String[] args) {
//         String msg = "Hello, world!";
//         System.out.println(msg);
//     }
// }
// public class program 
// {
//     public static void main(String[] args) {
//         var a = 123;
//         System.out.println(a);
//         System.out.println(getType(a));
//         var d = 33.456;
//         System.out.println(d);
//         System.out.println(getType(d));
//     }
//     static String getType(Object o) {
//         return o.getClass().getSimpleName();
//     }
// }


// классы обертки (см функционал обертка.)
//  примитив        обертка
//   int            Integer
//  short           Short
//  long            Long
//  byte            Bite
//  float           Float
//  double          Double
//  char            Character
// boolean          Boolean

// инкремент ++ если ..println(a++) постфиксный инкремент - только в след принте сделает +1, 
//если (++a) префисный инкр, то в этом же принте сделает +1

// лог операции ||- конъюнкция, && - дизъюнкция, ^ - разд.дизъюнкция ,! - инверсия