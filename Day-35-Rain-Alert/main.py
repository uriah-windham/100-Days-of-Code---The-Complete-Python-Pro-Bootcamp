import requests
from twilio.rest import Client

api_key = ""
account_sid = ""
auth_token = ""

location_parameters = {
    "q": "Moncton, Canada",
    "appid": "",
}

location = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=location_parameters)
location.raise_for_status()
location_data = location.json()
latitude = location_data[0]["lat"]
longitude = location_data[0]["lon"]

print(latitude, longitude)
print(location_data)

weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": "",
    "units": "imperial",
    "cnt": 4,
}

weather = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
weather.raise_for_status()
weather = weather.json()
print(weather["list"])

will_rain = False
for hour_data in weather["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="",
        to="",
        body="It's going to rain today! Remember to grab an ☂️",
    )
    print(message.status)