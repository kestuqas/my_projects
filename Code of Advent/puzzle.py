file = "C:\\Users\\Administrator\\Desktop\\Code of Advent\\towers.txt"

with open(file, 'r') as f:
    a = f.read().splitlines()

b = []
# print(a)

for item in a:
    b.append(item.replace('(', ''))
# print(b)

a = []

for item in b:
    a.append(item.replace(')', ''))
# print(a)

b = []
# print(a)

for item in a:
    b.append(item.replace('-> ', ''))
# print(b)

a = []

for item in b:
    a.append(item.replace(',', ''))
# print(a)

b = []

for item in a:
    b.append(item.split(" "))
# print(b)

for item in b:
    item[1] = int(item[1])

d = {t[0]:t[1:] for t in b}
print(d)

# d = {'tknk': [41, 'ugml', 'padx', 'fwft'],
#      'padx': [45, 'pbga', 'havc', 'qoyq'],
#      'fwft': [72, 'ktlj', 'cntj', 'xhth'],
#      'ugml': [68, 'gyxo', 'ebii', 'jptl'],
#      'pbga': [66],
#      'xhth': [66],
#      'ebii': [66],
#      'havc': [66],
#      'ktlj': [66],
#      'qoyq': [66],
#      'jptl': [66],
#      'gyxo': [66],
#      'cntj': [66],}

priklausomi = []

for item in d:
    for x in d:
        for y in d[x][1:]:
            if y == item:
                priklausomi.append(item)

print(priklausomi)

for item in d:
    if item not in priklausomi:
        print(item)

