# ITP Week 4 Day 2 Exercise

#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/docs/v2

#PSEUDO-CODE:

# IMPORTS
import requests
import json
from openpyxl import Workbook
from openpyxl.styles import Font
from pprint import pprint

#GET NAME AND ABILITY FROM API
### api for name & ability ----->  https://pokeapi.co/api/v2/ability
url_ability = "https://pokeapi.co/api/v2/ability"

# execute call to poke api.
response = requests.get(url_ability)

# convert and save response into dict
json_data = json.loads(response.text)

# grab only 'results' item from json_data; 'results' is a list of dicts (results['name'] and results['url'])
results = json_data['results']

### TESTING - pretty print data set just to see what we're working with ###
pprint(results)


# create workbook/spreadsheet file.
wb = Workbook()

# create output file
outfile = "pokeapi.xlsx"









#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK