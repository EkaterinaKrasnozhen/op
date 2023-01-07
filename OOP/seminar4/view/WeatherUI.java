package seminar4.view;

import java.util.Scanner;

import seminar4.presenter.Presenter;

public class WeatherUI implements View {

    private Presenter presenter;
    private Scanner scanner;
    
    public WeatherUI(){
        scanner = new Scanner(System.in);
    }
    @Override
    public void start() {
        String city = scan();
        presenter.onClick(city);//2. обратится к презентеру
    }

    private String scan(){
        System.out.println("Напишите город: ");//1. View попросит город, где нужно узнать погоду
        return scanner.nextLine();
    }

        
    public void setPresenter(Presenter presenter) {//3. презентер отработает. Каждый презентр работает со своим View
        this.presenter = presenter;
    }

    @Override
    public void answer(String message) {//4. и выведет ответ в View
        System.out.println(message);
    }


    
}
