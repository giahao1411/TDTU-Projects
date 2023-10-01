#bai 12

import numpy as np

def gram_schmidt(A):
    Q = np.zeros_like(A)                                  #initialize Q matrix
    for i in range(A.shape[1]):
        v = A[:, i]                                       #select a column vector from A
        for j in range(i):
            q = Q[:, j]                                   #select a column vector from Q
            v -= np.dot(v, q) * q                         #subtract the projection of v onto q from v
        Q[:, i] = v / np.linalg.norm(v)                   #normalize v and add it to Q
    return Q

A = np.array([
    [-10, 13, 7, -11], 
    [2, 1, -5, 3], 
    [-6, 3, 13, -3], 
    [16, -16, -2, 5], 
    [2, 1, -5, -7]
])

print("Orthogonal basis for column space of A = \n", gram_schmidt(A))