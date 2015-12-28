import requests
from bs4 import BeautifulSoup
header = {
'content-type':'application/x-www-form-urlencoded',
'cookie':'__cfduid=d1b1ca1f92e57c7195642d4fbda88faef1450192111; last_login=paul7373; PHPSESSID=a55fc5800ee694e14d0267a9fe54e96a; __utmt=1; _encid=%7B%22name%22%3A%22paul7373%22%2C%22email%22%3A%22%22%7D; __utma=226001156.2115263840.1450192110.1451313107.1451320251.7; __utmb=226001156.13.10.1451320251; __utmc=226001156; __utmz=226001156.1450192110.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
'origin':'https://osu.ppy.sh',
'referer':'https://osu.ppy.sh/p/beatmaplist',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}
rs = requests.session()
res = rs.get('https://osu.ppy.sh/forum/ucp.php?mode=login?redirect=%2Fp%2Fbeatmaplist&sid=&username=paul7373&password=49867515&login=login', headers = header)
res2 = rs.get('https://osu.ppy.sh/p/beatmaplist?q=vocaloid&m=-1&r=0&g=0&la=0', headers = header)
bsres2 = BeautifulSoup(res.text, "html.parser")
print (bsres2.select('html')[0].text)
#print (bsres2.select('.artist')[0].text)