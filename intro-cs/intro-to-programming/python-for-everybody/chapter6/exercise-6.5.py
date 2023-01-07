str = 'X-DSPAM-Confidence:0.8475'
col_pos = str.find(":")
number = str[col_pos + 1:]
confdence = float(number)
print(confdence)