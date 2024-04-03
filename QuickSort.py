def partition_HOAREA(array, l, r):
    mid = (l + r) // 2
    val = array[mid]
    i, j = l-1, r+1
    while True:
        i+=1
        while array[i] < val:
            i += 1
        j -= 1
        while array[j] > val:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def partition_LUMOTO(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def QuickSort(array, l, r):
    if l < r:
        part = partition_HOAREA(array, l, r)
        QuickSort(array, l, part)
        QuickSort(array, part+1, r)


def QuickSort2(array, l, r):
    if l < r:
        part = partition_LUMOTO(array, l, r)
        QuickSort(array, l, part - 1)
        QuickSort(array, part + 1, r)


A = [7, 8, 2, 4]
B = [7, 8, 2, 4]
QuickSort(A, 0, len(A) - 1)
QuickSort2(B, 0, len(B) - 1)
print(A)
print(B)
