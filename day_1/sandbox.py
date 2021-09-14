# sandbox for breakout rooms 9/13/21

import requests
import json
from openpyxl import Workbook
from openpyxl.styles import Font

response = requests.get("https://data.messari.io/api/v2/assets")

# print(response)

# json.loads() - takes text string and converts it to dict (clean_data)
json_data = json.loads(response.text)

# grab only 'data' ( asset list) from json_data. 
assets = json_data['data']

# create workbook object
wb = Workbook()

# create output file
out_file = 'bitcoin.xlsx'

# grab 'active' sheet, whichever it is
sheet = wb.active
sheet.title = "Asset ROI Data"

# write column headers and set font style.
sheet['A1'] = "Asset"
sheet['A1'].font = Font(size="14", bold=True, italic=True)
sheet['B1'] = "ROI Data"
sheet['B1'].font = Font(size="14", bold=True, italic=True)


# create counter for row
row = 2

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

    # assign values to cells.
    sheet['A' + str(row)] = asset['symbol']
    sheet['B' + str(row)] = roi_data

    # increment to next row
    row += 1

# save .xlsx file
wb.save(out_file)




