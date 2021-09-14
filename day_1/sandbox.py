# sandbox for breakout rooms


import os
import requests
import json
import openpyxl
import pprint

response = requests.get("https://data.messari.io/api/v2/assets")

# print(response)

# json.loads() - takes text string and converts it to dict (clean_data)
clean_data = json.loads(response.text)
print(clean_data["data"][0]["symbol"])

#pprint.pprint(clean_data)

