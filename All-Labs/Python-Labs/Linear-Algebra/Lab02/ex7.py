#bai 7

import numpy as np

A = np.array([
    [2, 7, 9, 7],
    [3, 1, 5, 6],
    [8, 1, 2, 5]
])

#cau a:
B = A[0:4, 1:5:2]
print("Cau a:\n", B)

#cau b:
C = A[0:4, 0:5:2]
print("Cau b:\n", C)

#cau c:
A1 = np.reshape(A, (4, 3))
print("Cau c:\n", A1)