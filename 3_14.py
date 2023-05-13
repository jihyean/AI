import numpy as np

A = np.array([2, 6, 3, 1])
B = np.array([[2, 6, 3, 1], [0, 7, 1, 1]])

print("np.max(A) ==", np.max(A))
print("np.argmax(A) ==", np.argmax(A))

print("np.max(B) ==", np.max(B))
print("np.argmax(B) ==", np.argmax(B))