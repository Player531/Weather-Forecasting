import requests
import json

api_key = "API KEY" #Enter your openweathermap api key 
city = "New York" #Enter any city name

api_endpoint = f"https://api.openweathermap.org/data/2.5/weather"
query_params = {'q': city, 'appid': api_key, 'units': 'metric'}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"{city}: {temperature}°c")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} Kmph")
else:
    print(f"Error: {response.status_code} - {response.text}")
