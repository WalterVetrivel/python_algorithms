from random import randint


def binary_search(n, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if n == arr[mid]:
            return mid
        elif n > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def create_list(max_val):
    return [randint(max_val) for num in range(max_val)]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_to_search = int(input('Enter number to search: '))

print(f'Index of {num_to_search} is: {binary_search(num_to_search, l)}')
