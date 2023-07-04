# N個無序數字, 要把數字由小到大排序
# 1. 每一輪, 會把最小的數字, 放到對應的位置
#   eg. 第一輪, 最小的數字會放到第一位, 從第一個位置開始
#       第二輪, 最小的數字會放到第二位, 從第二個位置開始
# 2. 共要做 N-1 輪

import numpy as np
N = 5
numbers = np.random.choice(100, N, replace=False)
print("Berfore: ", numbers)

for round in range(N): # 第0 ~ 4輪
    # 預設每一輪的最小值
    round_minimum = numbers[round]
    round_minimum_index = round

    # 找最小值
    for index in range(round, N):
        if numbers[index] < round_minimum:
            round_minimum = numbers[index]
            round_minimum_index = index

    # 交換
    if round != round_minimum_index:
        numbers[round], numbers[round_minimum_index] = numbers[round_minimum_index], numbers[round]

print("After: ", numbers)