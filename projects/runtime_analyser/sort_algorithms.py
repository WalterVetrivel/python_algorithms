def bubble_sort(arr):
    swap_happened = True
    max_index = len(arr) - 1
    while swap_happened:
        swap_happened = False
        for (index, el) in enumerate(arr):
            if index < max_index and el > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swap_happened = True


def selection_sort(arr):
    marker = 0
    while marker < len(arr) - 1:
        index = marker + 1
        while index < len(arr):
            if arr[marker] > arr[index]:
                arr[marker], arr[index] = arr[index], arr[marker]
            index += 1
        marker += 1


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


def merge_sorted(left_list, right_list):
    sorted_list = []
    left_index, right_index = 0, 0

    # Comparing elements in both lists
    while left_index < len(left_list) and right_index < len(right_list):
        if (left_list[left_index] < right_list[right_index]):
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    # For remaining elements
    if left_index < len(left_list):
        sorted_list.extend(left_list[left_index:])
    if right_index < len(right_list):
        sorted_list.extend(right_list[right_index:])

    return sorted_list


def merge_sort(full_list):
    if len(full_list) < 2:
        return full_list[:]
    else:
        middle = len(full_list) // 2
        left_list = merge_sort(full_list[:middle])
        right_list = merge_sort(full_list[middle:])
        return merge_sorted(left_list, right_list)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equal.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)
