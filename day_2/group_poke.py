# ITP Week 4 Day 2 Exercise

#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/api/v2/pokemon

#PSEUDO-CODE:

#GET NAME AND ABILITY FROM API
#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK

#imports:
    #json
    #openpyxl
import os
import string
from openpyxl import Workbook
from openpyxl.styles import Font
import json
import requests
from pprint import pprint

# clear output screen before each run.
os.system('clear')


#Input
    #json file from pokemon api
    #workbook
    # https://pokeapi.co/api/v2/pokemon
    # https://pokeapi.co/api/v2/pokemon/1/

# create dictionary to hold character name and list of abilities
# =>  eg: 'tentacool': ['clear-body', 'liquid-ooze', 'rain-dish']
poke_abilities = {}

# loop through any # number of characters. First 100 characters chosen
# for this example test.
for num in range(100):
    url = f"https://pokeapi.co/api/v2/pokemon/{num+1}/"   
    response = requests.get(url)
    json_data = json.loads(response.text)
    name = json_data['forms'][0]['name'] # only one element in 'forms', so '0' hardcode
    poke_abilities[name] = []

    abilities = json_data['abilities'] # list of abilities(dicts) for current name/poke character.
    for ability in abilities:
        poke_abilities[name].append(ability['ability']['name'])
    
# "pretty-print" abilities dictionary.
pprint(poke_abilities) 
    

# write data to spreadsheet/workbook.
wb = Workbook() # create workbook
outfile = "pokemon.xlsx"  # specify output file
sheet = wb.active  # assign active sheet to 'sheet' obj
sheet.title = "Pokemon Abilities"

# write column headers and set font properties.
sheet['A1'] = "Character"
sheet['A1'].font = Font(size="14", bold=True, italic=True, underline="single")
sheet['B1'] = "Abilities"
sheet['B1'].font = Font(size="14", bold=True, italic=True, underline="single")

# TEST write to workbook
# sheet['A2'] = "dodrio"
# sheet.write('B2', ', '.join(poke_abilities['dodrio']))


# OPTION #1:  print 'name' in column A and entire list of abilities in column B.
# loop through poke_abilities dict and write: 1) character name and 2) list of abilities
row_num = 2
for char_name in sorted(poke_abilities.keys()):
    sheet['A' + str(row_num)] = char_name.capitalize()
    sheet['B' + str(row_num)] = ', '.join(poke_abilities[char_name])
    row_num += 1

# save workbook/spreadsheet
wb.save(outfile)





