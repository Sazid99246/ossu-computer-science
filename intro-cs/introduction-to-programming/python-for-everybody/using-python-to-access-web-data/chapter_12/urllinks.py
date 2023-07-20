import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Function to follow links and retrieve the last name
def follow_links(url, count, position):
    for i in range(count):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Retrieve all of the anchor tags
        tags = soup('a')
        
        # Check if position is within range
        if position <= len(tags):
            url = tags[position - 1].get('href')
            name = tags[position - 1].text
            print(f"Retrieving: {url}")
        else:
            print("Position out of range.")
            break
        
    return name

# Prompt the user for inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Call the follow_links function
print(f"Retrieving: {url}")
last_name = follow_links(url, count, position)