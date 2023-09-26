import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import sys
import urllib.request
from bs4 import BeautifulSoup


url = str(sys.argv[1])

get = urllib.request.urlopen(url)
html = get.read()

with open('output.txt', "w", encoding="utf-8") as f:
    f.write(html.decode('utf-8'))