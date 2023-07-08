import numpy as np

def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers

    # 切分
    pivot = numbers[0]
    left_part = list()
    right_part = list()
    for number in numbers[1:]:
        if number > pivot:
            right_part.append(number)
        else:
            left_part.append(number)

    # 合併
    sorted_left_part = quick_sort(left_part)
    sorted_right_part = quick_sort(right_part)
    sorted_numbers = sorted_left_part + [pivot] + sorted_right_part
    return sorted_numbers

if __name__ == '__main__':
    numbers = np.random.choice(100, 10, replace=False).tolist()
    print(numbers)
    print(quick_sort(numbers))
