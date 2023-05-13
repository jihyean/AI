import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_datasets("iris")
print(iris.head())

sns.pairplot(iris, hue = 'species')
plt.show()