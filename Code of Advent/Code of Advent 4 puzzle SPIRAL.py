
L = [1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59]


def numeris(b1, b2, b3, b4, i, n, j):

    if n == 0:
        num = (b1 + b2 + b3 + b4)
        return num

    else:
        num = (b1 + b2 + b3 + b4)
        L.append(num)
        b11 = num
        b21 = L[i]
        b31 = L[i + 1]
        b41 = L[i + 2]
        # print('Pirmas: ', num)
        # print(L)

        for x in range(j):
            num = (b11 + b21 + b31 + b41)
            L.append(num)
            i += 1
            b11 = num
            b21 = L[i]
            b31 = L[i + 1]
            b41 = L[i + 2]
            # print('b11: ', b11)
            # print('b21: ', b21)
            # print('b31: ', b31)
            # print('b41: ', b41)
            # print('Vidurinis: ', num)
            # print(L)

        num = (b11 + b21 + b31)
        L.append(num)
        b12 = num
        b22 = b31
        # print('Antras: ', num)
        # print(L)

        num = (b12 + b22)
        L.append(num)
        b13 = num
        b23 = b12
        b33 = L[i + 1]
        b43 = L[i + 2]
        # print('b13: ', b13)
        # print('b23: ', b23)
        # print('b33: ', b33)
        # print('b43: ', b43)
        # print('Trecias: ', num)
        # print(L)

        num = (b13 + b23 + b33 + b43)
        L.append(num)
        i += 1
        b11 = num
        b21 = L[i]
        b31 = L[i + 1]
        b41 = L[i + 2]
        # print('PirmasPirmas: ', num)
        # print(L)

        for x in range(j):
            num = (b11 + b21 + b31 + b41)
            L.append(num)
            i += 1
            b11 = num
            b21 = L[i]
            b31 = L[i + 1]
            b41 = L[i + 2]
            # print('b11: ', b11)
            # print('b21: ', b21)
            # print('b31: ', b31)
            # print('b41: ', b41)
            # print('VidurinisVidurinis: ', num)
            # print(L)

        num = (b11 + b21 + b31)
        L.append(num)
        b12 = num
        b22 = b31
        # print('AntrasAntras: ', num)
        # print(L)

        num = (b12 + b22)
        L.append(num)
        b13 = num
        b23 = b12
        b33 = L[i + 1]
        b43 = L[i + 2]
        # print('b13: ', b13)
        # print('b23: ', b23)
        # print('b33: ', b33)
        # print('b43: ', b43)
        # print('TreciasTrecias: ', num)
        # print(L)

        i += 1
        j += 1
        return numeris(b13, b23, b33, b43, i, n - 1, j)

num = numeris(59, 57, 2, 4, 1, 5, 1)
print(L)
print('Galutinis atsakymas = ', num)
