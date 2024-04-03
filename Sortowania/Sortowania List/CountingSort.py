# W tym algorytmie zakldamy ze kazdy z n elementow jest calkowity oraz nalezy od przedzialu 0 do k (0 i k wlacznie)
# w tablicy b zostana umieszczone posorotwane dane wejsciowe, w tablicy c przechowywanie chwilowe danych
# dla n <= k czas dzialania to O(n) a ogolnie O(n+k)
# def CountingSort(A, k):
#     n = len(A)
#     B = [0] * len(A)
#     C = [0] * k
#     for j in range(n):
#         C[A[j]] = C[A[j]] + 1
#     # C[i] zawiera teraz liczbe elementow rownych i
#     for i in range(1, k):
#         C[i] = C[i] + C[i - 1]
#     # C[i] zawiera teraz liczbe elementow mniejszych badz rownych i
#     for j in range(n - 1, -1, -1):
#         B[C[A[j]] - 1] = A[j]
#         C[A[j]] = C[A[j]] - 1
#     return B
#
#
# A = [2, 5, 3, 0, 2, 3, 0, 3]
#
# print(CountingSort(A, 6))


def CountSort_Fast(A):
    maxim = max(A)
    minim = min(A)
    lenC = maxim - minim + 1
    C = [0] * lenC
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i] - minim] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]-minim]-1] = A[i]
        C[A[i]-minim] -= 1
    return B


H = [2, 5, 3, 9, 2, 3, 9, 3]
print(CountSort_Fast(H))
