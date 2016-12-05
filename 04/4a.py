import re
from collections import Counter
from itertools import groupby
from operator import itemgetter


with open('4.txt', 'r') as file:
    data = file.read().split('\n')

DATA = []
result = 0

for line in data:
    a, b, c = re.split(r'(\d+)', line)
    DATA.append([a.replace('-', ''), int(b), re.sub(r'\[|]', '', c)])

for name, ID, checksum in DATA:
    fin_name = list()
    name_pop = Counter(name).most_common(len(name))

    #srtd = sorted(name_pop, key=lambda tup: tup[1], reverse=True)
    grouped = [list(group) for key, group in groupby(name_pop, itemgetter(1))]

    for grp in grouped:
        if len(grp) > 1:
            [fin_name.append(l) for l, v in sorted(grp)]
        else:
            fin_name.append(grp[0][0])

    fin_name = ''.join(fin_name[0:5])

    if fin_name == checksum:
        result += ID

print(result)