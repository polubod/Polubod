import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import sys

file_url = str(sys.argv[1])
#print(file_url)
with open('readme.txt', 'w') as f:
    for line in urllib.request.urlopen(file_url):
        f.write(line.decode('utf-8'))
