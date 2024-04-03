def convert(n):
    A = [0] * 10
    temp = n
    while temp > 0:
        A[temp % 10] += 1
        temp //= 10
    single = 0
    many = 0
    for d in A:
        if d == 1:
            single += 1
        elif d > 1:
            many += 1
    return n, single, many


def countingSort(A, p, way):
    B = [0] * len(A)
    C = [0] * 10
    for i in range(len(A)):
        C[A[i][p]] += 1
    if way == 1:
        for i in range(1, len(C)):
            C[i] += C[i - 1]
    else:
        for i in range(len(C) - 2, -1, -1):
            C[i] += C[i + 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i][p]] - 1] = A[i]
        C[A[i][p]] -= 1
    return B


def prettySort(T):
    n = len(T)
    for i in range(n):
        T[i] = (convert(T[i]))
    T = countingSort(T, 2, 1) #sortowanie po 2kach - im mniej tym lepiej
    T = countingSort(T, 1, -1)# sortowanie po 1kach - im wiecej tym lepiej stad -1 - odwortonie way zrobiony
    return T

A = [2344, 67333, 1266, 455, 114577, 1234444444]
A = prettySort(A)
print(A)
