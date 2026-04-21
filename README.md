# 🌤️ Weather App

A simple yet powerful Python weather application that provides real-time weather data, local time, and humidity levels for any location in the world using the OpenWeatherMap API.

## Features

✨ **Key Features:**
- 🌍 Search weather by city and country
- 🌡️ Toggle between Celsius and Fahrenheit
- 🕐 Display local time for the location
- 💧 Show humidity levels
- 🌪️ Wind speed information
- 🔽 Atmospheric pressure
- 📍 Geographic coordinates
- 💾 Easy-to-use interactive menu

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- OpenWeatherMap API key (free tier available)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/cruzbarcelona09-maker/1st-py-project.git
cd 1st-py-project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

**Get your free OpenWeatherMap API key:**
1. Go to [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key

**Add your API key to the environment:**

Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

Edit `.env` and add your API key:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

## Usage

### Run the Application
```bash
python weather_app.py
```

### Menu Options

The app presents an interactive menu with the following options:

1. **Get weather for a city**: Enter city name and optionally country code
   - Example: City: "London", Country: "UK"
   - Example: City: "New York", Country: "US"
   - Example: City: "Tokyo" (country optional)

2. **Toggle temperature unit**: Switch between Celsius (°C) and Fahrenheit (°F)

3. **Exit**: Close the application

### Example Output

```
🌤️ Weather in London, GB
============================================================
🕐 Local Time: 2026-04-21 14:30:45 GMT
🌡️ Temperature: 15.5°C
💧 Humidity: 72%
📍 Conditions: Partly cloudy
🌪️ Wind Speed: 3.2 m/s
🔽 Pressure: 1013 hPa
📌 Coordinates: 51.5085, -0.1257
============================================================
```

## Project Structure

```
1st-py-project/
├── weather_app.py      # Main application
├── config.py           # Configuration and API settings
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── README.md           # This file
```

## API Reference

### WeatherApp Class Methods

#### `__init__()`
Initializes the weather app with default settings.

#### `get_weather(city, country=None)`
Fetches weather data for a given location.
- **Parameters:**
  - `city` (str): City name
  - `country` (str, optional): Country code (e.g., 'US', 'UK', 'ES')
- **Returns:** Dictionary with weather data or error message

#### `toggle_temperature_unit()`
Toggles between Celsius and Fahrenheit.
- **Returns:** Current temperature unit

#### `display_weather(weather_data)`
Displays formatted weather information.

## Error Handling

The app includes robust error handling for:
- Invalid city/country names
- API connection errors
- Missing or invalid API key
- Network timeouts

## Data Provided

Each weather query returns:
- 🏙️ City and Country name
- 🕐 Local time at that location
- 🌡️ Temperature (in selected unit)
- 💧 Humidity percentage
- 📍 Weather conditions
- 🌪️ Wind speed
- 🔽 Atmospheric pressure
- 📌 Geographic coordinates (latitude, longitude)

## Troubleshooting

### "API key not found" error
- Ensure `.env` file is created and contains your API key
- Check that `OPENWEATHER_API_KEY` is set correctly

### "Location not found" error
- Verify the city name spelling
- Try adding the country code for clarification
- Some smaller cities may not be recognized

### Connection errors
- Check your internet connection
- Verify the API is accessible at openweathermap.org
- Check if your API key is valid and not expired

## Limitations

- Free tier has rate limits (60 calls/minute)
- Some very small locations may not be available
- Weather data is current; historical data requires premium API

## Future Enhancements

- 📅 Add weather forecast (hourly/daily)
- 📍 Save favorite locations
- 💾 Cache recent searches
- 📊 Weather trends and statistics
- 🔔 Weather alerts and notifications
- 🌐 Web interface using Flask/Django

## License

This project is open source and available under the MIT License.

## Support

For issues or feature requests, please open an issue on GitHub.

## Author

**cruzbarcelona09-maker**

---

Happy weather checking! 🌤️