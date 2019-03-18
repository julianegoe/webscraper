# webscraper
This a webscraper to get all guests of the talk show Anne Will. It's a work in progess and doesn't work yet. For now the rest is in German:

# Website
https://daserste.ndr.de/annewill/archiv/index.html

Es folgen verschiedene Ideen wie ich an den Text der Gäste komme. In den <div> mit der Class "teaser" sind <p> mit der Class "teasertext". Dort stecken die Gäste in einem <a> drin. Die <a> haben aber keine Class, sondern nur einen Link href und einen title.

# Idee 1
Hier füge ich den Inhalte eines jeden <div class="teaser"> einer Liste hinzu, 
loope da durch und gucke, was davon den <a> tag hat. Klappt aber überhaupt nicht die Idee. 

```python
teaser = content.find_all('div', class_= "teaser") 
teaserli = []
for x in teaser:
	teaserli.append(x)
	print(teaserli)
for y in teaserli:
	if y == "a":
		print(y)
```

# Idee 2
Hier bekomme ich zwar nur den Text aber neun mal den gleichen der ersten Gäste.

python```
gast = content.find_all('div', class_= "teaser")
for x in gast: 
	x = content.find('p', class_= "teasertext").get_text()
	print(x)
```
