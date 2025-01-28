import requests

class WeatherData:
    def __init__(self):
        self.owm_api_key = 'c8537154778558a3c9e30c03f18a1672'
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def processRequest(self, req):
        try:
            self.result = req.get("queryResult")
            self.parameters = self.result.get("parameters")
            self.city = self.parameters.get("geo-city")

            print(f"city : {self.city}")
            
            # API request to OpenWeatherMap
            params = {
                'q': self.city,
                'appid': self.owm_api_key,
                'units': 'metric'  # for Celsius temperatures
            }

            response = requests.get(self.base_url, params=params)
            if response.status_code != 200:
                raise Exception("Failed to fetch weather data")

            data = response.json()
            print(data)

            # Extract relevant weather information
            # self.lat = data['coord']['lat']
            # self.lon = data['coord']['lon']
            self.condition = data['weather'][0]['main']
            self.wind_speed = data['wind']['speed']
            self.humidity = data['main']['humidity']
            self.temp_min_celsius = data['main']['temp_min']
            self.temp_max_celsius = data['main']['temp_max']

            # Construct the speech output
            speech = (
                f"Today's the weather in {self.city}: "
                f"Humidity: {self.humidity}% , "
                f"Wind Speed: {self.wind_speed} m/s , "
                f"Minimum Temperature: {self.temp_min_celsius}°C , "
                f"Maximum Temperature: {self.temp_max_celsius}°C , "
                f"Condition: {self.condition}" 
            )

        except Exception as e:
            print(f"Error: {e}")
            speech = "Sorry, I couldn't fetch the weather data at the moment. Please try again later."

        return {
            "fulfillmentText": speech,
            "displayText": speech
        }
