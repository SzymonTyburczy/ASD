def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def find_sum_pairs_with_binary_search(array, target):
    for i in range(len(array)):
        remaining_sum = target - array[i]
        pair = binary_search(array, remaining_sum)
        if pair:
            return 1

    return 0


def find_sum_pairs(array):
    # Sort the array in non-decreasing order
    array.sort()

    for i in range(0, len(array)):
        element = array[i]
        k = i
        if k != len(array)-1:
            while k < len(array) and array[k] == array[k+1]:
                k += 1
        else:
            if not find_sum_pairs_with_binary_search(array[0:k], element):
                return "not nice"
        if not find_sum_pairs_with_binary_search(array[0:k+1], element):
            return "not nice"
    return "nice"


my_array = [0, 0, 0, 2, 5, 3, 7, 1, 1, 1]
print(find_sum_pairs(my_array))

