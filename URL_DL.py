
#import urllib.request
# from urllib.request import urlopen, Request

# url = input()
# request = Request(url)
# response = urlopen(request)
# response = response.read()
# print(response)

import urllib.request
from bs4 import BeautifulSoup
url = input()
urllib.request.urlretrieve(url)
 
file = open("text_file.txt", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
 
f = open("test1.txt", "w")
 
# traverse paragraphs from soup
for data in soup.find_all("p"):
    sum = data.get_text()
    f.writelines(sum)
 
f.close()