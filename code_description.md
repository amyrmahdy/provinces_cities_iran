# Overview

This code is a Python script that scrapes data from two Wikipedia pages: one in English and the other in Persian, and generates a JSON file that contains a list of Iranian provinces and their corresponding cities. The script uses the requests library to make HTTP requests to the English Wikipedia page, and the BeautifulSoup library to parse the HTML content of the pages.

The script starts by defining a headers dictionary which contains some HTTP headers to be sent with the requests, and two variables that hold the URLs of the English and Persian Wikipedia pages. The script then reads the HTML content of the Persian page from a local file, since the Persian Wikipedia is blocked in some countries.

The script then sends an HTTP GET request to the English Wikipedia page using the requests library, and parses the HTML content of both pages using the BeautifulSoup library. It extracts the province names and the city names from the HTML tables using BeautifulSoup's find() and findAll() methods, and stores them in a list of dictionaries.

Finally, the script writes the list of dictionaries to a JSON file called "province_city.json". It also includes a small piece of code at the end that checks if any Persian city names contain English characters, which may indicate that the Persian name was not available or accurate in the Wikipedia page.

Overall, this script can be useful for developers who need a list of Iranian provinces and cities for their applications or websites.

<br >

<br >

# Step by Step

## 1 - Import necessary libraries:

```
import json

import requests

from bs4 import BeautifulSoup
```

## 2 - Set headers for HTTP requests:

```
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
```

## 3 - Set the English Wikipedia URL and the file path of the Persian HTML file:

```
en_url = '''https://wikipedia.lurkmore.com/wiki/List_of_cities_in_Iran_by_province?lang=en'''
fa_html_path = '''./persian.html'''
```

## 4 - Open the Persian HTML file and read its contents into a variable:

```
with open(fa_html_path, 'r') as f:
    fa_html = f.read()

```

## 5 - Send a GET request to the English Wikipedia page and store the HTML content in a variable:

```
result = requests.get(en_url, headers = headers)
```

## 6 - Use BeautifulSoup to parse the Persian and English HTML content:


```
fa_soup = BeautifulSoup(fa_html, 'html5lib')
en_soup = BeautifulSoup(result.content, 'html5lib')
```

## 7 - Find the h2 and table tags for each province on both Wikipedia pages and loop through them using zip:

```
fa_h2s = fa_soup.findAll('h2')[1:32]
en_h2s = en_soup.findAll('h2')[1:32]
fa_tables = fa_soup.findAll('table',class_="wikitable sortable")
en_tables = en_soup.findAll('table',class_="wikitable sortable")
for en_table,en_h2,fa_table,fa_h2 in zip(en_tables,en_h2s,fa_tables,fa_h2s):
```

## 8 - Create a dictionary for each province containing the province name in English and Persian, and a list of cities:

```
    daughter = {}
    en_province = en_h2.find('a',class_='mw-redirect').text.lower().replace(" ","-").replace("-province","")
    fa_province = fa_h2.find('a',class_='mw-redirect').text.replace("استان","").strip()
    daughter["province-en"] = en_province
    daughter["province-fa"] = fa_province
    daughter["cities"] = []
```

## 9 - Loop through the rows of the table for each province and create a dictionary for each city containing the city name in English and Persian. Append each city dictionary to the province's list of cities:

```
    en_trs = en_table.findAll('tr')[1:]
    fa_trs = fa_table.findAll('tr')[1:]
    for en_tr,fa_tr in zip(en_trs,fa_trs):
        niece = {}
        en_city = en_tr.find('a').text.lower().replace(" ","-")
        fa_city = fa_tr

```