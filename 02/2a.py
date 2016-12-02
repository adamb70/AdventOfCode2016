with open('2.txt', 'r') as file:
    data = file.read()

DATA = data.split('\n')
result = ""
current = 5

for line in DATA:
    for direction in line:
        if direction == "U":
            if current > 3:
                current -= 3
        elif direction == "D":
            if current < 7:
                current += 3
        elif direction == "L":
            if current not in [1, 4, 7]:
                current -= 1
        elif direction == "R":
            if current not in [3, 6, 9]:
                current += 1
    result += str(current)

print(result)
