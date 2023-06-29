import numpy as np
x = np.random.randint(1, 10)
y = np.random.randint(1, 10)

# if x > y:
#     print("bigger")
# else:
#     if x == y:
#         print("equal")
#     else:
#         print("smaller")

if x > y:
    print("bigger")
elif x == y:
    print("equal")
else:
    print("smaller")

print(f"x:{x}, y:{y}")

# comprehension
result = "bigger" if x > y else "equal or smaller"
print(result)

# Lesson
is_hot = True
is_raining = True
is_holiday = False
is_typhoon = False
is_emotional = False

is_going_to_school = True
# if is_hot and is_raining:
#     print("Hot and raining")
#     is_going_to_school = False

# if is_emotional and is_raining:
#     print("Emo and raining")
#     is_going_to_school = False

# if is_holiday or is_typhoon:
#     print("Holiday and typhoon")
#     is_going_to_school = False

# refactor
if (is_raining and (is_hot or is_emotional)) or is_holiday or is_typhoon:
    is_going_to_school = False

print(is_going_to_school)


