#bai 8

import numpy as np 

def computeSVD(A):
  return np.linalg.svd(A)
  

#cau a
B1 = np.array([
    [-18, 13, -4, 4],
    [2, 19, -4, 12],
    [-14, 11, -12, 8],
    [-2, 21, 4, 8]
])

print("a. matrix B1 svd = \n", computeSVD(B1))

#cau b
B2 = np.array([
    [6, -8, -4, 5, -4],
    [2, 7, -5, -6, 4],
    [0, -1, -8, 2, 2],
    [-1, -2, 4, 4, -8]
])

print("\nb. matrix B2 svd = \n", computeSVD(B2))