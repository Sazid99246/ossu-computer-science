file = open('assets/py4e/mbox-short.txt')
mail = dict()
for line in file:
    if line.startswith("From"):
        words = line.split()
        mailAddress = words[1]
        domain = mailAddress.split("@")
        if domain[1] not in mail:
            mail[domain[1]] = 1
        else:
            mail[domain[1]] += 1
print(mail)