import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]      # X-axis values (e.g. days)
y = [2, 4, 6, 4, 10]     # Y-axis values (e.g. prices)

plt.plot(x, y, label ='Line A', color = 'green', marker = 'o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.legend()
plt.show()
