import numpy as np

A = np.array([ [10, 20, 30, 40], [50, 60, 70, 80] ])

it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
    
    idx = it.multi_index
    
    print('index => ', idx, ', value =>', A[idx])
    
    it.iternext()