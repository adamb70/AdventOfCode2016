import regex

result = 0

with open('7.txt', 'r') as file:
    for line in file.readlines():
        fnd = regex.findall(r'(?:(?<=\[[^\]]*)(?=((\w)(?!\2)\w\2))(?=.*\])|(?=((\w)(?!\4)\w\4)))', line.strip())
        aba = [x[0] for x in fnd if x[0] != '']
        bab = [x[2] for x in fnd if x[2] != '']

        for x in aba:
            if "".join([x[1], x[0], x[1]]) in bab:
                result += 1
                break

print(result)
