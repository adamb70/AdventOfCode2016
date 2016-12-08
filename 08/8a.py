screen = {(x, y): False for x in range(50) for y in range(6)}
DATA = []

with open('8.txt', 'r') as file:
    for line in file.readlines():
        DATA.append(line.strip())


def rect(x, y):
    for xpos in range(x):
        for ypos in range(y):
            screen[(xpos, ypos)] = True


def rotate_col(col, dist):
    global screen
    temp = screen.copy()
    for ypos in range(6):
        new = ypos + dist
        new -= 6 if new > 5 else 0
        temp[(col, new)] = screen[(col, ypos)]
    screen = temp.copy()


def rotate_row(row, dist):
    global screen
    temp = screen.copy()
    for xpos in range(50):
        new = xpos + dist
        new -= 50 if new > 49 else 0
        temp[(new, row)] = screen[(xpos, row)]
    screen = temp.copy()


for instruction in DATA:
    if instruction.startswith('rect'):
        x, y = instruction.split(' ')[-1].split('x')
        rect(int(x), int(y))
    elif instruction.startswith('rotate'):
        instruction = instruction.split(' ')
        dist = int(instruction[-1])
        if instruction[2].startswith('y'):
            rotate_row(int(instruction[2].replace('y=', '')), dist)
        elif instruction[2].startswith('x'):
            rotate_col(int(instruction[2].replace('x=', '')), dist)

result = 0
for s in screen.values():
    if s:
        result += 1

print(result)
