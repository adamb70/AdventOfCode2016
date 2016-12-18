with open('13.txt', 'r') as file:
    fav_num = int(file.read().strip())


def is_wall(coords):
    x, y = coords
    res = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    rep = str(bin(res))[2:]
    if rep.count('1') % 2 == 0:
        return False
    return True


def get_moves(state):
    i, (x, y) = state
    mvs = []
    if x != 0:
        mvs.append((x - 1, y))
    if y != 0:
        mvs.append((x, y - 1))
    mvs.append((x + 1, y))
    mvs.append((x, y + 1))
    ret = []
    for m in mvs:
        if not hash(m) in visited and not hash(m) in walls:
            ret.append((i, m))
    return ret


pos = (1, 1)
visited = {hash(pos)}
walls = set()

# (number of moves, pos)
state = (0, pos)
moves = get_moves(state)
result = set()

while moves:
    i, move = moves.pop(0)

    if not is_wall(move):
        if i < 50:
            result.add(hash(move))
        elif i == 51:
            break

        i += 1
        visited.add(hash(move))
        state = (i, move)
        moves += get_moves(state)
    else:
        walls.add(hash(move))

print(len(result) + 1)
