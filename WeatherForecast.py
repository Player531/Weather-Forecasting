import requests
from tkinter import *

OPEN_WEATHER_MAP_API_KEY = "API KEY" #Enter your openweathermap api key
OPEN_WEATHER_MAP_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

IPBASE_API_KEY = "API KEY" #Enter your IP Base api key
IPBASE_API_ENDPOINT = "https://api.ipbase.com/v2/info"

def get_weather():
    input_value = input_field.get()
    weather_query_params = {
        "q": input_value,
        "appid": OPEN_WEATHER_MAP_API_KEY,
        "units": "metric"
    }
    response = requests.get(OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()
    
    weather_label.config(text=f"{weather_data['name']}: {weather_data['main']['temp']}°C")
    weather_description.config(text=f"Description: {weather_data['weather'][0]['description']}")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} Kmph")


def get_location_weather():
    query_params = {
        "apiKey": IPBASE_API_KEY
    }
    response = requests.get(IPBASE_API_ENDPOINT, params=query_params)
    city_name = response.json()['data']['location']['city']['name']

    weather_query_params = {
        'q': city_name,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    weather_label.config(text=f"{weather_data['name']}: {weather_data['main']['temp']}°C")
    weather_description.config(text=f"Description: {weather_data['weather'][0]['description']}")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} Kmph")

root = Tk()
root.title("Weather Forecast")
root.geometry("400x200")

input_label = Label(root, text="Enter a City:")
input_label.pack()

input_field = Entry(root)
input_field.pack()

submit_button = Button(root, text="Get Weather", command=get_weather, bg="#E5E4E2")
submit_button.pack()

location_button = Button(root, text="Use Current Loacation", command=get_location_weather, bg="#E5E4E2")
location_button.pack()

weather_label = Label(root, text="")
weather_label.pack()

weather_description = Label(root, text="")
weather_description.pack()

humidity_label = Label(root, text="")
humidity_label.pack()

wind_speed_label = Label(root, text="")
wind_speed_label.pack()

root.mainloop()
