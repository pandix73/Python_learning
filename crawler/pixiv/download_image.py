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
res = requests.session()
res1 = res.post('https://www.pixiv.net/login.php', data = payload)

soup = BeautifulSoup(res1.text, "html.parser")
print (str(soup.select(".user")[0].text))
#print ('login success' if str(soup.select('.user')[0].text) == pixiv_id else 'login fail')
keyword = ("C.C.")

#give up keyword input because can not deal with japanese code page

star = input('stars more than:')

check_page = res.get('http://www.pixiv.net/search.php?s_mode=s_tag_full&word='+keyword.replace('&', '%26')+'&abt=y')
cp_soup = BeautifulSoup(check_page.text, "html.parser")
total_page = int(int(str(cp_soup.select('.count-badge')[0].text)[0:-1]) / 20)+2
total_page = 1001 if total_page > 1001 else total_page
print (total_page)
for page in range(1, total_page):
	res2 = res.get('http://www.pixiv.net/search.php?s_mode=s_tag_full&word='+keyword+'&abt=y&p='+str(page))
	soup2 = BeautifulSoup(res2.text, "html.parser")
	for image in soup2.select('.autopagerize_page_element')[0].select('.image-item'):
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