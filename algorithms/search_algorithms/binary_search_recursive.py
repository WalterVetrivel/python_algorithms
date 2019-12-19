def binary_search(n, arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == n:
        return mid
    elif arr[mid] < n:
        return binary_search(n, arr, mid + 1, end)
    else:
        return binary_search(n, arr, start, mid - 1)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_to_search = int(input('Enter number to search: '))

print(
    f'Index of {num_to_search} is: {binary_search(num_to_search, l, 0, len(l) - 1)}')
