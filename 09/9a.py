result = ""

with open('9.txt', 'r') as file:
    DATA = file.read()

skip = 0
for i in range(len(DATA)):
    skip -= 1
    if skip > 0:
        continue

    if DATA[i] == '(':
        n = i

        while DATA[n] != ')':
            n += 1

        e = n - i + 1
        length, repeat = [int(_) for _ in DATA[i + 1:n].split('x')]
        print(DATA[i + e:i + e + length])
        result += DATA[i + e:i + e + length] * repeat
        skip = e + length
    else:
        result += DATA[i]

print(len(result))
