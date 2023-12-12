# Create
list_1 = list()
list_2 = []

string_for_list = "I want to play a game!".replace(" ", "**")
print(string_for_list)
list_from_string = string_for_list.split('**')
print(list_from_string)
list_from_string_2 = "Eat an apple a day, keep doctor away.".split(" ")
print(list_from_string_2)

# Get
list_3 = [1, 2, 3, 4, 5, 6, 7]
x = list_3[0] # 1
y = list_3[5] # 6
z = list_3[-1] # 7
w = list_3[1:3] # [2, 3]
v = list_3[1:-1] # [2,3,4,5,6]
print(x, y, z, w, v)

list_3[-1] = [55, 66]
list_3[1:3] = [10, 11]
print(list_3) # [1, 10, 11, 4, 5, 6, [55, 66]]

# expend, append
list_4 = ["A", "B", "C"]
list_4.append("D")
print(list_4)
list_4.extend(["E", "F"]) # list_4 = list_4 + ["E", "F"]
print(list_4)
list_4.append(["G", "H"])
print(list_4)
list_4.extend("X") # not wrong anymore
print(list_4)

# pop, remove
pop_1 = list_4.pop()
print("pop! ", pop_1, ", list:", list_4)

list_4.remove("E")
print("remove!", list_4)

# sort
list_for_sort = [5, 6 ,8 ,1, 9, 8, 9]
list_for_sort.sort()
print("sort:", list_for_sort)
list_for_sort.sort(reverse=True)
print("sort (reversed):", list_for_sort)

list_for_sorted = [5, 6, 8, 9, 9, 1, 3, 4]
print("Sorted:", sorted(list_for_sorted))
print("Original:", list_for_sorted)