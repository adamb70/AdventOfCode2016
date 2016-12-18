instructions = {}
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

with open('12.txt', 'r') as file:
    for num, line in enumerate(file.readlines()):
        instructions[num] = line.strip().split()


def get_val(obj):
    try:
        return int(obj)
    except ValueError:
        return registers[obj]


def to_int(obj):
    try:
        return int(obj)
    except ValueError:
        return -int(obj[1:])


i = 0
while i < len(instructions):
    instr = instructions[i]

    if instr[0] == 'cpy':
        reg = instr[2]
        val = get_val(instr[1])
        registers[reg] = val
    elif instr[0] == 'inc':
        registers[instr[1]] += 1
    elif instr[0] == 'dec':
        registers[instr[1]] -= 1
    else:
        if get_val(instr[1]) != 0:
            i += to_int(instr[2])
            continue
    i += 1

print(registers['a'])
