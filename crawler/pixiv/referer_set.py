import requests
import wget
import os
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
path = 'http://i2.pixiv.net/img-original/img/2016/02/14/19/57/47/55284197_p0.jpg'
fold = r"C:\Users\pandix\Desktop\Python_learning\crawler\pixiv\download"
r = requests.get(path)
print (len(r.content))
#wget.download(path, out = fold, headers = header)
os.system('python -m wget --referer="http://www.pixiv.net/member_illust.php?mode=medium&illust_id=55284197'-o %s %s'%(fold, path))
wget --referer='http://www.pixiv.net/member_illust.php?mode=medium&illust_id=55284197' -P Desktop http://i2.pixiv.net/img-original/img/2016/02/14/19/57/47/55284197_p0.jpg