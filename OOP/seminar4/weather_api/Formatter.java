package seminar4.weather_api;

import com.google.gson.Gson;

import seminar4.weather_api.weather.Weather;


public class Formatter {

    public Weather parse(String info) {
        Gson json = new Gson();
        Weather weather = json.fromJson(info, Weather.class);
        return weather;
    }
}
