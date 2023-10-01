#bai 9

import numpy as np

def is_orthogonal_set(vectors):
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if vectors[i].shape != vectors[j].shape:
                return False
            if np.dot(vectors[i], vectors[j]) != 0:
                return False
    return True

A = np.array([
    [3, 1, 1],
    [-1, 2, 1],
    [-1/2, 2, 7/2]
]).T

if is_orthogonal_set(A):
    print("The vectors are orthogona")
else:
    print("The vectors are not orthogonal")