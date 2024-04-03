def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        k = i - 1
        while k >= 0 and key < array[k]:
            array[k + 1] = array[k]
            k -= 1
        array[k + 1] = key
    return array


A = [4, 3, 2, 1, 90]
print(InsertionSort(A))


# Insert Sort - przechodzimy od poczatku tablicy po danych wartosciach od 1 i sprawdzamy jak najdalej mozna je wstawic przed wartosci poprzedzajace
# stad sortowanie przez wstawianie - wstawiamy wartosci przed wszystko


def selectsort(array):
    for i in range(0, len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return array


A = [6,8,4,9,1,5]
print(selectsort(A))


# Szukamy najmniejszej wartosci w tablicy a nastepnie wybieramy ja  dajemy na sam poczatek (zamieniamy pozycje 1 z pozycjanajmniejszego elementu)
# poczatek posortowany - dalsze iteracje
