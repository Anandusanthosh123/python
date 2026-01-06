import requests

API_KEY = "YOURE_API-KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q":city,"appid":API_KEY,"units":"metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
  
    
    if data.get("cod") != 200:
        print("City not Found!")
        return
    else:
         print(f"\nWeather in {city}:")
         print(f"Temperature: {data['main']['temp']}°C ")
         print(f"Condition: {data['weather'][0]['description'].title()}")
         print(f"Humidity: {data['main']['humidity']}%")
         print(f"Wind Speed: {data['wind']['speed']} m/s")
    
city = input("Enter city name: ")
get_weather(city)    
