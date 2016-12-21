from hashlib import md5
import re

pads = set()

with open('14.txt', 'r') as file:
    SALT = file.read().strip()


def get_trip(hsh):
    match = re.search(r'(.)\1{2}', hsh)

    if match:
        char = match.groups()[0]
        return char


def get_quint(hsh):
    return re.findall(r'(.)\1{4}', hsh)

i = 0
while len(pads) < 100:
    hsh = md5((SALT + str(i)).encode('UTF-8')).hexdigest()

    for quint_char in set(get_quint(hsh)):
        for x in range(max(i-1000, 0), i):
            trip_hsh = md5((SALT + str(x)).encode('UTF-8')).hexdigest()
            trip_char = get_trip(trip_hsh)
            if trip_char == quint_char:
                pads.add(x)

    i += 1

print(sorted(pads)[63])