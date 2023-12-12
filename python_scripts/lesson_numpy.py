# pip install numpy
import numpy as np
n = np.random.randint(1, 50000) # 數字串列的長度
major_element = np.random.randint(-1 * 10 ** 9, 10 ** 9) # 隨機一個Major element
part_2 = np.full(n - n // 2 + 1, major_element) # 把Major element 擴展為一個長度為n/2的串列 來符合題意
part_1 = np.random.randint(-1 * 10 ** 9, 10 ** 9, n // 2 - 1) # 填滿剩下的一半
print("Major element =", major_element)
test_case = np.concatenate([part_1, part_2])
np.random.shuffle(test_case)
# print(len(test_case), n)

