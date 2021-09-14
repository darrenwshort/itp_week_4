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
sheet['A1'].font = Font(size="14", bold=True, italic=True, underline="single")
sheet['B1'] = "ROI Data"
sheet['B1'].font = Font(size="14", bold=True, italic=True, underline="single")


# create counter for row
row = 2

# loop through asset list and retrieve - 'asset' is asset symbol (string)
for asset in assets:
 
    # build url for subsequent request per each asset.
    url = f"https://data.messari.io/api/v1/assets/{asset['symbol'].lower()}/metrics"

    # get response based on url.
    response_asset = requests.get(url)

    # load json from response str.
    json_asset = json.loads(response_asset.text)

    # try-except - some assets don't have ROI data.  If so, assign default of 'N/A' to 'roi_data'.
    try:
        roi_data = json_asset['data']['roi_data']['percent_change_last_1_week']
    except:
        roi_data = "N/A"

    # assign values to cells.
    sheet['A' + str(row)] = asset['symbol']
    sheet['B' + str(row)] = roi_data

    # increment to process next row.
    row += 1

# save .xlsx file
wb.save(out_file)




