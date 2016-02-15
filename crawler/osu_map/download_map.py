import requests
from bs4 import BeautifulSoup

import wget
import os

payload = {
'redirect':'/p/beatmaplist',
'sid':'',
#'username':'*name*',
#'password':'*pswd*',
'login':'login'
}
head = {
'content-length':'80',
'content-type':'application/x-www-form-urlencoded',
#'cookie':'***',
# dont know whether it is effective
'origin':'https://osu.ppy.sh',
'referer':'https://osu.ppy.sh/p/beatmaplist',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}

from requests import session
with session() as c:
	c.post('https://osu.ppy.sh/forum/ucp.php?mode=login', data = payload, headers = head)
	res2 = c.get("https://osu.ppy.sh/p/beatmaplist")
	soup = BeautifulSoup(res2.text, "html.parser")
	print (soup.select('.content-infoline')[0].text) # check login or not
	
	for map in soup.select('.beatmap'):
		print (map.select('.title')[0].text,map.select('.artist')[0].text)
		path = "https://osu.ppy.sh/d/"+map.get('id')
		download = c.get(path)
		print (download.url)
		fold = r"C:\Users\pandix\Desktop\Python_learning\crawler\download\map_" # my path
		fold += map.get('title') + r".osz"
		
		wget.download(download.url, out = fold, bar=None)
		#os.system('python -m wget -o %s %s'%(fold, path))
