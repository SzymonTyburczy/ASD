# Radix Sort czyli sortowanie pozycyjne - sortuje od najmniej istotnej do najbardziej istotnej cyfry w liczbe
# Zlozonosc O(nk)

# divisor to po ktorej cyfrze sortujemy od tylu, przy czym jezeli mamy liczby 123 i 40 to 40 pojdzie na poczatek bo divisor bedzie tak duzy ze zamieni 40 na 0 a 123 na 1
def Count_Radix(A, divisor):
    n = len(A)
    B = [0] * n
    C = [0] * 10
    for i in range(0, n):
        C[A[i] // divisor % 10] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i]//divisor%10]-1] = A[i]
        C[A[i] // divisor % 10] -=1
    return B


def radix_sort(array):
    # dlugosc najdluzszej liczby
    k = len(str(max(array)))
    for i in range(k):
        array = Count_Radix(array, 10**i)
    return array

A = [60, 51213, 4432, 35, 2, 13]
print(radix_sort(A))
