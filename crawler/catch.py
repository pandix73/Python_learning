import requests
from bs4 import BeautifulSoup
url = 'http://www.moneydj.com/InfoSvc/apis/vc'
payload = '{"counts":[{"svc":"NV","guid":"a180a15b-9e4f-4575-b28f-927fcb5c63a3"}]}'
head = {'Content-Type': 'application/json'}
res = requests.post(url, data = payload, headers = head)
print (res.text)