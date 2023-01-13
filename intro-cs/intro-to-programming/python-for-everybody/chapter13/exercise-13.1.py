import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter url: ')
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
count = 0

for comment in lst:
    text = comment.find('count').text
    num = int(text)
    count += num
print(count)