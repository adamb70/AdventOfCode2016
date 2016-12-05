import re
from itertools import combinations

with open('3.txt', 'r') as file:
    data = file.read()

raw_DATA = data.split('\n')
DATA = []
result = 0

for line in raw_DATA:
    DATA.append([int(n) for n in re.split(r'\s+', line.strip())])

for tri in DATA:
    possible = True
    for thing in combinations(tri, 2):
        remaining = list(tri)
        for item in thing:
            remaining.pop(remaining.index(item))

        if sum(thing) <= sum(remaining):
            possible = False
            break

    if possible:
        result += 1


print(result)
