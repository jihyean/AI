from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()

iris_x = iris.data
iris_y = iris.target

print("x_shape=", iris_x.shape)
print("y_shape=", iris_y.shape)

#3. model 생성
log_model = LogisticRegression(solver='liblinear', max_iter=1000)
log_model.fit(X=iris_x, y=iris_y)

print("\n coef=", log_model.coef_)
print("\n intercept=", log_model.intercept_)

# 4. model 평가
y_pred = log_model.predict(iris_x)

acc = accuracy_score(iris_y, y_pred)
print('\n accuracy =', acc)

print("2270005_KGH")