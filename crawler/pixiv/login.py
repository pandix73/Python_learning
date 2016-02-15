import requests
from bs4 import BeautifulSoup
payload = {
'mode':'login',
'return_to':'/',
'pixiv_id':'***',
'pass':'***',
'skip':'1'
}

res = requests.session()
res1 = res.post('https://www.secure.pixiv.net/login.php', data = payload)

soup = BeautifulSoup(res1.text, "html.parser")
print (soup.select('.user')[0].text)

res2 = res.get('http://www.pixiv.net/search.php?s_mode=s_tag&word=gumi&abt=y')
soup2 = BeautifulSoup(res2.text, "html.parser")
for image in soup2.select('.image-item'):
    soup3 = BeautifulSoup(str(list(image)[1]), "html.parser")
    for site in soup3.findAll('a'):
        print ('http://www.pixiv.net'+site.get('href'))