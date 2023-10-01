#bai 4 

import numpy as np

A = np.array([
    [-2, 2, -3],
    [2, 1, -6],
    [-1, -2, 0]
])

#A = A 
eval_a, vector_a = np.linalg.eig(A)
print("- A = A, eigenvalues = ", eval_a)
print("eigenvectors = \n", vector_a)
print("det_a = ", round(np.linalg.det(A), 5))

#A = A.T
B = A.T

eval_b, vector_b = np.linalg.eig(B)
print("\n- A = A.T, eigenvalues = ", eval_b)
print("eigenvectors = \n", vector_b)
print("det_a.T = ", round(np.linalg.det(B), 5))

#A = A^-1
C = np.linalg.inv(A)

eval_c, vector_c = np.linalg.eig(C)
print("\n- A = A^-1, eigenvalues = ", eval_c)
print("eigenvectors = \n", vector_c)
print("det_a^-1 = ", round(np.linalg.det(C), 5))