from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
tags = soup('span')
for tag in tags:
    y = str(tag)
    x = re.findall("[0-9]+",y)
    for i in x:
        sum = sum + int(i)
    #sum = sum + int(tag.contents[0])
print(sum)
