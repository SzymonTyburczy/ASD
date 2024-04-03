def selectsort(array):
    for i in range(0, len(array)):
        min_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return array
A = [5,4,3,2,1]
print(selectsort(A))
#Szukamy najmniejszej wartosci w tablicy a nastepnie wybieramy ja  dajemy na sam poczatek (zamieniamy pozycje 1 z pozycjanajmniejszego elementu)
#poczatek posortowany - dalsze iteracje
