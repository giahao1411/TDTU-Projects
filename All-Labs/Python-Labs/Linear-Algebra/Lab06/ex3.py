#bai 3

import numpy as np

C1 = np.array([
    [5, -4, 2],
    [-1, 2, 3],
    [-2, 1, 0]
])

C2 = np.array([
    [1, 7, 3],
    [4, -2, -2],
    [-2, -1, 1]
])

C3 = np.array([[2, 3], [1, -1]])

#frobenius - can bac 2 cac phan tu trong ma tran cong roi sqrt chung

norm_frobenius_C1 = np.linalg.norm(C1, 'fro')
norm_frobenius_C2 = np.linalg.norm(C2, 'fro')
norm_frobenius_C3 = np.linalg.norm(C3, 'fro')

print("frobenius norm C1 = ", norm_frobenius_C1)
print("frobenius norm C2 = ", norm_frobenius_C2)
print("frobenius norm C3 = ", norm_frobenius_C3)

#euclide norm

E = np.array([
    [4, 8, -2, 6],
    [-3, 2, 4, -1],
    [1, 5, 3, 2]
])

euclide_norm = np.linalg.norm(E, 'fro')
print("euclide norm = ", euclide_norm)