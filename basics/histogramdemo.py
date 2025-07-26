import matplotlib.pyplot as plt

# Example data
data = [67, 70, 72, 68, 75, 78, 72, 69, 71, 74, 73, 77, 76, 70, 71]

plt.hist(data, color = 'red', bins = 5, edgecolor = 'black')
plt.title("Simple Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
