import requests
from bs4 import BeautifulSoup
payload = {
'mode':'login',
'return_to':'/',
'pixiv_id':'pandix',
'pass':'49867515',
'skip':'1'
}

res = requests.session()
res1 = res.post('https://www.secure.pixiv.net/login.php', data = payload)

soup = BeautifulSoup(res1.text, "html.parser")
print (soup.select('.user')[0].text)

res2 = res.get('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=55096369')
soup2 = BeautifulSoup(res2.text, "html.parser")
soup3 = BeautifulSoup(str(soup2.select('.wrapper')), "html.parser")
for site in soup3.findAll('img'):
	print (site.get('data-src'))
