def selection_sort(arr):
    marker = 0
    while marker < len(arr) - 1:
        index = marker + 1
        while index < len(arr):
            if arr[marker] > arr[index]:
                arr[marker], arr[index] = arr[index], arr[marker]
            index += 1
        marker += 1

