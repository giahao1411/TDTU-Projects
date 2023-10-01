#bai 1 

import numpy as np 

#cau a

A = np.array([
    [-1, 3.5, 14],
    [0, 5, -26],
    [0, 0, 2]
])

eval_a, vector_a = np.linalg.eig(A)
print("a. eigenvalues = ", eval_a)
print("- eigenvectors = \n", vector_a)

det_a = np.linalg.det(A)
print("- det_a = ", round(det_a, 5))

#cau b
B = np.array([
    [-2, 0, 0],
    [99, 0, 0],
    [10, -4.5, 10]
])

eval_b, vector_b = np.linalg.eig(B)
print("\nb. eigenvalues = ", eval_b)
print("- eigenvectors = \n", vector_b)

det_b = np.linalg.det(B)
print("- det_b = ", round(det_b, 5))

#cau c 
C = np.array([
    [5, 5, 0, 2],
    [0, 2, 3, 6],
    [0, 0, 3, -2],
    [0, 0, 0, 5]
])

eval_c, vector_c = np.linalg.eig(C)
print("\nc. eigenvalues = ", eval_c)
print("- eigenvectors = \n", vector_c)

#another way to calculate det_c by multiply each value in eigenvalues
det_c = 1
for i in eval_c:
  det_c *= i

print("- det_c = ", round(det_c, 5))

#cau d 