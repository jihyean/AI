import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

cars = pd.read_csv('cars.csv', nrows=None)

x=cars['speed']
y=cars['dist']

lr = LinearRegression()

lr.fit(x.value.reshape(-1,1), y)
print('w = ', lr.coef_, 'b=', lr.intercept_)
print('speed =19', 'dist=', 'b=', lr.predict([[19]]))

plt.xlabel("Speed")
plt.xlabel("Distance")
plt.plot(x, y, 'o')
plt.plot(x, lr.predict(x.values.reshape(-1, 1)))
plt.show()
