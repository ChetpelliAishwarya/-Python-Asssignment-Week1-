# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:29:50 2025

@author: Hi
"""

#
import requests  # Importing requests library for making API calls
import datetime  # For adding timestamps in log file


# ---------------------------------------------------------
# Function 1: Fetch Weather Data
# ---------------------------------------------------------
def fetch_weather(city: str, api_key: str) -> dict:


    try:
        # Construct the full API URL with city name, API key, and metric units
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        # Make the GET request to the API
        response = requests.get(url)

        # If API returns an HTTP error (like 404, 401), raise an exception
        response.raise_for_status()

        # Convert JSON response to Python dictionary
        return response.json()

    except requests.exceptions.HTTPError:
        # Handle invalid city error
        return {"error": "Invalid city name or unauthorized API key."}

    except requests.exceptions.ConnectionError:
        # Handle network issues
        return {"error": "Network connection error. Check your Internet."}

    except Exception as e:
        # Catch any other unexpected errors
        return {"error": str(e)}


# ---------------------------------------------------------
# Function 2: Analyze Weather Data
# ---------------------------------------------------------
def analyze_weather(weather_data: dict) -> str:
    """
    Takes the JSON weather dictionary and returns a readable summary.
    """

    # If error exists, return the error message immediately
    if "error" in weather_data:
        return weather_data["error"]

    # Extract temperature, wind speed, humidity from the API response
    temp = weather_data["main"]["temp"]               # Current temperature
    wind = weather_data["wind"]["speed"]              # Wind speed in m/s
    humidity = weather_data["main"]["humidity"]       # Humidity percentage

    # Determine temperature category
    if temp <= 11:
        summary = "Cold (<=10°C)"
    elif temp < 25:
        summary = "Mild (11–24°C)"
    else:
        summary = "Hot (>=25°C)"

    # Add warnings based on wind and humidity values
    if wind > 10:
        summary += "  High wind alert!"
    if humidity > 80:
        summary += " Humid conditions!"

    return summary


# ---------------------------------------------------------
# Function 3: Log Weather to CSV File
# ---------------------------------------------------------
def log_weather(city: str, filename: str, api_key: str):
    """
    Fetches weather, analyzes it, and logs results to a CSV file.
    """

    # First, fetch weather data for the city
    weather = fetch_weather(city, api_key)

    # Analyze the fetched weather data
    summary = analyze_weather(weather)

    # Open the CSV file in append mode so new entries are added continuously
    with open(filename, "a",encoding="utf-8-sig") as file:

        # Add a timestamp for logging when data was fetched
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # If weather returned an error, log error only
        if "error" in weather:
            file.write(f"{timestamp},{city},ERROR,{weather['error']}\n")

        else:
            # Extract required actual weather values
            temp = weather["main"]["temp"]
            wind = weather["wind"]["speed"]
            humidity = weather["main"]["humidity"]

            # Write CSV row: timestamp, city, temperature, wind, humidity, summary
            file.write(f"{timestamp},{city},{temp},{wind},{humidity},{summary}\n")

    print(f"Weather for {city} logged successfully!")


# ---------------------------------------------------------

# ---------------------------------------------------------
api_key = "f94f4a31733063f3b7c11e1acedbd126"   
log_weather("London", "weather_log.csv", api_key)

        
        
        
        