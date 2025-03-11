from dotenv import load_dotenv
import os
import requests
import math
import sys


load_dotenv()




api_key = os.getenv("API_KEY")

city = input("Enter the city name: ")

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    
    temp = response['main']['temp']
    temp = math.ceil(temp - 273.15)
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description']
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

get_weather(api_key, city)