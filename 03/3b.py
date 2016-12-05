import re
from itertools import combinations

with open('3.txt', 'r') as file:
    data = file.read()

raw_DATA = data.split('\n')
unf_DATA = []
result = 0

for line in raw_DATA:
    unf_DATA.append([int(n) for n in re.split(r'\s+', line.strip())])

col1 = []
col2 = []
col3 = []

for x in unf_DATA:
    col1.append(x[0])
    col2.append(x[1])
    col3.append(x[2])

temp = col1 + col2 + col3
DATA = [temp[i:i + 3] for i in range(0, len(temp), 3)]

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
