package seminar4.presenter;

import seminar4.view.View;
import seminar4.weather_api.Service;

public class Presenter {
    private View view;
    private Service service;
    
    public Presenter(View view, Service service) {
        this.view = view;
        this.service = service;
        view.setPresenter(this);

    }
    public void onClick(String city) {
        String answer = service.getWeather(city);
        view.answer(answer);
    }
}
