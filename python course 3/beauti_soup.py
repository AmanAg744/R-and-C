import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = input()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser") # stores the data by parsing it in the desired format by scraing the web
  

