# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
payload = {
'redirect':'/p/beatmaplist',
'sid':'',
'username':'paul7373',
'password':'49867515',
'login':'login'
}
head = {
'content-length':'80',
'content-type':'application/x-www-form-urlencoded',
'cookie':'last_login=paul7373; __cfduid=d1b1ca1f92e57c7195642d4fbda88faef1450192111; PHPSESSID=cc49700a15d9e9d7a637a6923c6c932e; phpbb3_2cjk5_u=2958680; phpbb3_2cjk5_k=; phpbb3_2cjk5_sid=b315d6b9c93451add1bd7e41ad8856db; __utma=226001156.2115263840.1450192110.1451320251.1451382912.8; __utmb=226001156.14.10.1451382912; __utmc=226001156; __utmz=226001156.1450192110.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _encid=%7B%22name%22%3A%22paul7373%22%2C%22email%22%3A%22%22%7D',
'origin':'https://osu.ppy.sh',
'referer':'https://osu.ppy.sh/p/beatmaplist',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}
res = requests.session()
res1 = res.post('https://osu.ppy.sh/forum/ucp.php?mode=login', data = payload, headers = head)
head2 = {
'cookie':'last_login=paul7373; __cfduid=d1b1ca1f92e57c7195642d4fbda88faef1450192111; PHPSESSID=cc49700a15d9e9d7a637a6923c6c932e; __utmt=1; _encid=%7B%22name%22%3A%22paul7373%22%2C%22email%22%3A%22%22%7D; __utma=226001156.2115263840.1450192110.1451320251.1451382912.8; __utmb=226001156.13.10.1451382912; __utmc=226001156; __utmz=226001156.1450192110.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); phpbb3_2cjk5_u=2958680; phpbb3_2cjk5_k=; phpbb3_2cjk5_sid=b315d6b9c93451add1bd7e41ad8856db',
'referer':'https://osu.ppy.sh/forum/',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}
res2 = res.get('https://osu.ppy.sh/forum/', headers = head2)
soup = BeautifulSoup(res2.text, "html.parser")
print (soup.select('.content-infoline')[0].text)