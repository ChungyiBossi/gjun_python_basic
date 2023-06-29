from matplotlib import pyplot as plt

# 1
list_y = [2, 4, 6, 8]
plt.plot(list_y)
# plt.show()
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend(["First Line"])
plt.title("First Plot")
plt.savefig("./plot_image/first_plot.jpg")

plt.cla()

# 2
list_x_y = [(1,2), (2,4), (9,6), (7,10)]
list_x_y.sort()
plt.plot([x for x, y in list_x_y], [y for x, y in list_x_y], marker='^')
# plt.show()
plt.savefig("./plot_image/second_plot.jpg")
plt.cla()

# 3
n = range(1,30)
plt.plot(n, n, marker='o', linestyle='--', color='y')   # Yellow marker-o Dash
plt.plot(n, [i*i for i in n], "rs", linestyle="-") # Red Square Dash
plt.plot(n, [i**3 for i in n], "g^--") # Green Triangle Dash
# plt.plot(n, n, "y--", n, n**2, "rs", n, n**3, "g^")
plt.legend(["n", "n*n", "n*n*n"])
plt.savefig("./plot_image/third_plot.jpg")
plt.cla()

# 4
n = range(1,30)
plt.scatter(n, n, c='y') 
plt.scatter(n, [i*i for i in n], c="r")
plt.scatter(n, [i**3 for i in n], c="g")
plt.legend(["n","n*n","n*n*n"])
plt.savefig("./plot_image/forth_plot.jpg")
plt.cla()

# 5
import numpy as np
x = np.random.randint(1, 100, 20)
y = np.linspace(1, 100, 20)
plt.scatter(sorted(x), y, c='y') 
plt.savefig("./plot_image/fifth_random_scatter.jpg")
plt.cla()

# 6
x = np.random.randint(1,100,10000)
plt.hist(x, bins=10)
plt.savefig("./plot_image/sixth_histogram.jpg")
plt.cla()


# 7
x = [1, 2, 3, 4]
plt.pie(x, explode=[0, 0, 0.1, 0.1], labels=['1', '2', '3','4'])
plt.savefig("./plot_image/seventh_pie.jpg")
plt.cla()