import re

result = 0

with open('7.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if re.search(r'(.)(?!\1)(.)\2(?!\2)\1', line):
            if re.search(r'\[[^\]]*(.)(?!\1)(.)\2(?!\2)\1.*?\]?', line):
                pass
            else:
                result += 1

print(result)
