from sklearn import datasets
import matplotlib.pyplot as plt

digit = datasets.load_digits()
plt.imshow(digit.images[0], cmap=plt.cm.gray_r) #0번 샘플을 그림
plt.show()
print(digit.data[0])    #0번의 샘플의 최솟값을 그림
print("이 숫자는 ", digit.target[0], "입니다.")