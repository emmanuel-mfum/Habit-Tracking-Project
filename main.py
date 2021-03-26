import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(".env")  # loads the environment file


USERNAME = os.getenv("USER")
TOKEN = os.getenv("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"



# MAKING AN ACCOUNT
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)  # sends the user_params as json
# print(response.text)  # gives the response as a piece of text


# CREATING A GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"  # endpoint for the graph creation

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)  These lines were use to create graph
# print(response.text)


# POST A PIXEL
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


# today = datetime(year=2020, month=12, day=25) custom date
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend reading today? "),

}

response = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_config)  # post a new pixel
print(response.text)


# UPDATING A PIXEL

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
updated_pixel = {
    "quantity": "3"
}

# response = requests.put(url=update_endpoint, headers=headers, json=updated_pixel)
# print(response.text)


# DELETING A PIXEL

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
# response = requests.delete(url=delete_endpoint,headers=headers)
