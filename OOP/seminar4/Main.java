package seminar4;

import seminar4.presenter.Presenter;
import seminar4.view.View;
import seminar4.view.WeatherUI;
import seminar4.weather_api.Service;
import seminar4.weather_api.WeatherService;

public class Main {
    public static void main(String[] args) {
        View view = new WeatherUI();
        Service service = new WeatherService();
        Presenter presenter = new Presenter(view, service);
        
        view.start();
    }
}
