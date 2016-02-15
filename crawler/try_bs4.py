import requests
from bs4 import BeautifulSoup
res = requests.get("https://osu.ppy.sh/p/beatmaplist")
#print (res.text)
soup = BeautifulSoup(res.text, "html.parser")
#print (soup.contents)
for map in soup.select('.beatmap'):
	print (map.select('.artist')[0].text,map.select('.title')[0].text)