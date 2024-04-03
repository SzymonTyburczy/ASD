# szukanie binarne
def binary_search(array, left, right, szukana):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == szukana:
            return mid
        elif array[mid] > szukana:
            return binary_search(array, left, mid-1, szukana)
        else:
            return binary_search(array, mid + 1, right, szukana)

T = [1,2,3,17,21,58,99]
print(binary_search(T, 0, len(T)-1, 3))
