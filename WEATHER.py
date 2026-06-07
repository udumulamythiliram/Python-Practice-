import requests
import sys

city = input("Enter city name:")

API_KEY = "Your_api_key_here" 

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()


if data["cod"] != 200:
    sys.exit("City not found!")


Temperature = data["main"]["temp"]
Feels_like = data["main"]["feels_like"]
Humidity = data["main"]["humidity"]
Description = data["weather"][0]["description"]
City_name = data["name"]
Country  = data["sys"]["country"]
Wind_speed = data["wind"]["speed"]

print(f"Weather in {City_name} , {Country}")
print(f"Temperature:{Temperature}C")
print(f"Feels like:{Feels_like}")
print(f"Humidity:{Humidity}%")
print(f"Description:{Description}")
print(f"Wind_speed:{Wind_speed}m/s")


if Temperature >= 35:
    print("Very hot outside , avoide heavy and dark colored cloths")
elif Temperature >= 25:
    print("Warm outside , wear light cotton cloths")
elif Temperature >= 15:
    print("Mild outside , can go out with anything")
elif Temperature <15:
    print("Cold Outside , Suggested to wear a jacket")


if "rain" in Description:
    print("Rainy outside , Umbrella needed")
