import matplotlib.pyplot as plt

# Example data
x = [150, 160, 170, 180, 190]
y = [50, 60, 65, 80, 85]

plt.scatter(x, y, color = 'red', s = 100, label = 'Height vs Weight', marker = 'D')
plt.title("Simple Scatter Plot")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.show()
