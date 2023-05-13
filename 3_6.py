import numpy as np

A = np.array([[1, 2, 3, 4],
              [10, 20, 30, 40],
              [100, 200, 300, 400]])
print(A.shape)
print(A)
B = A.reshape(-1, 3)
print('B.shape = ', B.shape)
print(B)
C = A.reshape(-1, 6)
print('C.shape = ', C.shape)
print(C)