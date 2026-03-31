def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid + 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Find position using binary search
        pos = binary_search(arr, key, 0, i - 1)

        # Shift elements
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1

        arr[pos] = key

    return arr


# Example
arr = [37, 23, 0, 17, 12, 72, 31]
print("Sorted array:", binary_insertion_sort(arr))