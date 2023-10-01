#bai 4

import numpy as np 

A = np.array([
    [1, 0, 2, 3],
    [4, -1, 0, 2],
    [0, -1, -8, -10]
])

U, s, Vt = np.linalg.svd(A)
null_space = Vt[-2:].T

v1 = null_space[:, 0]
v2 = null_space[:, 1]

print("Cau a:")
print("v1:", v1)
print("v2:", v2)