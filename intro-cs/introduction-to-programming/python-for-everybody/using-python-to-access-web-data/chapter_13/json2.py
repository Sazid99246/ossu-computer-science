import json
import urllib.request, urllib.parse, urllib.error

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    print('URL is required')
    exit()
print("Retrieving " + url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

comments = json.loads(data)['comments']
print('Count:', len(comments))

sum_count = 0
for item in comments:
    count = item['count']
    sum_count += count
print("Sum:", str(sum_count))