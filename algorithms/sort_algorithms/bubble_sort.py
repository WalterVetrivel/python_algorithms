def bubble_sort(arr):
    swap_happened = True
    max_index = len(arr) - 1
    while swap_happened:
        swap_happened = False
        for (index, el) in enumerate(arr):
            if index < max_index and el > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swap_happened = True
