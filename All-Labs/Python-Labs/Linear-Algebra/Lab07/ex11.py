#bai 11

import numpy as np

def has_orthonormal_columns(A):
    U = A / np.linalg.norm(A, axis=0) 
    UTU = np.dot(U.T, U) 
    return np.allclose(UTU, np.eye(UTU.shape[0]))

A = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])

B = np.array([
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
])

print("Has orthonormal column:", has_orthonormal_columns(A))
print("Has orthonormal column:",has_orthonormal_columns(B)) 
