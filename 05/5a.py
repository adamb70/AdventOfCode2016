import hashlib

with open('5.txt', 'r') as file:
    DATA = file.read().strip()

password = ''

for i in range(10000000):
    door = DATA + str(i)
    hsh = hashlib.md5(door.encode('utf-8')).hexdigest()
    if str(hsh).startswith('00000'):
        password += hsh[5]
        if len(password) >= 8:
            break

print(password)
