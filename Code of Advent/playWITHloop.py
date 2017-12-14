
L = [1, 5, 3, 9]
LL = []
i = 0
j = 0
for x in range(2):
    for i in range(len(L)):
        if i > (len(L) - 1) or j > (len(L) - 1):
            if j > (len(L) - 1):
                j = 0
            L[j] += 1
            j += 1
        else:
            L[i] += 1
        i += 1
    LL.append(L)
    print(L)
    print(LL)

A = [1, 2]
B = []
A[0] = 3
print(A)
B.append(list(A))
print(B)
A[1] += 1
B.append(list(A))
print(B)
