from lesson_merge_sort import merge, merge_sort
from lesson_insertion_sort import insertion_sort
import time
import numpy as np


def fake_timsort(numbers):
    if len(numbers) < 64:  # 剩下一個, 已經排好了, 直接完成
        return insertion_sort(numbers)

    middle_index = len(numbers)//2
    left_array, right_array = numbers[:middle_index], numbers[middle_index:]
    sorted_left_array = fake_timsort(left_array)
    sorted_right_array = fake_timsort(right_array)
    sorted_numbers = merge(sorted_left_array, sorted_right_array)
    return sorted_numbers


if __name__ == '__main__':
    N = 3 * 10 ** 4
    numbers = np.random.choice(10 ** 5, N, replace=False).tolist()

    start = time.perf_counter()
    insertion_sort(numbers)
    print("Insertion sort time (sec):", round(time.perf_counter() - start, 5))

    start = time.perf_counter()
    merge_sort(numbers)
    print("Merge sort time (sec):", round(time.perf_counter() - start, 5))

    start = time.perf_counter()
    fake_timsort(numbers)
    print("Fake tim sort time (sec):", round(time.perf_counter() - start, 5))
