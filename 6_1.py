from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
digit = datasets.load_digits()
X_train, x_test, Y_train, y_test = train_test_split(digit.data,
                                              digit.target, train_size = 0.6) #60퍼를 트레이닝, 나머지 40퍼를 테스트

#MLP 분류기 모델을 학습 100, 100, 200 이니까 은닉층 3개 은닉층이 많다고 다 좋은 것 아님
mlp = MLPClassifier(hidden_layer_sizes=(100,100,200), learning_rate_init=0.001,
                    batch_size=32, max_iter=300, solver='sgd', verbose=True) #verbose = True > 학습되는 걸 볼 수 있게
mlp.fit(X_train, Y_train)

y_pred = mlp.predict(x_test) # 테스트 집합으로 예측

acc = accuracy_score(y_test, y_pred)

print('\n MLP accuracy =', acc)

print("2270005 권지현")