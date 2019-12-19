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
