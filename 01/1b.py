with open('1.txt', 'r') as file:
    data = file.read()

DATA = data.replace(' ', '').split(',')
X, Y = 0, 0
facing = "N"
result = None
visited = []


def step(turn, distance):
    for d in range(1, distance + 1):
        if turn == "LN" or turn == "RS":
            visited.append((X - d, Y))
        if turn == "LE" or turn == "RW":
            visited.append((X, Y + d))
        if turn == "LS" or turn == "RN":
            visited.append((X + d, Y))
        if turn == "LW" or turn == "RE":
            visited.append((X, Y - d))

        if visited.count(visited[-1]) > 1:
            return visited[-1]


for x in DATA:
    direction = x[0]
    distance = int(x[1:])

    if direction == "L":
        if facing == "N":
            result = step(direction + facing, distance)
            facing = "W"
        elif facing == "E":
            result = step(direction + facing, distance)
            facing = "N"
        elif facing == "S":
            result = step(direction + facing, distance)
            facing = "E"
        elif facing == "W":
            result = step(direction + facing, distance)
            facing = "S"

    elif direction == "R":
        if facing == "N":
            result = step(direction + facing, distance)
            facing = "E"
        elif facing == "E":
            result = step(direction + facing, distance)
            facing = "S"
        elif facing == "S":
            result = step(direction + facing, distance)
            facing = "W"
        elif facing == "W":
            result = step(direction + facing, distance)
            facing = "N"

    X, Y = visited[-1]

    if result:
        break


print(abs(result[0]) + abs(result[1]))

