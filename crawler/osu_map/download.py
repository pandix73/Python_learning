import wget
import os
import requests
from bs4 import BeautifulSoup
path = "https://m1.ppy.sh/r/osu!install.exe"
fold = r"C:\Users\pandix\Desktop\Python_learning\crawler\download"
os.system('python -m wget -o %s %s'%(fold, path))
#wget.download(path, out = fold, bar=None)