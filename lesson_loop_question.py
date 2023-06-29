list_a = range(1, 101)
# print(list(list_a))

# Q_1
# list_square = list()
# for x in list_a:
#     list_square.append(x**2)
list_square = [x**2 for x in list_a]
# print(list_square, len(list_square))

# Q_2
c = 0
list_square_sum = list()
for x in list_a:
    c = c + x**2
    list_square_sum.append(c)
# print(list_square_sum[-1], sum(list_square))
 
# comprehension
list_square_sum = [sum([y**2 for y in range(1, x + 1)]) for x in list_a]
# print(list_square_sum[-1], sum(list_square))


# Q_3: Continue - square odd only
# [1**2, 2, 3**2, 4, 5**2.....]
list_square_odd = list()
for x in list_a:
    if x % 2 == 0:
        list_square_odd.append(x)
        continue
    else:
        list_square_odd.append(x**2)
    # print("square it!!!!", x)
# print(list_square_odd, len(list_square_odd))

# Q_3: Continue - While loop version
# [1**2, 2, 3**2, 4, 5**2.....]
list_square_odd = list()
index = 0
while index < len(list_a):
    x = list_a[index]
    index += 1  # index = index + 1
    if x % 2 == 0:
        list_square_odd.append(x)
        continue
    else:
        list_square_odd.append(x**2)
    # print("square it!!!!", x)
# print(list_square_odd, len(list_square_odd))

# Q_4: Break
# square: 1-50
list_square_50 = list()
for x in list_a:
    if x > 50:
        # print("Over 50!")
        break
    else:
       list_square_50.append(x**2)
# print(list_square_50, len(list_square_50))

# Q_4: Break - while loop version
list_square_50 = list()
index = 0
while index < len(list_a):
    # 例外條件
    if list_a[index] > 50:
        break
    list_square_50.append(list_a[index]**2)
    index = index + 1
# print(list_square_50, len(list_square_50))