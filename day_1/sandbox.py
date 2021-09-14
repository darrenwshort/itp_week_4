# sandbox for breakout rooms


import os
import requests
import json
import openpyxl
import pprint

response = requests.get("https://data.messari.io/api/v2/assets")

# print(response)

# json.loads() - takes text string and converts it to dict (clean_data)
json_data = json.loads(response.text)

# grab only 'data' ( asset list) from json_data. 
assets = json_data['data']
# for a in assets:
#     print(a['symbol'])


# loop through asset list and retrieve 
for asset in assets:
 
    url = f"https://data.messari.io/api/v1/assets/{asset['symbol'].lower()}/metrics"
    response_asset = requests.get(url)
    json_asset = json.loads(response_asset.text)

    # try-except - some assets don't have ROI data.  Assign 'N/A' if so.
    try:
        roi_data = json_asset['data']['roi_data']['percent_change_last_1_week']
    except:
        roi_data = "N/A"

    print(f"{asset['symbol'].lower()}: {roi_data}")


# get list of all symbols in data list



# print(type(data))
# print(data)





