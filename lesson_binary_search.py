import numpy as np
from lesson_insertion_sort import insertion_sort


def binary_search(numbers, target):
    start, end = 0, len(numbers)-1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    print("Target Not Found")
    return -1


if __name__ == '__main__':
    N = 100
    numbers = np.random.choice(1000, N, replace=False)
    numbers = insertion_sort(numbers)
    target = np.random.choice(numbers, 1)[0]
    # print(numbers, target)
    target_index = binary_search(numbers, target)
    print(numbers[target_index], target)
