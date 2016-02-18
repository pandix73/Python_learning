#!/usr/bin/python 
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import wget
import os
pixiv_id = input("pixiv_id:")
password = input("password:")
payload = {
'mode':'login',
'return_to':'/',
'pixiv_id':pixiv_id,
'pass':password,
'skip':'1'
}

header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
'Referer':'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=55284197',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
'Cookie':'p_ab_id=7; PHPSESSID=5470314_a939a14347556289740a8c48bffea8a9; module_orders_mypage=%5B%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; __utmt=1; __utma=235335808.1978129076.1448521378.1455630532.1455639120.39; __utmb=235335808.12.10.1455639120; __utmc=235335808; __utmz=235335808.1453317778.31.19.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/qH70FNBY1Q; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=5470314=1; _ga=GA1.2.1978129076.1448521378',
'If-Modified-Since':'Sun, 14 Feb 2016 10:57:47 GMT'
}

res = requests.session()
res1 = res.post('https://www.secure.pixiv.net/login.php', data = payload)

soup = BeautifulSoup(res1.text, "html.parser")
print ('login success' if str(soup.select('.user')[0].text) == pixiv_id else 'login fail')
keyword = ("Puzzle&Dragons")

#give up keyword input because can not deal with japanese code page

star = input('stars more than:')

check_page = res.get('http://www.pixiv.net/search.php?s_mode=s_tag_full&word='+keyword.replace('&', '%26')+'&abt=y')
cp_soup = BeautifulSoup(check_page.text, "html.parser")
total_page = int(int(str(cp_soup.select('.count-badge')[0].text)[0:-1]) / 20)+2
total_page = 1001 if total_page > 1001 else total_page
for page in range(1, total_page):
	res2 = res.get('http://www.pixiv.net/search.php?s_mode=s_tag_full&word='+keyword+'&abt=y&p='+str(page))
	soup2 = BeautifulSoup(res2.text, "html.parser")
	for image in soup2.select('.image-item'):
		if len(list(image)) > 3:
			soup3 = BeautifulSoup(str(list(image)[3]), "html.parser")
			if int(soup3.text) > int(star):
				print (int(soup3.text))
				soup4 = BeautifulSoup(str(list(image)[1]), "html.parser")
				for site in soup4.findAll('a'):
					page_url = 'http://www.pixiv.net'+site.get('href')
					print (page_url)
					get_image = res.get(page_url)
					soup_image = BeautifulSoup(get_image.text, "html.parser")
					soup_url = BeautifulSoup(str(soup_image.select('.wrapper')), "html.parser")
					for url in soup_url.findAll('img'):
						fold = r"C:\Users\pandix\Desktop\Python_learning\crawler\pixiv\download\pixiv_"
						#chose path 
						fold += keyword.replace('&', '_and_')+'_'+star
						os.system('wget --referer="%s" -P %s %s'%(page_url ,fold, url.get('data-src')))
			