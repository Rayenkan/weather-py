import requests
from geopy.geocoders import Nominatim

ch=input("give a country :")
geolocator = Nominatim(user_agent="my_geocoding_app")
location = geolocator.geocode(ch)
lat=location.latitude
lon=location.longitude
print(location)
result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=4a878ed39f73fffe6591a2aa5da230d2")
details=result.json()

print("the weather in ",ch," is ",str(details["weather"][0]["description"])," the temperature is " ,round(details["main"]["temp"]-273.15) ," and the humidity is ",str(details["main"]["humidity"]),"% and the wind speed is ", str(details["wind"]["speed"]),"Km/H ")
