# Import necessary libraries
import json
import requests
from bs4 import BeautifulSoup

# Set headers for HTTP requests:
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

# Set the English Wikipedia URL and the file path of the Persian HTML file:
en_url = '''https://wikipedia.lurkmore.com/wiki/List_of_cities_in_Iran_by_province?lang=en'''
fa_html_path = '''./persian.html'''

# Open the Persian HTML file and read its contents into a variable:
with open(fa_html_path, 'r') as f:
    fa_html = f.read()

# Send a GET request to the English Wikipedia page and store the HTML content in a variable:
result = requests.get(en_url, headers = headers)

# Use BeautifulSoup to parse the Persian and English HTML content:
fa_soup = BeautifulSoup(fa_html, 'html5lib')
en_soup = BeautifulSoup(result.content, 'html5lib')

# Find the h2 and table tags for each province on both Wikipedia pages and loop through them using zip:
fa_h2s = fa_soup.findAll('h2')[1:32]
en_h2s = en_soup.findAll('h2')[1:32]
fa_tables = fa_soup.findAll('table',class_="wikitable sortable")
en_tables = en_soup.findAll('table',class_="wikitable sortable")
mother = []
for en_table,en_h2,fa_table,fa_h2 in zip(en_tables,en_h2s,fa_tables,fa_h2s):
    # Create a dictionary for each province containing the province name in English and Persian, and a list of cities:
    daughter = {}
    en_province = en_h2.find('a',class_='mw-redirect').text.lower().replace(" ","-").replace("-province","")
    fa_province = fa_h2.find('a',class_='mw-redirect').text.replace("استان","").strip()
    daughter["province-en"] = en_province
    daughter["province-fa"] = fa_province
    # Loop through the rows of the table for each province and create a dictionary for each city containing the city name in English and Persian.
    # Append each city dictionary to the province's list of cities
    daughter["cities"] = []
    en_trs = en_table.findAll('tr')[1:]
    fa_trs = fa_table.findAll('tr')[1:]
    for en_tr,fa_tr in zip(en_trs,fa_trs):
        niece = {}
        en_city = en_tr.find('a').text.lower().replace(" ","-")
        fa_city = fa_tr.find('a').text.strip()
        niece["city-en"] = en_city
        niece["city-fa"] = fa_city
        daughter["cities"].append(niece)
    mother.append(daughter)

## print(mother)

# Save result
with open('province_city.json','w') as f:
    f.write(json.dumps(mother)) 



# # Check which persian city's name still in english
# all_cities = []
# for province in mother:
#     cities = province["cities"]
#     for city in cities:
#         all_cities.append(city["city-fa"])
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# list_alphabet = list(alphabet)

# for city in all_cities:
#     list_city = list(city)
#     for character in list_city:
#         if character in list_alphabet:
#             print(city)
#             break

# Author: amyrmahdy
# Date: 3 March 2023


