def parent(i):  # znalezn=ienie rodzica
    return (i - 1) // 2


def heapify(T, i, n):  # funkcja ktora naprawia nam drzewo binarne
    l = 2 * i + 1  # znalezienie lefta dla rodzica
    r = 2 * i + +2  # znalezienie righta dla rodzica
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l

    if r < n and T[r] > T[max_ind]:
        max_ind = r

    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, max_ind, n)


def build_heap(array):  # funkcja towrzaca drzewo binarne
    n = len(array)
    for i in range(parent(n - 1), -1, -1):
        heapify(array, i, n)


def HeapSort(T):  # sorcik
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]  # wsadzamy na poczatek tablicy koncowa wartosc bo w kopcu max koncowa wartosx jest najmniejsza
        heapify(T, 0, i)


K = [6, 54, 2, 6, 1]
HeapSort(K)
print(K)
