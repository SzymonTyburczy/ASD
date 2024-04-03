#Algorytm QuickSelect jest algorytmem wyboru,
# który służy do znalezienia k-tego najmniejszego elementu na nieuporządkowanej liście.
def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

def quickSelect(list, left, right, k):
    if left == right:
        return list[left]

    pivotIndex = partition(list, left, right)

    if k == pivotIndex:
        return list[k]
    elif k < pivotIndex:
        return quickSelect(list, left, pivotIndex - 1, k)
    else:
        return quickSelect(list, pivotIndex + 1, right, k)
T = [3,7,1,5,6]
print(quickSelect(T,0, len(T)-1, 1))