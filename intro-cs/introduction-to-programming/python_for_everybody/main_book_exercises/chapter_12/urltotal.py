import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

nums = []

tags = soup.find_all('span')
for tag in tags:
    strTag = str(tag)
    num = re.findall(r'\d+', strTag)[0]
    nums.append(int(num))

print(f'Count {str(len(nums))}')
print(f'Sum {str(sum(nums))}')