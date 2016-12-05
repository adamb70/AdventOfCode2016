import hashlib

with open('5.txt', 'r') as file:
    DATA = file.read().strip()

password = {}


def is_valid(n):
    try:
        if int(n) > 7:
            return False
        return True
    except ValueError:
        return False


for i in range(100000000):
    door = DATA + str(i)
    hsh = hashlib.md5(door.encode('utf-8')).hexdigest()
    if str(hsh).startswith('00000'):
        if not password.get(hsh[5]) and is_valid(hsh[5]):
            password[hsh[5]] = hsh[6]

            if len(password) >= 8:
                break


print(''.join([y for x, y in sorted(password.items())]))
