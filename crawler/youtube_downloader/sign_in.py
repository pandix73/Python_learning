import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.youtube.com/?gl=TW&hl=zh-TW')

soup = BeautifulSoup(res.text, 'html.parser')

print (soup.select('.yt-masthead-picker-name')[0].text)
print (soup.select('.yt-uix-button-content')[0].text)