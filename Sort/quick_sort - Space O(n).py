def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # choose the pivot as the last element
    pivot = arr[-1]

    # partition
    left  = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left ) + [pivot] + quick_sort(right)

# Example
nums = [5, 3, 8, 4, 2, 7, 1, 10]
print(quick_sort(nums))  # Output: [1, 2, 3, 4, 5, 7, 8, 10]
