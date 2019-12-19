def insertion_sort(arr):
    if len(arr) < 2:
        return
    key = 1
    while key < len(arr):
        index = key
        while index > 0:
            if arr[index] < arr[index - 1]:
                arr[index - 1], arr[index] = arr[index], arr[index - 1]
                index -= 1
            else:
                break
        key += 1
