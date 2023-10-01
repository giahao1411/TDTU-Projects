#bai 4

import numpy as np

a = np.array([i for i in range(1, 10)])

A = np.reshape(a, (3, 3))
C = np.flip(A, axis = 0)    #vertically -> axis = 0

print("Ma tran:\n", C)