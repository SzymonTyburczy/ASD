def KMP(text, pattern):
    prefix_array = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            prefix_array[i] = j
        else:
            if j != 0:
                j = prefix_array[j-1]
            else:
                prefix_array[i] = 0
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            print("Znaleziono wzorzec na indeksie " + str(i-j))
            j = prefix_array[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = prefix_array[j-1]
            else:
                i += 1

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            print(f"Wzorzec znaleziony na indeksie {i}")

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

text = "ABC ABCDAB ABCDABCDABDE"
pattern = "ABCDABD"

KMP(text, pattern)
naive_search(text, pattern)
print(boyer_moore(text, pattern))
