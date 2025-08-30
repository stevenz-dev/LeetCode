def quick_sort(arr, lo, hi):
    if lo >= hi:
        return

    p = hi  # choose rightmost as pivot
    l, r = lo, hi - 1

    while True:
        # Move l to the first element >= pivot
        while l <= r and arr[l] < arr[p]:
            l += 1
        # Move r to the last element < pivot
        while r >= l and arr[r] >= arr[p]:
            r -= 1
        if l >= r:
            break
        arr[l], arr[r] = arr[r], arr[l]

    # put pivot in place
    arr[l], arr[p] = arr[p], arr[l]

    quick_sort(arr, lo, l - 1)
    quick_sort(arr, l + 1, hi)


arr = [3, 5, 8, 1, 2, 9, 4, 7, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
