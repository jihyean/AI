from sklearn.datasets import load_breast_cancer         #dataset
from sklearn.linear_model import LogisticRegression     #모델생성
from sklearn.metrics import accuracy_score

breast = load_breast_cancer()
print(breast.DESCR)

breast_x = breast.data
breast_y = breast.target    # 0 or 1인 데이터

print("x_shape=", breast_x.shape)
print("y_shape=", breast_y.shape)

#3. model 생성
log_model = LogisticRegression(solver='liblinear', max_iter=1000)
log_model.fit(X=breast_x, y=breast_y)

print("\n coef=", log_model.coef_)
print("\n intercept=", log_model.intercept_)

# 4. model 평가
y_pred = log_model.predict(breast_x)

acc = accuracy_score(breast_y, y_pred)
print('\n accuracy =', acc)

print("2270005_KGH")