import requests
res = requests.get("https://www.google.com.tw/?gws_rd=ssl")
print (res.text)