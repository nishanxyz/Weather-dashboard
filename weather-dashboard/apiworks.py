from urllib.request import urlopen
import json

import time

curr_time = time.strftime("%Y-%m-%dT%H:00")


def forecast(location):
  url = "https://api.open-meteo.com/v1/forecast?latitude="+str(location[0])+"&longitude="+str(location[1])+"&hourly=temperature_2m,wind_speed_10m,rain,relative_humidity_2m,visibility&forecast_days=1"
  # print(url)
  with urlopen(url) as request:
    source = request.read()
  
  data = json.loads(source)

  print(f"Time: {curr_time}")
  index = data["hourly"]["time"].index(curr_time)

  print(f"Temp: {data["hourly"]["temperature_2m"][index]}°C")
  print(f"Wind Speed: {data["hourly"]["wind_speed_10m"][index]}km/h")
  print(f"Rain: {data["hourly"]["rain"][index]}mm")
  print(f"Relative Humidity: {data["hourly"]["relative_humidity_2m"][index]}%")
  print(f"Visibility: {data["hourly"]["visibility"][index]}m")



