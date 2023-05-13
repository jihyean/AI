import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0,10)
Y1 = np.ones(10)
Y2 = X
Y3 = X**2
plt.plot(X, Y1, X, Y2, X, Y3)
plt.show()