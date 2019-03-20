# Zeilen 2 - 7 sind aus einem Scraping Tutorial
from bs4 import BeautifulSoup
import requests
import json
import regex

url = 'https://daserste.ndr.de/annewill/archiv/index.html' #Sendungsarchiv von Anne Will
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


def extract(exp, string):
    result = regex.compile(exp).search(string)
    if result:
        return result.capturesdict()
    else:
        return None


for teaser in content.find_all('div', class_= "teaser"):

    teaser_text = teaser.get_text()

    result = extract(r"Mit ((?P<name>[^,]+), )+((?P<name>[^\.]+) und (als \w+ )?(?P<name>[^\.]+))\.",
             teaser_text)

    if result is None:
        raise ValueError(f"No names found in {teaser_text}")
    else:
        print(result)


