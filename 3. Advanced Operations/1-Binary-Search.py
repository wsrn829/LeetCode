def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_first_occurrence(arr, target):
    index = binary_search(arr, target)
    if index == -1:
        return -1
    while index > 0 and arr[index - 1] == target:
        index -= 1
    return index

def find_last_occurrence(arr, target):
    index = binary_search(arr, target)
    if index == -1:
        return -1
    while index < len(arr) - 1 and arr[index + 1] == target:
        index += 1
    return index

def find_num_occurrences(arr, target):
    first_index = find_first_occurrence(arr, target)
    if first_index == -1:
        return 0
    last_index = find_last_occurrence(arr, target)
    return last_index - first_index + 1

def find_closest_element(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left if abs(arr[left] - target) < abs(arr[right] - target) else right
