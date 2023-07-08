import numpy as np

def merge(left_array, right_array):
    result = list()
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] < right_array[0]:
            result.append(left_array.pop(0))
        else:
            result.append(right_array.pop(0))
    if len(left_array) > 0:
        result += left_array  # result = result + left_array
    else:
        result += right_array
    return result

def merge_sort(array):
    if len(array) == 1:  # 剩下一個, 已經排好了, 直接完成
        return array
    # 切一半
    middle_index = len(array)//2
    left_array, right_array = array[:middle_index], array[middle_index:]
    # 排好兩半
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)
    # 合併
    sorted_array = merge(sorted_left_array, sorted_right_array)
    return sorted_array

if __name__ == '__main__':
    numbers = np.random.choice(100, 10, replace=False).tolist()
    print(numbers)
    print(merge_sort(numbers))

    # Note: Numpy Pop = np.delete
    # numbers = np.random.choice(100, 10, replace=False)
    # print(numbers, numbers[0], np.delete(numbers, 0))
