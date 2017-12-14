import os
print(os.getcwd())


file = "C:\\Users\\Administrator\\Desktop\\Code of Advent\\passphrase.txt"


def check(line):

    L = line.strip().split(" ")

    L[-1].replace('\\n', '')
    # print(L)
    global bad
    for item in L:
        a = L.count(item)
        if a > 1:
            bad += 1
            return print('bad: ', bad, ' Result: ', line_no - bad)
            break
    check2(L)


def check2(L):
    j = 0
    for item in L:
        i = 1
        for x in range(len(L) - 1 - j):
            if len(item) == len(L[L.index(item) + i]):
                if check3(item, L[L.index(item) + i]) == 'found':
                    global bad
                    bad += 1
                    return print('bad: ', bad, ' Result: ', line_no - bad)

                    break

            i += 1
        j += 1


def check3(a, b):
    for item in a:
        if item not in b:
            break
        elif a.count(item) != b.count(item):
            break
    else:
        print(a, b)
        return 'found'


bad = 0

with open(file) as f:
    line_no = 1
    for line in f.readlines():
        print('Line no: ', line_no)
        check(line)
        line_no += 1
