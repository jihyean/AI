import numpy as np

C = np.array([1, 2, 3])

print("C.shpae == ", C.shape)
print(C)                        #1차원인 벡터라 값이 없다가
C = C.reshape(1, 3)
print("C.shpae == ", C.shape)   #매트릭스로 바뀌고 생김
print(C)