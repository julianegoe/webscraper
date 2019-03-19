from bs4 import BeautifulSoup
import requests
import json
url = 'https://daserste.ndr.de/annewill/archiv/index.html' #Sendungsarchiv von Anne Will
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

teaserli = []	
for element in content.find_all("p", class_= "teasertext"):
	for a_element in element.find_all("a"):
		teaserli.append(a_element.get_text())
		print(teaserli)

with open('willData.json', 'w') as outfile:
	json.dump(teaserli, outfile)