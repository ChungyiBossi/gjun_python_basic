import math
import numpy as np

def _find_divisor_of_min(list_of_numbers):
    # 1
    min_number = min(list_of_numbers)
    # 2
    # 時間複雜度:O(N)
    divisors_of_min = list()
    for n in range(1, min_number+1):
        if min_number % n == 0:
            divisors_of_min.append(n)
    return divisors_of_min

def find_great_common_divisors(list_of_numbers):
    divisors = _find_divisor_of_min(list_of_numbers)
    # 3
    # 時間複雜度:O(M * N), M = len(Divisor), N = len(Number)
    list_of_common_divisors = list()
    for divisor in divisors:
        is_common_divisor = True
        for number in list_of_numbers:
            if number % divisor == 0:
                continue
            else:
                is_common_divisor = False
                break
        if is_common_divisor == True:
            list_of_common_divisors.append(divisor)
    # 4
    return max(list_of_common_divisors)

if __name__ == '__main__':
    n = 2
    for _ in range(3):
        numbers = np.random.choice(1000, n, replace=False)
        print("Numbers: ", numbers, math.gcd(*numbers))
        result = find_great_common_divisors(numbers)
        print(result)