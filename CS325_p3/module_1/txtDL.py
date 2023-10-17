#This file takes input from run.py which is the url
#It outputs a file into the raw folder as output.txt
#The whole code is taking the url it's given and extracting all the text and putting it in raw folder.
import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import sys
import urllib.request
from bs4 import BeautifulSoup
import os.path
from pathlib import Path

#url = str(sys.argv[1])
def Txt_DL(url):
    root_dir = Path(__file__).resolve().parent.parent
    
    save_path = root_dir /"Data"/ "raw"
    
    completeName = os.path.join(save_path, "output.txt")
    get = urllib.request.urlopen(url)
    html = get.read()


    with open(completeName, "w", encoding="utf-8") as f:
        f.write(html.decode('utf-8'))