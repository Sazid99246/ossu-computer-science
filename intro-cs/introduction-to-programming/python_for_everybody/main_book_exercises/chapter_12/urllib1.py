from urllib import request, parse, error

url = input("Enter a url: ")
fhand = request.urlopen(url)
words = fhand.read().decode()

print(words[:3000])
count = len(words)

print("Total words in the document is: " + str(count))