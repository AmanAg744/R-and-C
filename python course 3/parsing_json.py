import json
import urllib.request,urllib.parse,urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




url = input("Enter-")
html = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(html)

sum = 0

for i in info["comments"]:
    sum = sum + int(i["count"])
print(sum)
    