############## poke_abilities dictionary of first 100 poke characters ################
#  100 Characters and their list of abilities
# {
# 'abra': ['synchronize', 'inner-focus', 'magic-guard'],
#  'alakazam': ['synchronize', 'inner-focus', 'magic-guard'],
#  'arbok': ['intimidate', 'shed-skin', 'unnerve'],
#  'arcanine': ['intimidate', 'flash-fire', 'justified'],
#  'beedrill': ['swarm', 'sniper'],
#  'bellsprout': ['chlorophyll', 'gluttony'],
#  'blastoise': ['torrent', 'rain-dish'],
#  'bulbasaur': ['overgrow', 'chlorophyll'],
#  'butterfree': ['compound-eyes', 'tinted-lens'],
#  'caterpie': ['shield-dust', 'run-away'],
#  'charizard': ['blaze', 'solar-power'],
#  'charmander': ['blaze', 'solar-power'],
#  'charmeleon': ['blaze', 'solar-power'],
#  'clefable': ['cute-charm', 'magic-guard', 'unaware'],
#  'clefairy': ['cute-charm', 'magic-guard', 'friend-guard'],
#  'cloyster': ['shell-armor', 'skill-link', 'overcoat'],
#  'dewgong': ['thick-fat', 'hydration', 'ice-body'],
#  'diglett': ['sand-veil', 'arena-trap', 'sand-force'],
#  'dodrio': ['run-away', 'early-bird', 'tangled-feet'],
#  'doduo': ['run-away', 'early-bird', 'tangled-feet'],
#  'drowzee': ['insomnia', 'forewarn', 'inner-focus'],
#  'dugtrio': ['sand-veil', 'arena-trap', 'sand-force'],
#  'ekans': ['intimidate', 'shed-skin', 'unnerve'],
#  'farfetchd': ['keen-eye', 'inner-focus', 'defiant'],
#  'fearow': ['keen-eye', 'sniper'],
#  'gastly': ['levitate'],
#  'gengar': ['cursed-body'],
#  'geodude': ['rock-head', 'sturdy', 'sand-veil'],
#  'gloom': ['chlorophyll', 'stench'],
#  'golbat': ['inner-focus', 'infiltrator'],
#  'golduck': ['damp', 'cloud-nine', 'swift-swim'],
#  'golem': ['rock-head', 'sturdy', 'sand-veil'],
#  'graveler': ['rock-head', 'sturdy', 'sand-veil'],
#  'grimer': ['stench', 'sticky-hold', 'poison-touch'],
#  'growlithe': ['intimidate', 'flash-fire', 'justified'],
#  'haunter': ['levitate'],
#  'hypno': ['insomnia', 'forewarn', 'inner-focus'],
#  'ivysaur': ['overgrow', 'chlorophyll'],
#  'jigglypuff': ['cute-charm', 'competitive', 'friend-guard'],
#  'kadabra': ['synchronize', 'inner-focus', 'magic-guard'],
#  'kakuna': ['shed-skin'],
#  'kingler': ['hyper-cutter', 'shell-armor', 'sheer-force'],
#  'krabby': ['hyper-cutter', 'shell-armor', 'sheer-force'],
#  'machamp': ['guts', 'no-guard', 'steadfast'],
#  'machoke': ['guts', 'no-guard', 'steadfast'],
#  'machop': ['guts', 'no-guard', 'steadfast'],
#  'magnemite': ['magnet-pull', 'sturdy', 'analytic'],
#  'magneton': ['magnet-pull', 'sturdy', 'analytic'],
#  'mankey': ['vital-spirit', 'anger-point', 'defiant'],
#  'meowth': ['pickup', 'technician', 'unnerve'],
#  'metapod': ['shed-skin'],
#  'muk': ['stench', 'sticky-hold', 'poison-touch'],
#  'nidoking': ['poison-point', 'rivalry', 'sheer-force'],
#  'nidoqueen': ['poison-point', 'rivalry', 'sheer-force'],
#  'nidoran-f': ['poison-point', 'rivalry', 'hustle'],
#  'nidoran-m': ['poison-point', 'rivalry', 'hustle'],
#  'nidorina': ['poison-point', 'rivalry', 'hustle'],
#  'nidorino': ['poison-point', 'rivalry', 'hustle'],
#  'ninetales': ['flash-fire', 'drought'],
#  'oddish': ['chlorophyll', 'run-away'],
#  'onix': ['rock-head', 'sturdy', 'weak-armor'],
#  'paras': ['effect-spore', 'dry-skin', 'damp'],
#  'parasect': ['effect-spore', 'dry-skin', 'damp'],
#  'persian': ['limber', 'technician', 'unnerve'],
#  'pidgeot': ['keen-eye', 'tangled-feet', 'big-pecks'],
#  'pidgeotto': ['keen-eye', 'tangled-feet', 'big-pecks'],
#  'pidgey': ['keen-eye', 'tangled-feet', 'big-pecks'],
#  'pikachu': ['static', 'lightning-rod'],
#  'poliwag': ['water-absorb', 'damp', 'swift-swim'],
#  'poliwhirl': ['water-absorb', 'damp', 'swift-swim'],
#  'poliwrath': ['water-absorb', 'damp', 'swift-swim'],
#  'ponyta': ['run-away', 'flash-fire', 'flame-body'],
#  'primeape': ['vital-spirit', 'anger-point', 'defiant'],
#  'psyduck': ['damp', 'cloud-nine', 'swift-swim'],
#  'raichu': ['static', 'lightning-rod'],
#  'rapidash': ['run-away', 'flash-fire', 'flame-body'],
#  'raticate': ['run-away', 'guts', 'hustle'],
#  'rattata': ['run-away', 'guts', 'hustle'],
#  'sandshrew': ['sand-veil', 'sand-rush'],
#  'sandslash': ['sand-veil', 'sand-rush'],
#  'seel': ['thick-fat', 'hydration', 'ice-body'],
#  'shellder': ['shell-armor', 'skill-link', 'overcoat'],
#  'slowbro': ['oblivious', 'own-tempo', 'regenerator'],
#  'slowpoke': ['oblivious', 'own-tempo', 'regenerator'],
#  'spearow': ['keen-eye', 'sniper'],
#  'squirtle': ['torrent', 'rain-dish'],
#  'tentacool': ['clear-body', 'liquid-ooze', 'rain-dish'],
#  'tentacruel': ['clear-body', 'liquid-ooze', 'rain-dish'],
#  'venomoth': ['shield-dust', 'tinted-lens', 'wonder-skin'],
#  'venonat': ['compound-eyes', 'tinted-lens', 'run-away'],
#  'venusaur': ['overgrow', 'chlorophyll'],
#  'victreebel': ['chlorophyll', 'gluttony'],
#  'vileplume': ['chlorophyll', 'effect-spore'],
#  'voltorb': ['soundproof', 'static', 'aftermath'],
#  'vulpix': ['flash-fire', 'drought'],
#  'wartortle': ['torrent', 'rain-dish'],
#  'weedle': ['shield-dust', 'run-away'],
#  'weepinbell': ['chlorophyll', 'gluttony'],
#  'wigglytuff': ['cute-charm', 'competitive', 'frisk'],
#  'zubat': ['inner-focus', 'infiltrator']
# }






###################### pseudo-code from lecture (Tyler) #####################

#Assign response to variable

#Create workbook
    #get workbook from openpy
    #load workbook
    #assign workbook to variable
    
#Create Worksheet
    #assign sheet to variable

#Create a dictionary, assign to variable

#FUNCTION BODY
    #Convert response to json file
        #clean data(response)
            #json.loads(response.text)

    #Iterate over response
        #for each pokemon in response
            #variable key = pokemon.name
            #variable value = pokemon.abilites
            #append {key/value} pair to dictionary

    #Iterate over dictionary
        #for each item in dictionary
            #assign dictionary values to rows & cols
                #Write Name to Cell
                #Write Abilities to Cell

#Output
    #Workbook

# pokemon = {
#     bulbasour : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     },
#     pikachu : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     }
# }