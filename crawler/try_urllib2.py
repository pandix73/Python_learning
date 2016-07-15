import urllib.request
path = 'http://i2.pixiv.net/img-original/img/2016/02/14/19/57/47/55284197_p0.jpg'
fold = r"C:\Users\pandix\Desktop\Python_learning\crawler\pixiv\download"
req = urllib.Request(path)
req.add_header('Referer', 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=55284197')
r = urllib2.urlopen(req)