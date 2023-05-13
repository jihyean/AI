import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.normal(size=1000)

plt.hist(numbers)
plt.xlabel("value")
plt.ylabel("freq")
plt.show()