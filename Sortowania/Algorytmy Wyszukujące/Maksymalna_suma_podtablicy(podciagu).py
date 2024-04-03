# Algorytm o zlozonosci n^2
def function_n2(array):
    max_sum = array[0]
    start_index = 0
    end_index = 0
    for i in range(0, len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum > max_sum:
                max_sum = sum
                start_index = i
                end_index = j
    return max_sum, start_index, end_index

# algorytm o zlozonosci nlogn
def function_nlogn_crossing(array, low, mid, high):
    left_sum = -9999999999
    sum = 0
    for i in range(mid, low-1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -999999999
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return left_sum + right_sum, max_left, max_right


def function_nlogn(array, low, high):
    if high == low:
        return low, high, array[low]
    else:
        mid = (low + high) // 2
        (left_sum, left_low, left_high) = function_nlogn(array, low, mid)
        (right_sum, right_low, right_high) = function_nlogn(array, mid + 1, high)
        (cross_sum, cross_low, cross_high) = function_nlogn_crossing(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_low, left_high
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_low, right_high
        else:
            return cross_sum, cross_low, cross_high


# algorytm kadane'a o zlozonosci liniowej

def kadean(array):
    max_sum = current_sum = array[0]
    start_index = end_index = 0

    for i in range(0, len(array)):
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
        if current_sum < array[i]:
            current_sum = array[i]
            start_index = i
    return max_sum, start_index, end_index


T = [-1, -2, -3, 3, 4]

print(function_n2(T))
print(function_nlogn(T, 0, len(T) - 1))
print(kadean(T))
