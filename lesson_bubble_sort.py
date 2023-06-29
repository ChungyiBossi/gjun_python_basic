import numpy as np 
n = 6
bubbles = np.random.choice(10, n, replace=False)
print(list(bubbles))

# n = 6
# round 0:
#   idx: 1~5, 
# round 1:
#   idx: 1~4, 
# round 2:
#   idx: 1~3, 
# round 3:
#   idx: 1~2,
# round 4:
#   idx: 1~1
# round + idx <= 5, idx <= 5 - round, idx <= n - 1 - round
# Time Complexity = O(n**2)
for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles):
        if index < n - round - 1:
            print(f"Round:{round}, i:{bubbles[index]}, j:{bubbles[index + 1]}")
            print(f"Bubbles before: {bubbles}")
            if bubbles[index] > bubbles[index + 1]:
                temp = bubbles[index + 1]
                bubbles[index + 1] = bubbles[index]
                bubbles[index] = temp
            print(f"Bubbles  after: {bubbles}")

# print(sorted(bubbles))