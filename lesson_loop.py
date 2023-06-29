list_a = ['a', 'b', 'c', 'd', 'e']
print(list_a)
# replace with for-loop
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[3])
# print(list_a[4])
# for letter in list_a:
#     for letter_upper in list_a:
#         print("Letter: ", letter)
#         print("Letter upper: ", letter_upper.upper())
#     print("------------------------------------------")
    
# enumerate
# for index, letter in enumerate(list_a):
#     index = index + 1
#     print(index, ":", letter * index)

import numpy as np
list_n = np.random.randint(1, 1000, 30)

list_even = list()
list_odd  = list()
list_five = list()
list_three_or_five = list()

for number in list_n:
    if number % 2 == 0: # even
        list_even.append(number)
    else: # odd
        list_odd.append(number)

    if number % 5 == 0:
        list_five.append(number)
        list_three_or_five.append(number)
    elif number % 3 == 0:
        list_three_or_five.append(number)

# comprehension
list_even = [number for number in list_n if number % 2 == 0]
list_odd  = [number for number in list_n if number % 2 == 1]
list_five = [number for number in list_n if number % 5 == 0]
list_three_or_five = [number for number in list_n if number % 3 == 0  or number % 5 == 0]
print("list_even: ", list_even)
print("list_odd: ", list_odd)
print("list_five: ", list_five)
print("list_three_or_five: ", list_three_or_five)
print(len(list_even) + len(list_odd))


sorted_even_numbers = sorted([number for number in list_n if number % 2 == 0])
for even_number in sorted_even_numbers:
    print(even_number)