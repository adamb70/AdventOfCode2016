with open('2.txt', 'r') as file:
    data = file.read()

DATA = data.split('\n')
result = ""
current = "5"

"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

dic = {
    "1": ["0", "0", "3", "0"],
    "2": ["0", "3", "6", "0"],
    "3": ["1", "4", "7", "2"],
    "4": ["0", "0", "8", "3"],
    "5": ["0", "6", "0", "0"],
    "6": ["2", "7", "A", "5"],
    "7": ["3", "8", "B", "6"],
    "8": ["4", "9", "C", "7"],
    "9": ["0", "0", "0", "8"],
    "A": ["6", "B", "0", "0"],
    "B": ["7", "C", "D", "A"],
    "C": ["8", "0", "0", "B"],
    "D": ["B", "0", "0", "0"],
}

for line in DATA:
    for direction in line:
        if direction == "U":
            if dic[current][0] != "0":
                current = dic[current][0]
        elif direction == "D":
            if dic[current][2] != "0":
                current = dic[current][2]
        elif direction == "L":
            if dic[current][3] != "0":
                current = dic[current][3]
        elif direction == "R":
            if dic[current][1] != "0":
                current = dic[current][1]
    result += current

print(result)
