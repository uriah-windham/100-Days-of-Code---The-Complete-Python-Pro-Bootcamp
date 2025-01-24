import requests
from datetime import datetime

USERNAME = "uwindham"
TOKEN = ""
GRAPH_ID = "graph1"

now = datetime.now()
my_time = now.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": my_time,
    "quantity": "30",
}

# response = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_config)
# print(response.text)

update_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{my_time}"
pixel_update = {
    "quantity": "120"
}

# response = requests.put(url=update_pixel_endpoint, headers=headers, json=pixel_update)
# print(response.text)

delete_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{my_time}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)