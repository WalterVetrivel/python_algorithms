import random
import time

from sort_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort


def read_int(msg):
    return int(input(msg))


def generate_list(list_size, value_range):
    return [random.randint(0, value_range) for num in range(list_size)]


def runtime_analyser(input_list, algorithm):
    start_time = time.time()
    algorithm(input_list[:])
    end_time = time.time()
    return end_time - start_time


def select_algorithm():
    print('-' * 30)
    print('SELECT AN ALGORITHM TO ANALYSE')
    print('-' * 30)
    print('1. Bubble Sort')
    print('2. Insertion Sort')
    print('3. Selection Sort')
    print('4. Merge Sort')
    print('5. Quick Sort')
    print("6. Python's sorted function")
    print('0. Quit')
    print('-' * 30)
    return read_int('Enter your choice: ')


def display_results(runtime, list_size, algorithm):
    print('-' * 10)
    print('RESULTS')
    print('-' * 10)
    print(
        f'The runtime of {algorithm} for sorting a random list of {list_size} numbers is : {runtime}')


def main():
    print('-' * 30)
    print('SORTING ALGORITHM RUNTIME ANALYSER')
    print('-' * 30)

    while True:
        choice = select_algorithm()
        if choice == 0:
            break
        else:
            list_size = read_int('Enter the list size: ')
            value_range = read_int('Enter the value range: ')

            input_list = generate_list(list_size, value_range)
            if choice == 1:
                runtime, algorithm = runtime_analyser(
                    input_list, bubble_sort), bubble_sort.__name__
            elif choice == 2:
                runtime, algorithm = runtime_analyser(
                    input_list, insertion_sort), insertion_sort.__name__
            elif choice == 3:
                runtime, algorithm = runtime_analyser(
                    input_list, selection_sort), selection_sort.__name__
            elif choice == 4:
                runtime, algorithm = runtime_analyser(
                    input_list, merge_sort), merge_sort.__name__
            elif choice == 5:
                runtime, algorithm = runtime_analyser(
                    input_list, quick_sort), quick_sort.__name__
            elif choice == 6:
                runtime, algorithm = runtime_analyser(
                    input_list, sorted), sorted.__name__
            else:
                print('Invalid choice.')
                continue

            display_results(runtime, list_size, algorithm)


main()
