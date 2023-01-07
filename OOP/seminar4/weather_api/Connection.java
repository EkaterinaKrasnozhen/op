package seminar4.weather_api;


import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class Connection {
    private static final String apiKey = "eceae5bae9142cc79ef4bb4199703b7f";

    public String getInfo(String city) {
        StringBuilder stringBuilder = new StringBuilder();
        try {
            URL url = new URL("http://api.weatherstack.com/current?access_key=" + apiKey + "&query=" + city);
            //http://api.weatherstack.com/current?access_key=eceae5bae9142cc79ef4bb4199703b7f&query=moscow
            URLConnection connection = url.openConnection();
            Scanner scanner = new Scanner(connection.getInputStream());
            while (scanner.hasNext()) {
                stringBuilder.append(scanner.nextLine());
            }
            scanner.close();   
        } catch (Exception e) {
            e.printStackTrace();
            return e.getMessage();//строковое пояснение почему ошибка
        }
        System.out.println("Ответ от сервера: " + stringBuilder.toString());//чтобы понимать, что ответ пришел и все ок
        return stringBuilder.toString();    
    }
}
