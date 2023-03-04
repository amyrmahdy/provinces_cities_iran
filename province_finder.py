import json
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

en_url = '''https://wikipedia.lurkmore.com/wiki/List_of_cities_in_Iran_by_province?lang=en'''

fa_html_path = '''./persian.html'''

with open(fa_html_path, 'r') as f:
    fa_html = f.read()


result = requests.get(en_url, headers = headers)


fa_soup = BeautifulSoup(fa_html, 'html5lib')
fa_h2s = fa_soup.findAll('h2')[1:32]
fa_tables = fa_soup.findAll('table',class_="wikitable sortable")


en_soup = BeautifulSoup(result.content, 'html5lib')
en_h2s = en_soup.findAll('h2')[1:32]
en_tables = en_soup.findAll('table',class_="wikitable sortable")


mother = []
for en_table,en_h2,fa_table,fa_h2 in zip(en_tables,en_h2s,fa_tables,fa_h2s):
    daughter = {}
    en_province = en_h2.find('a',class_='mw-redirect').text.lower().replace(" ","-").replace("-province","")
    fa_province = fa_h2.find('a',class_='mw-redirect').text.replace("استان","").strip()
    daughter["province-en"] = en_province
    daughter["province-fa"] = fa_province

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

# print(mother)
with open('province_city.json','w') as f:
    f.write(json.dumps(mother)) 



# Check which persian city's name still in english
all_cities = []
for province in mother:
    cities = province["cities"]
    for city in cities:
        all_cities.append(city["city-fa"])
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_alphabet = list(alphabet)

for city in all_cities:
    list_city = list(city)
    for character in list_city:
        if character in list_alphabet:
            print(city)
            break

# Author: amyrmahdy
# Date: 3 March 2023