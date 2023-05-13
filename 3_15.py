import numpy as np

loaded_data = np.loadtxt('./ch03_test.csv', delimister=',', dtype=np.float32)

print('loaded_data.shape = ', loaded_data.shape)

print(loaded_data)