# klasyczne babelkowe
# przypadek liniowy czyli ze zamienienie obok siebie
def bubblesort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubblesort_faster(array):
    n = len(array)
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    return array


A = [4, 3, 2, 1]
B = [5, 4, 3, 2, 1]

print(bubblesort(A))
print(bubblesort_faster(B))
