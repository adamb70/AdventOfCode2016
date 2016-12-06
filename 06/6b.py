from collections import Counter

DATA = [[] for _ in range(8)]
result = ""

with open('6.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        for i in range(8):
            DATA[i].append(line[i])


for col in DATA:
    result += Counter(col).most_common()[-1][0]

print(result)
