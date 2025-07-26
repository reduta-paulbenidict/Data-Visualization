import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Bananas', 'Cherries']
values = [50, 30, 40]

plt.bar(categories, values, label = 'Fruit Quantity', color = 'blue', width='0.5')
plt.title("Simple Bar Chart")
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.legend()
plt.show()
