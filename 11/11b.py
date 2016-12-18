from itertools import combinations


class Generator(object):
    def __init__(self, element):
        self.elem = element

    def __repr__(self):
        return str(self.elem) + ' Generator'


class Chip(object):
    def __init__(self, element):
        self.elem = element

    def __repr__(self):
        return str(self.elem) + ' Chip'


def get_moves():
    temp_moves = []
    floor = state[0]
    for x in combinations(distrib[floor], 2):
        if floor < 4:
            temp_moves.append(x + ('UP',))
        if floor > 1:
            temp_moves.append(x + ('DOWN',))
    for x in combinations(distrib[floor], 1):
        if floor < 4:
            temp_moves.append(x + ('UP',))
        if floor > 1:
            temp_moves.append(x + ('DOWN',))

    final_moves = []

    for move in temp_moves:
        safe = True

        if move[-1] == 'UP':
            new_floor = distrib[floor + 1].copy()
            elev_dest = floor + 1
        else:
            if len(move) == 3:
                if move[0].elem == move[1].elem:
                    continue
            new_floor = distrib[floor - 1].copy()
            elev_dest = floor - 1

        new_floor += move[0:-1]
        old_floor = [x for x in distrib[floor] if x not in move[0:-1]]

        while safe:
            # Dont move down to floor 1 if it is empty
            if floor == 2 and elev_dest == 1:
                if len(distrib[1]) == 0:
                    safe = False
                    break
            # Dont move down to floor 2 if 1 and 2 are empty
            elif floor == 3 and elev_dest == 2:
                if len(distrib[1]) == 0 and len(distrib[2]) == 0:
                    safe = False
                    break

            # Test if old floor is safe to move from
            for chip in [x for x in old_floor if type(x) is Chip]:
                gennies = [x for x in old_floor if type(x) is Generator]
                if gennies:
                    if not any([x.elem == chip.elem for x in gennies]):
                        # chip is missing it's generator, but another is present
                        safe = False
                        break

            if not safe:
                break

            # Test that new floor is safe to move to
            for chip in [x for x in new_floor if type(x) is Chip]:
                gennies = [x for x in new_floor if type(x) is Generator]
                if gennies:
                    if not any([x.elem == chip.elem for x in gennies]):
                        # chip is missing it's generator, but another is present
                        safe = False
                        break

            if not safe:
                break

            # If move has already been done, skip
            temp_dstr = distrib.copy()
            temp_dstr[floor] = old_floor
            temp_dstr[elev_dest] = new_floor

            temp_state = (elev_dest, 0, temp_dstr)
            if _hash(temp_state) in visited:
                safe = False
                break

            break

        if safe:
            final_moves.append((tuple(state), move))

    for direction in ([item[1][-1] for item in final_moves if len(item[1]) == 3]):
        for mov in [x for x in final_moves if len(x[1]) == 2]:
            if mov[1][-1] == direction:
                final_moves.remove(mov)

    return final_moves


def get_pairs(state):
    pairs = set()
    dstr = state[2]
    chip_floor = 0

    for chips in dstr.values():
        chip_floor += 1
        for chip in [x for x in set(chips) if type(x) is Chip]:
            gen_floor = 0
            paired = False
            for gens in dstr.values():
                gen_floor += 1
                for gen in [x for x in set(gens) if type(x) is Generator]:
                    if gen.elem == chip.elem:
                        pairs.add((chip_floor, gen_floor))
                        paired = True
                        break
            if paired:
                continue

    return pairs


def _hash(state):
    temp_table = (state[0],)
    temp_table += (tuple(get_pairs(state)),)
    return hash(temp_table)


def add_to_visited(state):
    visited.add(_hash(state))



distrib = {}

with open('11.txt', 'r') as file:
    floor = 0
    for line in file.readlines():
        floor += 1
        if 'nothing' in line:
            distrib[floor] = []
        else:
            line = line.strip().replace(',', '').replace('.', '').replace('and', '').split(' a ')[1:]
            distrib[floor] = []
            for item in line:
                if 'generator' in item:
                    elem = item.split(' ')[0]
                    distrib[floor].append(Generator(elem))
                else:
                    elem = item.split('-')[0]
                    distrib[floor].append(Chip(elem))

distrib[1] += [Chip('elerium'), Generator('elerium'), Chip('dilithium'), Generator('dilithium')]
# (floor, moves, placements)
state = (1, 0, distrib)
visited = set()

moves = get_moves()
while moves:
    move = moves.pop(0)
    state, move = move
    floor = state[0]
    distrib = state[2].copy()

    if move[-1] == 'UP':
        new_floor = distrib[floor + 1].copy()
        elev_dest = floor + 1
    else:
        new_floor = distrib[floor - 1].copy()
        elev_dest = floor - 1

    new_floor += move[0:-1]
    old_floor = [x for x in set(distrib[floor]) if x not in move[0:-1]]

    add_to_visited(state)

    distrib[floor] = old_floor
    distrib[elev_dest] = new_floor
    state = (elev_dest, state[1] + 1, distrib.copy())

    if len(state[2][1] + state[2][2] + state[2][3]) == 0:
        # All items on 4th floor
        print(state[1])
        break
    else:
        moves += get_moves()
