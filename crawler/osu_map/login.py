# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
payload = {
'redirect':'/p/beatmaplist',
'sid':'',
'username':'***',
'password':'***',
'login':'login'
}
head = {
'content-length':'80',
'content-type':'application/x-www-form-urlencoded',
'cookie':'***',
'origin':'https://osu.ppy.sh',
'referer':'https://osu.ppy.sh/p/beatmaplist',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}
res = requests.session()
res1 = res.post('https://osu.ppy.sh/forum/ucp.php?mode=login', data = payload, headers = head)

soup = BeautifulSoup(res1.text, "html.parser")
print (soup.select('.content-infoline')[0].text)