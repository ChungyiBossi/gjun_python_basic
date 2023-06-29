set_a = set([1,2,3,5,5,6,6])
set_b = set([4,4,5,5,6,6])
print(f"Set a: {set_a}, Set b: {set_b}")
print(set_a.difference(set_b))
print(set_b.difference(set_a))

print("symmetric_difference: ", set_a.symmetric_difference(set_b))
print("symmetric_difference: ", set_b.symmetric_difference(set_a))
print("symmetric_difference: ", set.symmetric_difference(set_a, set_b))