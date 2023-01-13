import json
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0

url = input("Enter URL: ")
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
for item in info['comments']:
    number = item['count']
    count = count + number
print(count)