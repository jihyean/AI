import matplotlib.pyplot as plt

X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

plt.plot(X, Y1, label="Seoul")
plt.plot(X, Y2, label="Busan")
plt.xlabel("day")
plt.xlabel("temperature")
plt.legend(loc="upper left")
plt.title("Temperatuers of Cities")
plt.show()