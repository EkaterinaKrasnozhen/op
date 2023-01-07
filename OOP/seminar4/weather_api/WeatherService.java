package seminar4.weather_api;

import seminar4.weather_api.weather.Weather;

public class WeatherService implements Service {

    private Connection connection;
    private Formatter formatter;

    public WeatherService() {
        connection = new Connection();
        formatter = new Formatter();
    }

    @Override
    public String getWeather(String city) {
        String info = connection.getInfo(city);//возвращает строку и передаем
        Weather weather = formatter.parse(info);// в форматтор
        return weather.toString();
    }
    
}
