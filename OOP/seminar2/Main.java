package seminar2;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        
        Cat cat1 = new Cat();
        Dog dog1 = new Dog();
        List<Speakable> speakbles = new ArrayList<>();
        speakbles.add(dog1);
        speakbles.add(cat1);
        
        Radio radio = new Radio();
        speakbles.add(radio);
        speakAll(speakbles);
        Writable fw = new FileWorker();
        cat1.setFw(fw);
        cat1.save();
    }


        public static void speakAll(List<Speakable> speakables) {
            for (Speakable speakable : speakables) {
                speakable.speak();
            }
        }
    
}
