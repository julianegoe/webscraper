# Zeilen 2 - 7 sind aus einem Scraping Tutorial
from bs4 import BeautifulSoup
import requests
import json
url = 'https://daserste.ndr.de/annewill/archiv/index.html' #Sendungsarchiv von Anne Will
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#jetzt folgen verschiedene Ideen wie ich an den Text komme. In den <div> mit der Class "Teaser" sind <p> mit der Class "teasertext". 
#Dort stecken die Gäste in einem <a> drin. Die <a> haben aber keine Class, sondern nur einen Link href und einen title.


#Hier tu ich den Inhalte eines jeden <div class="teaser"> in eine Liste, 
#loope da durch und gucke, was davon den <a> tag hat. Klappt aber überhaupt nicht die Idee. 
#teaser = content.find_all('div', class_= "teaser") 
#teaserli = []
#for x in teaser:
#	teaserli.append(x)
	#print(teaserli)
#for y in teaserli:
#	if y == "a":
		#print(y)


#hier bekomme ich zwar nur den Text aber neun mal den gleichen der ersten Gäste.

gast = content.find_all('div', class_= "teaser")
for x in gast: 
	x = content.find('p', class_= "teasertext").get_text()
	print(x)