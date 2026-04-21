import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherApp:
    def __init__(self):
        """Initialize the Weather App with API configuration."""
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.timezone_url = "https://api.openweathermap.org/data/2.5/timezone"
        self.temperature_unit = "Celsius"  # Default unit
        self.temp_symbol = "°C"
        
        if not self.api_key:
            raise ValueError(
                "❌ API key not found! Please set OPENWEATHER_API_KEY in your .env file"
            )
    
    def get_weather(self, city, country=None):
        """
        Fetch weather data for a given city and optional country.
        
        Args:
            city (str): City name
            country (str, optional): Country code (e.g., 'US', 'UK', 'ES')
        
        Returns:
            dict: Weather data or error message
        """
        # Format location string
        location = f"{city},{country}" if country else city
        
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'  # Always fetch in metric, convert based on user preference
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                return {"error": f"❌ Location '{location}' not found. Please check the spelling."}
            return {"error": f"❌ API Error: {response.status_code}"}
        except requests.exceptions.Timeout:
            return {"error": "❌ Request timeout. Please check your internet connection."}
        except requests.exceptions.RequestException as e:
            return {"error": f"❌ Connection error: {str(e)}"}
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    def toggle_temperature_unit(self):
        """Toggle between Celsius and Fahrenheit."""
        if self.temperature_unit == "Celsius":
            self.temperature_unit = "Fahrenheit"
            self.temp_symbol = "°F"
        else:
            self.temperature_unit = "Celsius"
            self.temp_symbol = "°C"
        return self.temperature_unit
    
    def format_temperature(self, celsius_temp):
        """Format temperature based on current unit setting."""
        if self.temperature_unit == "Fahrenheit":
            temp = self.celsius_to_fahrenheit(celsius_temp)
        else:
            temp = celsius_temp
        return f"{temp:.1f}{self.temp_symbol}"
    
    def get_local_time(self, timezone_offset):
        """Get local time based on timezone offset."""
        utc_now = datetime.utcnow()
        from datetime import timedelta
        local_time = utc_now + timedelta(seconds=timezone_offset)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    
    def display_weather(self, weather_data):
        """Display formatted weather information."""
        if "error" in weather_data:
            print(f"\n{weather_data['error']}\n")
            return
        
        try:
            city = weather_data.get('name', 'Unknown')
            country = weather_data.get('sys', {}).get('country', 'Unknown')
            temperature = weather_data.get('main', {}).get('temp', 0)
            humidity = weather_data.get('main', {}).get('humidity', 0)
            description = weather_data.get('weather', [{}])[0].get('main', 'Unknown')
            wind_speed = weather_data.get('wind', {}).get('speed', 0)
            pressure = weather_data.get('main', {}).get('pressure', 0)
            timezone_offset = weather_data.get('timezone', 0)
            lat = weather_data.get('coord', {}).get('lat', 0)
            lon = weather_data.get('coord', {}).get('lon', 0)
            
            local_time = self.get_local_time(timezone_offset)
            formatted_temp = self.format_temperature(temperature)
            
            print("\n" + "="*60)
            print(f"🌤️  Weather in {city}, {country}")
            print("="*60)
            print(f"🕐 Local Time: {local_time}")
            print(f"🌡️  Temperature: {formatted_temp}")
            print(f"💧 Humidity: {humidity}%")
            print(f"📍 Conditions: {description}")
            print(f"🌪️  Wind Speed: {wind_speed} m/s")
            print(f"🔽 Pressure: {pressure} hPa")
            print(f"📌 Coordinates: {lat}, {lon}")
            print("="*60 + "\n")
            
        except (KeyError, TypeError) as e:
            print(f"\n❌ Error displaying weather data: {str(e)}\n")
    
    def run(self):
        """Run the interactive weather app."""
        print("\n" + "🌤️ " * 15)
        print("Welcome to the Weather App!")
        print("🌤️ " * 15 + "\n")
        
        while True:
            print(f"Current Temperature Unit: {self.temperature_unit} ({self.temp_symbol})")
            print("\nMenu:")
            print("1. Get weather for a city")
            print("2. Toggle temperature unit")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                city = input("Enter city name: ").strip()
                if not city:
                    print("❌ City name cannot be empty!")
                    continue
                
                country = input("Enter country code (optional, e.g., 'US', 'UK', 'ES'): ").strip()
                
                print("\n⏳ Fetching weather data...\n")
                weather_data = self.get_weather(city, country if country else None)
                self.display_weather(weather_data)
            
            elif choice == "2":
                new_unit = self.toggle_temperature_unit()
                print(f"\n✅ Temperature unit changed to {new_unit}!\n")
            
            elif choice == "3":
                print("\n👋 Thank you for using the Weather App! Goodbye!\n")
                break
            
            else:
                print("\n❌ Invalid choice! Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    try:
        app = WeatherApp()
        app.run()
    except ValueError as e:
        print(f"\n{e}\n")
        print("📖 Setup Instructions:")
        print("1. Create a .env file in the project directory")
        print("2. Add: OPENWEATHER_API_KEY=your_api_key_here")
        print("3. Get a free API key from: https://openweathermap.org/api\n")
