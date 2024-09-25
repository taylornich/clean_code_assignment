# question 1 task 1

class WeatherDataFetcher:

    def __init__(self, city):
        self.city = city

    def fetch_weather_data(self):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {self.city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})

class DataParser:

    def __init__(self, data):
        self.data = data

    def parse_weather_data(self):
        # Function to parse weather data
        if not self.data:
            return "Weather data not available"
        city = self.data["city"]
        temperature = self.data["temperature"]
        condition = self.data["condition"]
        humidity = self.data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:


    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        fetcher = WeatherDataFetcher(city)
        data = fetcher.fetch_weather_data()
        parser = DataParser(data)
        return parser.parse_weather_data()

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        fetcher = WeatherDataFetcher(city)
        data = fetcher.fetch_weather_data()
        parser = DataParser(data)
        if not data:
            return f"Weather data not available for {city}"
        parser = DataParser(data)
        return f"Weather in {city}: {data['temperature']} degrees, {data['condition']}."

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break

            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()