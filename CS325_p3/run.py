#This is the run.py which is the main program it takes the the command line argument as an input
# It doesnt have any actual output
# The code imports functions from other modules and calls them
import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import sys
import urllib.request
from bs4 import BeautifulSoup
import sys
import os
from module_1 import txtDL
from module_2 import extract
from module_3 import relativeD
from pathlib import Path




txtDL.Txt_DL(str(sys.argv[1]))

filename = relativeD.rel_D()
extract.Ext_com(filename)