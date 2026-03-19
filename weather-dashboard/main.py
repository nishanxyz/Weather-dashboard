from urllib.request import urlopen
import json
from apiworks import forecast

def city_to_latlong(city):

    url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city +"&count=1"
    with urlopen(url) as response:
        source = response.read()
    datas = json.loads(source)
    location = [datas["results"][0]["latitude"], datas["results"][0]["longitude"]]
    return location


print("----Welcome to Nishan's Weather Dashboard CLI-----\n")

print("Please enter one of the search options.")
print("1. Enter latitude and longitude of the city.")
print("2. Enter name of the city.(only limited to Nepal)\n")

choice = int(input(" ").strip())

if choice == 1:
    lat = float(input("Enter the latitude: ").strip())
    longi = float(input("Enter the longitude: ").strip())
    location = [lat, longi]
    forecast(location)
elif choice ==2:
    city = input("Enter the name of the city: ").strip()
    location = city_to_latlong(city)
    forecast(location)
else:
    print("INVALID CHOICE")


    




