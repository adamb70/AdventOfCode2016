with open('1.txt', 'r') as file:
    data = file.read()

DATA = data.replace(' ', '').split(',')
X, Y = 0, 0


for x in DATA:
    direction = x[0]
    distance = int(x[1:])

    if direction == "L":
        X, Y = Y, -X
    elif direction == "R":
        X, Y = -Y, X

    Y += distance


print(X + Y)
