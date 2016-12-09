with open('9.txt', 'r') as file:
    DATA = file.read()


def decompress(data):
    result = 0
    skip = 0
    for i in range(len(data)):
        skip -= 1
        if skip > 0:
            continue

        if data[i] == '(':
            n = i

            while data[n] != ')':
                n += 1

            e = n - i + 1
            length, repeat = [int(_) for _ in data[i + 1:n].split('x')]
            result += decompress(data[i + e:i + e + length]) * repeat
            skip = e + length
        else:
            result += 1

    return result


print(decompress(DATA))
