import requests
import datetime as dt
import json
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_KEY = os.getenv("TOKEN")

#Gets my current date and time and converts it into a readable format
my_now = dt.datetime.now()
my_date = my_now.date().strftime("%m/%d/%Y")
my_time = my_now.time().strftime("%H:%M:%S")

user_input = input("Tell me which exercises you did? ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": user_input,
    "weight_kg": 75,
    "height_cm": 170,
    "age": 25,
}

#Gets the needed data from nutritionix
response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_parameters)
print(response.status_code)
response.raise_for_status()
response_string = response.text
data = json.loads(response_string) #converts the data into a json format to keep the program from crashing

sheety_endpoint = os.getenv("SHEET_ENDPOINT")
sheety_headers = {
    "Authorization": BEARER_KEY
}

#Parameters for sheety, to add rows to my google sheets. The data needs to be nested within the "workout" dict which is
#the same name as my Sheety sheet, in order for Sheety to correctly read the data
sheety_parameters = {
    "workout": {
        "date": str(my_date),
        "time": str(my_time),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
sheety_response.raise_for_status()