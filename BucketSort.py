def selectionsort(bucket):
    n = len(bucket)
    for i in range(0, n):
        minidx = i
        for j in range(i, n):
            if bucket[minidx] > bucket[j]:
                minidx = j
        bucket[i], bucket[minidx] = bucket[minidx], bucket[i]


def bucketsort(array):
    n = len(array)
    maxval = max(array)
    minval = min(array)
    bucket_range = (maxval + minval + 1) / n
    buckets = [[] for _ in range(n)]
    for val in array:
        bucket_idx = int((val - minval) / bucket_range)
        buckets[bucket_idx].append(val)
    for i in range(n):
        selectionsort(buckets[i])

    idx = 0
    for bucket in buckets:
        for val in bucket:
            array[idx] = val
            idx += 1


tab = [0.124, 0.432, 0.976, 0.834, 0.194, 0.629, 0.333, 0.666]
bucketsort(tab)
print(tab)