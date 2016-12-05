import re

with open('4.txt', 'r') as file:
    data = file.read().split('\n')

DATA = []
result = []

for line in data:
    a, b, c = re.split(r'(\d+)', line)
    DATA.append([a.replace('-', ' ').strip(), int(b), re.sub(r'\[|]', '', c)])


for name, ID, checksum in DATA:
    decrypted = ''
    for letter in name:
        dec = 0
        if letter == ' ':
            decrypted += letter
        else:
            dec = ord(letter) + ID
            while dec > 122:
                dec -= 26

        decrypted += chr(dec).replace('\x00', '')

    if 'pole' in decrypted:
        result.append((name, ID, decrypted))

print(result)

