from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()

iris_x = iris.data
iris_y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(iris_x, iris_y, test_size=0.25, random_state=321)

print("x_train_shape=", X_train.shape)
print("x_test_shape=", X_test.shape)

#3. model 생성
log_model = LogisticRegression(solver='liblinear', max_iter=1000)
log_model.fit(X_train, Y_train)

print("\n coef=", log_model.coef_)
print("\n intercept=", log_model.intercept_)

# 4. model 평가
y_pred = log_model.predict(X_test)

acc = accuracy_score(Y_test, y_pred)
print('\n accuracy =', acc)

print("2270005_KGH")