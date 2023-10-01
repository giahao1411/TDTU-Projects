#bai 3

import numpy as np

a = np.array([i for i in range(1, 10)])

A = np.reshape(a, (3, 3))
B = np.flip(A, axis = 1)    #horizontally -> axis = 1

print("Ma tran:\n", B)
