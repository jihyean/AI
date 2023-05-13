import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

prestige = pd.read_csv('prestige.csv', nrows= None)
print(prestige.head())

x = prestige[['education', 'women', 'prestige']]
y = prestige[['income']]
print("x dmen=", x.ndim, "y dmen=", y.ndim)
lr = LinearRegression()

lr.fit(x, y)
print('w= ', lr.coef_, 'b=', lr.intercept_)
myincome=[[14.3, 0.9, 60.0]]
print('myincome predtiction=', lr.predict(myincome))

plt.figure(figsize=(12,4))
plt.subplots_adjust(wspace=0.5)
plt.subplot(131)
plt.title("2270005_KJH")
plt.xlabel("Education")
plt.ylabel("Income")
plt.scatter(prestige[['education']], prestige[['income']])

plt.subplot(132)
plt.title("2270005_KJH")
plt.xlabel("Women")
plt.ylabel("Income")
plt.scatter(prestige[['women']], prestige[['income']])

plt.subplot(133)
plt.title("2270005_KJH")
plt.xlabel("Prestige")
plt.ylabel("Income")
plt.scatter(prestige[['prestige']], prestige[['income']])
plt.show()