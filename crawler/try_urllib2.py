import requests
content = requests.get("https://osu.ppy.sh/d/368312")
print (content.url)