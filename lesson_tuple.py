list_height = [183, 179, 160, 148, 155]
list_name  = ["John", "Joe", "Mark", "May", "Jue"]
list_tuple = [
    (list_height[0], list_name[0]),
    (list_height[1], list_name[1]),
    (list_height[2], list_name[2]),
    (list_height[3], list_name[3]),
    (list_height[4], list_name[4])
]  # [(176, "John"), (183, "Joe")]
list_tuple_2 = [
    (list_name[0], list_height[0]),
    (list_name[1], list_height[1]),
    (list_name[2], list_height[2]),
    (list_name[3], list_height[3]),
    (list_name[4], list_height[4])
]  # [("John", 176), ("Joe", 133)]



print(list_tuple)
print("Tuple (height, name): ", sorted(list_tuple))
print("Tuple (name, height): ", sorted(list_tuple_2, key=lambda x:x[1]))
# ("May", 148, 45) -> key=lambda x: (x[1], x[2])