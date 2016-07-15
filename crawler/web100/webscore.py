# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
payload = {
'score':'90',
'HW':'03162',
'ID':'s100062272'
}
head = {
'Authorization':'Basic czEwMzA2MjEzNToxMDMwNjIxMzU=',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'web.2y.idv.tw',
'Origin':'http://web.2y.idv.tw',
'Referer':'http://web.2y.idv.tw/score/scoreform.cgi?ID=s100062272&HW=03161',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}
res = requests.session()
res1 = res.post('http://web.2y.idv.tw/score/frame.html', data = payload, headers = head)
