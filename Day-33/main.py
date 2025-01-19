import requests
from datetime import datetime
import smtplib
MY_LAT = 0#MY LATITUDE
MY_L0NG = 0#MY LONGITUDE
MY_EMAIL = ""
MY_PASSWORD = ""

#Your position is with +5 and -5 degrees of ISS position
def check_proximity(my_lat, my_long, iss_lat, iss_long):
    if iss_lat - 5 <= my_lat <= iss_lat + 5 and iss_long - 5 <= my_long <= iss_long + 5:
        return True
    else:
        return False

#Check if it is currently nighttime
def check_is_night(current_hour, current_min, my_sunrise_hour, my_sunrise_min, my_sunset_hour, my_sunset_min):
    if (my_sunset_hour < current_hour and my_sunset_min < current_min) or (my_sunrise_hour > current_hour and my_sunrise_min > current_min):
        return True
    else:
        return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
iss_location = (iss_latitude, iss_longitude)
print(iss_location)



parameters = {
    "lat": MY_LAT,
    "lng": MY_L0NG,
    "formatted": 0,
    "tzid": "America/Chicago",
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
print(sunrise)
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunrise_min = int(sunrise.split("T")[1].split(":")[1])
print(f"Sunrise: {sunrise_hour}:{sunrise_min}")

sunset = data["results"]["sunset"]
print(sunset)
sunset_hour = int(sunset.split("T")[1].split(":")[0])
sunset_min = int(sunset.split("T")[1].split(":")[1])
print(f"Sunset: {sunset_hour}:{sunset_min}")

my_time = datetime.now()
my_hour = my_time.hour
my_minute = my_time.minute
print(f"My Time: {my_hour}:{my_minute}")

#If the ISS is close to my current position
iss_in_range = check_proximity(MY_LAT, MY_L0NG, iss_latitude, iss_longitude)
print(iss_in_range)
# and it is currently dark
is_night = check_is_night(my_hour, my_minute, sunrise_hour, sunrise_min, sunset_hour, sunset_min)
print(is_night)
# Then send me an email to tell me to look up
if iss_in_range and is_night:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg="Subject: ISS Nearby!\n\nLook outside! The ISS is currently passing above you!"
        )
# BONUS: Run to code every 60 seconds