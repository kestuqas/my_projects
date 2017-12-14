L = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
# L = [0, 2, 7, 0]
L1 = [0, 2, 7, 0]
step = 0
LL = []
d1 = 0
d = 0


def check(LL):
    global d
    for item in LL:
        for x in LL:
            if item == x:
                d += 1
                if d > 1:

                    print('Radau, žingsnis: ', step, 'd =', d)
                    print('x indeksas: ', LL.index(item))


                    return d
                    break
        d = 0


while step < 5042:
# while d < 2:

    max_val = max(L)
    max_poz = L.index(max_val)

    i = 1
    j = 0
    L[max_poz] = 0
    while i <= max_val:
        if (max_poz + i) > (len(L) - 1) or j > (len(L) - 1):
            if j > (len(L) - 1):
                j = 0
            L[j] += 1
            # print(L[j], '1 i = ', i)
            j += 1

        else:
            L[max_poz + i] += 1
            # print(L[max_poz + i], '3 i = ', i)
        i += 1
    LL.append(list(L))
    step += 1

    # check(LL)
# print('Pabaiga, žingsnis: ', step)


